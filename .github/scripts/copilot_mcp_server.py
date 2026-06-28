"""Copilot MCP Server — run prompts through GitHub Copilot CLI.

Provides a single tool `run_prompt` that sends a prompt to Copilot
and returns the response. Uses `copilot -p` for non-interactive execution.

On Windows, `copilot` is a bash script so we must run it through bash.
--allow-all is needed to prevent TTY permission prompt hangs.
"""
import subprocess
import os
from fastmcp import FastMCP

mcp = FastMCP("copilot-mcp")

BASH = r"C:\Program Files\Git\usr\bin\bash.exe"
COPILOT_CANDIDATES = [
    None,  # try PATH first
    r"C:\Users\Alexa\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilotCli\copilot",
]


def _find_copilot() -> str:
    """Locate the copilot bash script (not .BAT) on PATH."""
    copilot = __import__("shutil").which("copilot")
    if copilot:
        # which() may return copilot.BAT on Windows — we want the shell script
        dir_name = os.path.dirname(copilot)
        base = os.path.join(dir_name, "copilot")
        if os.path.isfile(base):
            return base
        return copilot
    candidates = [
        r"C:\Users\Alexa\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilotCli\copilot",
    ]
    for c in candidates:
        if os.path.isfile(c):
            return c
    raise FileNotFoundError(
        "copilot CLI not found. Install with: gh extension install github/gh-copilot"
    )


@mcp.tool()
def run_prompt(prompt: str) -> str:
    """Run a coding prompt through GitHub Copilot CLI and return the response.

    Use this for code generation, explanation, refactoring, and general
    programming questions. The prompt is sent as a non-interactive request
    and returns the full Copilot output.

    Copilot can also create/edit files when given file-related tasks.

    Args:
        prompt: The prompt/question to send to Copilot.
    """
    copilot_bin = _find_copilot()
    # Convert Windows path to MSYS path for bash
    if ":" in copilot_bin and copilot_bin[1] == ":":
        # C:\... → /c/...
        drive = copilot_bin[0].lower()
        rest = copilot_bin[2:].replace("\\", "/")
        copilot_bin = f"/{drive}{rest}"
    try:
        # --allow-all prevents TTY permission prompt hangs in subprocess mode
        bash_cmd = (
            f"{copilot_bin} -p {_q(prompt)} --allow-all"
        )
        result = subprocess.run(
            [BASH, "-c", bash_cmd],
            capture_output=True,
            text=True,
            timeout=120,
        )
        output = (result.stdout or "").strip()
        if not output and result.returncode != 0:
            stderr = (result.stderr or "")[:500].strip()
            return f"Error (exit {result.returncode}): {stderr}" if stderr else (
                f"Copilot CLI exited with code {result.returncode}"
            )
        return output[:8000] if output else (
            f"(empty output — exit {result.returncode})"
        )
    except subprocess.TimeoutExpired:
        return "Error: request timed out after 120 seconds"
    except FileNotFoundError as e:
        return f"Error: Copilot CLI not found — {e}"
    except Exception as e:
        return f"Error: {e}"


def _q(s: str) -> str:
    """Shell-quote a string for bash -c."""
    return "'" + s.replace("'", "'\\''") + "'"


if __name__ == "__main__":
    mcp.run(show_banner=False)
