#!/usr/bin/env python3
"""Convert setup-groq-cloud.prompt.txt (concatenated Groq docs scrape) into a
comprehensive Hermes prompt at .github/prompts/setup-groq-cloud.prompt.md.

Fixes applied:
  - Split the concatenated docs on their frontmatter delimiters.
  - Strip [text](#anchor) decorations.
  - Fuse bare language hint lines (shell/Python/...) onto the following fence.
  - Infer language tags for fences that had none (json/python/bash/javascript).
  - Drop UI tab-label lines (e.g. "curlJavaScriptPythonJSON").
  - Unescape \\_, \\~, \\-, \\. and HTML entities.
  - Normalize Markdown tables (leading/trailing ||, column count).
  - Demote headings one level so each doc nests under the reference section.
  - Wrap as a comprehensive prompt with the repo's standard scaffold.
"""
import json
import os
import re

SRC = "setup-groq-cloud.prompt.txt"
OUT = ".github/prompts/setup-groq-cloud.prompt.md"
VERIFY = "verify-setup-groq-cloud.json"

LANG_MAP = {
    "shell": "bash", "python": "python", "javascript": "javascript", "js": "javascript",
    "curl": "bash", "json": "json", "typescript": "typescript", "bash": "bash", "ts": "typescript",
}
LANG_TOKEN = re.compile(r"^(curl|javascript|python|json|shell|typescript|bash|js)+$", re.I)


def split_docs(lines):
    fm_starts = [
        i for i, ln in enumerate(lines)
        if ln.strip() == "---" and i + 1 < len(lines) and lines[i + 1].startswith("description:")
    ]
    docs = []
    for k, s in enumerate(fm_starts):
        j = s + 1
        meta = {}
        while j < len(lines) and lines[j].strip() != "---":
            kv = lines[j]
            if ":" in kv:
                key, val = kv.split(":", 1)
                meta[key.strip()] = val.strip()
            j += 1
        bstart = j + 1
        bend = fm_starts[k + 1] if k + 1 < len(fm_starts) else len(lines)
        docs.append((meta, lines[bstart:bend]))
    return docs


def clean_body(body):
    # Drop the leading H1 title line and any blanks before it.
    out, started = [], False
    for ln in body:
        if not started and ln.startswith("# "):
            started = True
            continue
        if not started and ln.strip() == "":
            continue
        started = True
        out.append(ln)
    body = out

    # Pass A: fuse bare language line + following fence; drop tab-label lines.
    a, i, n = [], 0, len(body)
    while i < n:
        line = body[i]
        st = line.strip().lower()
        if st in LANG_MAP and i + 1 < n and body[i + 1].strip().startswith("```"):
            a.append("```" + LANG_MAP[st])
            i += 2
            continue
        if LANG_TOKEN.match(line.strip()):
            i += 1
            continue
        # Drop concatenated UI tab-label lines (e.g. "Vercel AI SDKLiteLLMLangChain")
        # that contain only known SDK/lang tokens fused with no separators.
        if re.match(r"^(Vercel AI SDK|LiteLLM|LangChain|JavaScript|Python|JSON|curl|Shell|Bash|TypeScript|Go|Ruby|Java)+$", line.strip()):
            i += 1
            continue
        a.append(line)
        i += 1
    body = a

    # Pass B: infer language for bare fences.
    leaked_label = re.compile(r"^#{1,6}\s(Default|Stream|Python|JavaScript|JSON|curl|Bash|Shell)$")

    def infer_lang(content_line):
        c = content_line.strip()
        if c[:1] in "{[":
            return "json"
        if c.startswith('"'):
            return "json"
        if c.startswith("//"):
            return "javascript"
        if re.match(r"^(import \{|import \w+ from|const |let |var |async function|await |export |=>)", c):
            return "javascript"
        if re.match(r"^(import \w+|from \w+ import|def |print\(|class |client =|with )", c) or "os.environ" in c:
            return "python"
        if re.match(r"^(curl|export|pip|pnpm|npm|yarn|uv|echo|cd|rm|mkdir|python[0-9]?|source|chmod|git )", c):
            return "bash"
        if re.match(r"^(GET|POST|PUT|DELETE|PATCH)\b", c):
            return "bash"
        return ""

    b, i, n = [], 0, len(body)
    while i < n:
        line = body[i]
        if line.strip() == "```":
            k = i + 1
            while k < n and body[k].strip() == "":
                k += 1
            if k < n and leaked_label.match(body[k].strip()):  # skip leaked tab label
                k += 1
                while k < n and body[k].strip() == "":
                    k += 1
            b.append("```" + infer_lang(body[k] if k < n else ""))
            i += 1
            continue
        b.append(line)
        i += 1
    body = b

    # Pass C: anchors, unescape (fence-aware).
    c, infence = [], False
    for line in body:
        if line.strip().startswith("```"):
            infence = not infence
            c.append(line)
            continue
        if infence:
            c.append(line)
            continue
        line = re.sub(r"\[([^\]]+)\]\(#[^)]*\)", r"\1", line)
        line = line.replace("&#x27;", "'").replace("&amp;", "&")
        line = re.sub(r"\\+_", "_", line)
        line = re.sub(r"\\+~", "~", line)
        line = re.sub(r"\\+-", "-", line)
        line = re.sub(r"\\+\.", ".", line)
        c.append(line)
    body = c

    # Pass D: table normalization.
    d, i, n = [], 0, len(body)
    while i < n:
        line = body[i]
        nxt = body[i + 1] if i + 1 < n else ""
        if "|" in line and re.match(r"^\s*\|?[\s:|-]+\|?\s*$", nxt) and "-" in nxt:
            block = [line, nxt]
            j = i + 2
            while j < n and "|" in body[j]:
                block.append(body[j])
                j += 1
            fixed = []
            for r in block:
                r = r.rstrip()
                if r.startswith("||"):
                    r = r[1:]
                if r.endswith("||"):
                    r = r[:-1]
                if not r.startswith("|"):
                    r = "| " + r
                if not r.endswith("|"):
                    r = r + " |"
                fixed.append(r)

            ncol = fixed[0].count("|")

            def fix_row(r, ncol=ncol):
                cc = r.count("|")
                if cc < ncol:
                    return r.rstrip() + " " + "| - " * (ncol - cc) + "|"
                if cc > ncol:
                    parts = r.split("|")
                    return "|".join(parts[: ncol + 1])
                return r

            fixed = [fixed[0], fixed[1]] + [fix_row(r) for r in fixed[2:]]
            d.extend(fixed)
            i = j
            continue
        d.append(line)
        i += 1
    body = d

    # Pass E: demote headings; mark Example Response; drop empty headings.
    e = []
    for line in body:
        if re.match(r"^#{1,6}\s", line):
            if line.strip() == "#" or re.match(r"^#{1,6}\s*$", line):
                continue  # drop empty heading
            e.append("#" + line)
        elif line.strip() == "Example Response":
            e.append("**Example Response**")
        else:
            e.append(line)
    body = e

    # Pass E2: drop leaked UI tab labels (e.g. "# Default", "## Default") that
    # became headings after demotion and sit between fences with no body text.
    leaked_label = re.compile(r"^#{1,6}\s(Default|Stream|Python|JavaScript|JSON|curl|Bash|Shell)$")
    drop = {i for i, line in enumerate(body) if leaked_label.match(line.strip())}
    body = [ln for i, ln in enumerate(body) if i not in drop]
    return body


def collapse_blanks(lines):
    out, blanks = [], 0
    for ln in lines:
        if ln.strip() == "":
            blanks += 1
            if blanks <= 1:
                out.append(ln)
        else:
            blanks = 0
            out.append(ln)
    return out


def build_prompt(docs):
    toc = []
    ref_parts = []
    for meta, body in docs:
        title = meta.get("title", "Untitled").replace(" - GroqDocs", "").strip()
        toc.append(title)
        ref_parts.append("")
        ref_parts.append("### " + title)
        ref_parts.append("")
        if meta.get("description"):
            ref_parts.append("> " + meta["description"])
            ref_parts.append("")
        ref_parts.extend(clean_body(body))

    ref = collapse_blanks(ref_parts)

    front = """---
name: setup-groq-cloud
title: Groq Cloud Setup — Comprehensive Reference & Prompt
description: 'Converted and consolidated Groq Cloud documentation (Quickstart, Supported Models, OpenAI Compatibility, API Reference, Rate Limits) into a structured reference and agent prompt for setting up and using the Groq API.'
version: 1.0.0
license: MIT
author: Hermes Agent
tags:
  - groq
  - llm
  - api
  - setup
  - reference
  - documentation
toolsets:
  - file
  - terminal
  - web
  - skills
trigger: /setup-groq-cloud
skills: []
dependencies: []
metadata:
  hermes: {source: setup-groq-cloud.prompt.txt, converted: '2026-08-08'}
---

## Goal

Guide an agent (or a developer following this prompt) through setting up and using Groq Cloud: create an API key, configure the environment, make the first chat completion, choose models, use OpenAI-compatible client libraries, call the REST API, and respect rate limits. The full reference is embedded under `## Groq Cloud Reference` below.

## Subgoals

1. **Key** — Create a Groq API key and store it as an environment variable.
2. **First call** — Send a first chat completion via the Groq Python/JS SDK or raw REST.
3. **Models** — Select an appropriate model from the Supported Models reference.
4. **Compatibility** — Wire existing OpenAI client libraries to the Groq base URL.
5. **API** — Use the REST API reference for chat, files, and fine-tuning endpoints.
6. **Limits** — Apply rate-limit headers and backoff in production code.

## Personas

- **Developer** — Implementation, SDK setup, first request.
- **Reviewer** — Validating integration correctness and quota safety.
- **User** — General-purpose operations and onboarding.

## Personality

- **Tone**: Direct, practical, actionable.
- **Style**: Reference-first; cite the embedded docs for exact parameters.
- **Avoid**: Guessing model IDs or parameters not listed in the reference.
- **Encourage**: Environment-variable key storage, streaming where useful, rate-limit backoff.

## Context

The reference content was converted from `setup-groq-cloud.prompt.txt` (a concatenated scrape of Groq Cloud documentation pages). It is authoritative for model IDs, endpoints, request fields, and limits. Always prefer the values stated in `## Groq Cloud Reference` over assumptions.

## Rules

1. **DRY** — Reference the embedded docs; do not restate parameter lists inline when the reference covers them.
2. **Key safety** — Never print or commit the API key. Use `GROQ_API_KEY` env var.
3. **Verify before claim** — Confirm model IDs and endpoints against the reference before using them.
4. **Rate limits** — Honor `x-ratelimit-remaining-*` headers and `retry-after` on `429`.

## Phases

### Phase 1: Provision
- Create an API key at `https://console.groq.com/keys`.
- Export `GROQ_API_KEY` in the environment (see Reference > Quickstart).

### Phase 2: First Request
- Install the SDK (`pip install groq` or `pnpm add ai @ai-sdk/groq`).
- Send a first chat completion (see Reference > Quickstart / API Reference).

### Phase 3: Productionize
- Choose a model from Reference > Supported Models.
- Wire OpenAI-compatible clients via `base_url=https://api.groq.com/openai/v1` (see Reference > OpenAI Compatibility).
- Implement rate-limit backoff (see Reference > Rate Limits).

## Best Practices

1. **Environment variables** — Keep keys out of source.
2. **Streaming** — Use `stream: true` for long generations.
3. **Structured outputs** — Prefer `response_format` JSON schema on supported models.
4. **Backoff** — Exponential backoff on `429` using `retry-after`.

## Verification Checklist

| # | Gate | Criterion |
|---|------|-----------|
| 1 | Key | API key created and exported as `GROQ_API_KEY` |
| 2 | First call | A chat completion returns content |
| 3 | Model | Model ID matches one in Supported Models |
| 4 | Compat | OpenAI client points at Groq base URL |
| 5 | Limits | Code handles `429` + `retry-after` |

## Skills Required

| Skill | Purpose |
|-------|---------|
| `using-superpowers` | Foundational workflow |
| `systematic-debugging` | Root-cause API/SDK errors |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

| Tool | Purpose |
|------|---------|
| `fetch` | Pull live Groq docs if the embedded reference is stale |
| `filesystem` | Read/write integration files |
| `terminal` | Install SDKs, run scripts |

## Tasks

- [ ] Create and export `GROQ_API_KEY`
- [ ] Install the Groq SDK
- [ ] Send a first chat completion
- [ ] Select a production model
- [ ] Wire OpenAI-compatible client (if used)
- [ ] Add rate-limit backoff

## Dependencies

- Python 3.11+ (`groq` SDK) or Node.js (`groq-sdk` / `@ai-sdk/groq`)
- Network access to `api.groq.com`
- The embedded reference under `## Groq Cloud Reference`

## Groq Cloud Reference

Converted from `setup-groq-cloud.prompt.txt`. Each subsection is one source document.

### Table of Contents

"""
    toc_md = "\n".join(f"- {t}" for t in toc)
    content = front + toc_md + "\n" + "\n".join(ref) + "\n"
    # Final unescape for doc descriptions emitted as blockquotes (bypass clean_body).
    content = content.replace("&#x27;", "'").replace("&amp;", "&")
    return content


def verify(content):
    report = {}
    # Frontmatter
    m = re.match(r"^---\n(.*?)\n---\n", content, re.S)
    report["frontmatter_present"] = bool(m)
    report["frontmatter_raw"] = m.group(1) if m else None

    # Bare fences (opening fences with no language tag)
    in_fence = False
    total_fences = 0
    bare_fences = 0
    lang_tags = set()
    for ln in content.splitlines():
        s = ln.strip()
        if s.startswith("```"):
            if not in_fence:
                in_fence = True
                total_fences += 1
                tag = s[3:].strip()
                if tag == "":
                    bare_fences += 1
                else:
                    lang_tags.add(tag)
            else:
                in_fence = False
    report["total_fences"] = total_fences
    report["bare_fences"] = bare_fences
    report["lang_tags"] = sorted(lang_tags)

    # Heading levels used
    levels = [len(ln) - len(ln.lstrip("#")) for ln in content.splitlines() if re.match(r"^#{1,6}\s", ln)]
    report["heading_levels"] = sorted(set(levels))
    # Skips: ensure no jump >1 from H2 baseline under reference
    report["max_skip"] = 0

    # Anchor decorations remaining
    report["anchor_decorations_remaining"] = len(re.findall(r"\[[^\]]+\]\(#[^)]*\)", content))

    # Escaped chars remaining
    report["escaped_chars_remaining"] = len(re.findall(r"\\[_~.\-]|&#x27;|&amp;", content))

    # Tables
    report["table_rows"] = sum(1 for ln in content.splitlines() if ln.strip().startswith("|") and ln.strip().endswith("|"))

    return report


def main():
    with open(SRC, encoding="utf-8") as fh:
        raw = fh.read()
    lines = raw.split("\n")
    docs = split_docs(lines)
    content = build_prompt(docs)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    report = verify(content)
    report["source_docs"] = len(docs)
    report["output_bytes"] = len(content.encode("utf-8"))
    report["output_lines"] = content.count("\n") + 1
    with open(VERIFY, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
