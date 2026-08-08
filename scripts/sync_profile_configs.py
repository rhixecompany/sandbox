#!/usr/bin/env python3
"""Bidirectional-safe propagation of root Hermes config.yaml/.env/auth.json to all
non-default profiles.

Strategy (root -> profiles, preserving per-profile identity):
  - config.yaml: deep-merge ROOT over PROFILE, then restore the profile's own
    top-level model.provider / model.default (the only meaningful per-profile
    identity). This eliminates cosmetic drift (comment escaping, provider aliases)
    while keeping each profile's model selection.
  - .env: copy ROOT .env into profiles whose .env is a placeholder (no active
    key= lines). Profiles that already have real secrets are left alone.
  - auth.json: copy ROOT auth.json into profiles that lack one.

Safety:
  - Timestamped backups of every overwritten file.
  - Secrets never printed; this script only reads/writes at the OS layer.
  - Idempotent: skips write if merged result == current profile file.
"""
import datetime
import os
import shutil
import sys

import yaml

HERMES = os.environ.get("HERMES_HOME", r"C:/Users/Alexa/AppData/Local/hermes")
ROOT_CFG = os.path.join(HERMES, "config.yaml")
ROOT_ENV = os.path.join(HERMES, ".env")
ROOT_AUTH = os.path.join(HERMES, "auth.json")

PROFILES = [
    "alexa", "code-architect", "creative-director", "cto", "designer", "dev",
    "exec-assistant", "ops", "patient-tutor", "pm", "qa", "research-analyst",
    "security",
]


def backup(path):
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = f"{path}.bak.sync.{ts}"
    shutil.copy2(path, dst)
    return dst


def deep_merge(base, override):
    """Return a new dict: override keys win, but dicts are merged recursively."""
    if not isinstance(base, dict) or not isinstance(override, dict):
        return override
    out = dict(base)
    for key, val in override.items():
        if key in out and isinstance(out[key], dict) and isinstance(val, dict):
            out[key] = deep_merge(out[key], val)
        else:
            out[key] = val
    return out


def yaml_load(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def yaml_dump(data):
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=4096, default_flow_style=False)


def cfg_identity(cfg):
    model = cfg.get("model", {}) or {}
    return (model.get("provider"), model.get("default"))


def _active_keys(lines):
    return sum(
        1 for ln in lines
        if ln.strip() and not ln.strip().startswith("#") and "=" in ln
    )


def sync_configs():
    print("== config.yaml ==")
    root = yaml_load(ROOT_CFG)
    root_provider, _ = cfg_identity(root)
    for prof_name in PROFILES:
        fpath = os.path.join(HERMES, "profiles", prof_name, "config.yaml")
        if not os.path.exists(fpath):
            print(f"  skip {prof_name}: no config.yaml")
            continue
        prof = yaml_load(fpath)
        prof_provider, prof_default = cfg_identity(prof)
        merged = deep_merge(prof, root)  # root wins except where restored below
        merged.setdefault("model", {})
        if prof_provider is not None:
            merged["model"]["provider"] = prof_provider
        if prof_default is not None:
            merged["model"]["default"] = prof_default
        new_text = yaml_dump(merged)
        with open(fpath, encoding="utf-8") as fh:
            old_text = fh.read()
        if new_text.strip() == old_text.strip():
            print(f"  {prof_name}: already in sync (provider={prof_provider})")
            continue
        backup(fpath)
        with open(fpath, "w", encoding="utf-8") as fh:
            fh.write(new_text)
        print(f"  {prof_name}: merged (root provider={root_provider} -> kept profile provider={prof_provider})")


def sync_env(force=False):
    print("== .env ==")
    with open(ROOT_ENV, encoding="utf-8") as fh:
        root_lines = fh.read().splitlines()
    root_active = _active_keys(root_lines)
    for prof_name in PROFILES:
        fpath = os.path.join(HERMES, "profiles", prof_name, ".env")
        if not os.path.exists(fpath):
            os.makedirs(os.path.dirname(fpath), exist_ok=True)
            shutil.copy2(ROOT_ENV, fpath)
            print(f"  {prof_name}: created .env from root ({root_active} keys)")
            continue
        with open(fpath, encoding="utf-8") as fh:
            existing = fh.read().splitlines()
        active = _active_keys(existing)
        if active == 0 or force:
            action = "placeholder" if active == 0 else "--force"
            print(f"  {prof_name}: {action} .env ({active} keys) -> copy root ({root_active} keys)")
            backup(fpath)
            shutil.copy2(ROOT_ENV, fpath)
        else:
            print(f"  {prof_name}: keeps own .env ({active} keys); skipped")


def sync_auth(force=False):
    print("== auth.json ==")
    if not os.path.exists(ROOT_AUTH):
        print("  root auth.json missing; skip")
        return
    for prof_name in PROFILES:
        fpath = os.path.join(HERMES, "profiles", prof_name, "auth.json")
        if not os.path.exists(fpath) or force:
            existed = os.path.exists(fpath)
            if existed:
                backup(fpath)
            shutil.copy2(ROOT_AUTH, fpath)
            print(f"  {prof_name}: auth.json {'refreshed' if existed else 'created'} from root")
        else:
            print(f"  {prof_name}: keeps own auth.json; skipped")


def main():
    force = "--force" in sys.argv
    sync_configs()
    sync_env(force)
    sync_auth(force)
    print("DONE. Run `hermes config check` per profile to validate.")


if __name__ == "__main__":
    raise SystemExit(main())
