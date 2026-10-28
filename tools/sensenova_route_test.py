#!/usr/bin/env python3
"""Check where SenseNova-Skills sends API keys, using dummy keys.

Runs the image, text and vision commands of sn-image-base's runner and
sn-da-image-caption in four setups, reports the host each request went to and
compares it with the results in SECURITY-SCAN.md, recorded at upstream commit
0ee34f3. A FAIL means upstream behaviour changed and the write-up needs
revisiting.

Every command runs with dummy keys in a clean environment, so no real key can
be picked up. Requests are pointed at a local recorder that logs them and
answers 403:

- Text, vision and sn-da-image-caption honour HTTPS_PROXY, so they reach the
  recorder as a proxy and never leave the machine.
- Image generation ignores HTTPS_PROXY, so in setups A to C its request goes to
  the real host (SenseNova in A, Google in B and C) carrying the dummy Gemini
  key, and the host is read from the error it returns. Setup D points the
  image fallback at the recorder, so `--setups D` runs entirely on this machine.

This runs SenseNova-Skills code, so point --skills at a checkout you have read.
See "How this was checked" in SECURITY-SCAN.md for the setup commands.
"""

from __future__ import annotations

import argparse
import base64
import re
import socketserver
import subprocess
import sys
import tempfile
import threading
from pathlib import Path
from urllib.parse import urlsplit

REVIEWED_COMMIT = "0ee34f37b969011d527eba348d1bec220fd1a7dd"

SENSENOVA = "token.sensenova.cn"
GOOGLE = "generativelanguage.googleapis.com"
ANTHROPIC = "api.anthropic.com"
TRIPWIRE_HOST = "sn-base-url-not-set.invalid"
RECORDER = "the local recorder"

AUTH_HEADERS = ("authorization", "x-api-key", "x-goog-api-key")
PIXEL_PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
)

# The safe configuration from SECURITY-SCAN.md, in parts so a setup can leave one out.
TRIPWIRE = {"SN_BASE_URL": f"https://{TRIPWIRE_HOST}/v1"}
IMAGE_ON_GEMINI = {
    "SN_IMAGE_GEN_MODEL_TYPE": "nano-banana",
    "SN_IMAGE_GEN_MODEL": "gemini-3.1-flash-image-preview",
    "SN_IMAGE_GEN_API_KEY": "DUMMY-not-a-real-gemini-key",
}
GEMINI_BASE_URL = {"SN_IMAGE_GEN_BASE_URL": f"https://{GOOGLE}"}
CHAT_ON_CLAUDE = {
    "SN_CHAT_TYPE": "anthropic-messages",
    "SN_CHAT_MODEL": "claude-sonnet-5-5",
    "SN_CHAT_API_KEY": "DUMMY-not-a-real-anthropic-key",
}
CLAUDE_BASE_URL = {"SN_CHAT_BASE_URL": f"https://{ANTHROPIC}/v1"}

REQUEST_URL = re.compile(r"\b(?:POST|GET|PUT) '?(https?://[^\s'\"]+)")
ANY_URL = re.compile(r"(https?://[^\s'\"]+)")


class Recorder(socketserver.ThreadingTCPServer):
    """Records where each request was headed and refuses it."""

    allow_reuse_address = True
    daemon_threads = True

    def __init__(self) -> None:
        super().__init__(("127.0.0.1", 0), RecorderHandler)
        self.url = f"http://127.0.0.1:{self.server_address[1]}"
        self._hits: list[tuple[str, str, tuple[str, ...]]] = []
        self._lock = threading.Lock()

    def record(self, host: str, route: str, auth: tuple[str, ...]) -> None:
        with self._lock:
            self._hits.append((host, route, auth))

    def take_hits(self) -> list[tuple[str, str, tuple[str, ...]]]:
        with self._lock:
            hits, self._hits = self._hits, []
        return hits


class RecorderHandler(socketserver.StreamRequestHandler):
    server: Recorder

    def handle(self) -> None:
        method, target = (
            [*self.rfile.readline(65536).decode("latin-1").split(), "?", "?"]
        )[:2]
        header_names = []
        while (line := self.rfile.readline(65536)) not in (b"", b"\r\n", b"\n"):
            header_names.append(line.decode("latin-1").split(":", 1)[0].strip().lower())
        auth = tuple(sorted(h for h in header_names if h in AUTH_HEADERS))
        if method == "CONNECT":
            self.server.record(
                urlsplit(f"//{target}").hostname or target, "via proxy", auth
            )
        elif target.startswith("http"):
            self.server.record(urlsplit(target).hostname or target, "via proxy", auth)
        else:
            self.server.record(RECORDER, f"direct, {target.split('?')[0]}", auth)
        self.wfile.write(
            b"HTTP/1.1 403 Forbidden\r\nContent-Length: 0\r\nConnection: close\r\n\r\n"
        )


def host_from_output(output: str) -> str | None:
    match = REQUEST_URL.search(output) or ANY_URL.search(output)
    return urlsplit(match.group(1)).hostname if match else None


def checkout_commit(skills: Path) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(skills), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip() or None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check where SenseNova-Skills sends API keys, using dummy keys."
    )
    parser.add_argument(
        "--skills",
        type=Path,
        required=True,
        help="the skills/ folder of a SenseNova-Skills checkout",
    )
    parser.add_argument(
        "--python",
        type=Path,
        required=True,
        help="a Python with httpx, pillow, python-dotenv, typing_extensions and openai installed",
    )
    parser.add_argument(
        "--setups",
        default="ABCD",
        help="setups to run, e.g. D for the fully local one (default: ABCD)",
    )
    args = parser.parse_args()

    runner = args.skills / "sn-image-base" / "scripts" / "sn_agent_runner.py"
    caption = args.skills / "sn-da-image-caption" / "scripts" / "caption.py"
    for path in (runner, caption, args.python):
        if not path.exists():
            parser.error(f"not found: {path}")

    commit = checkout_commit(args.skills)
    print(f"SenseNova-Skills checkout: {commit or 'unknown commit'}")
    if commit != REVIEWED_COMMIT:
        print(
            f"Expected results were recorded at {REVIEWED_COMMIT[:7]}; a FAIL may just mean upstream changed."
        )

    recorder = Recorder()
    threading.Thread(target=recorder.serve_forever, daemon=True).start()

    setups = {
        "A": (
            "Keys set, no base URLs (the leak)",
            {**IMAGE_ON_GEMINI, **CHAT_ON_CLAUDE},
            {
                "image": SENSENOVA,
                "text": SENSENOVA,
                "vision": SENSENOVA,
                "caption": SENSENOVA,
            },
        ),
        "B": (
            "Safe configuration",
            {
                **TRIPWIRE,
                **IMAGE_ON_GEMINI,
                **GEMINI_BASE_URL,
                **CHAT_ON_CLAUDE,
                **CLAUDE_BASE_URL,
            },
            {
                "image": GOOGLE,
                "text": ANTHROPIC,
                "vision": ANTHROPIC,
                "caption": ANTHROPIC,
            },
        ),
        "C": (
            "Safe configuration without SN_CHAT_BASE_URL",
            {**TRIPWIRE, **IMAGE_ON_GEMINI, **GEMINI_BASE_URL, **CHAT_ON_CLAUDE},
            {
                "image": GOOGLE,
                "text": TRIPWIRE_HOST,
                "vision": TRIPWIRE_HOST,
                "caption": TRIPWIRE_HOST,
            },
        ),
        "D": (
            "Safe configuration without SN_IMAGE_GEN_BASE_URL, tripwire set to the local recorder",
            {
                "SN_BASE_URL": f"{recorder.url}/tripwire",
                **IMAGE_ON_GEMINI,
                **CHAT_ON_CLAUDE,
                **CLAUDE_BASE_URL,
            },
            {
                "image": RECORDER,
                "text": ANTHROPIC,
                "vision": ANTHROPIC,
                "caption": ANTHROPIC,
            },
        ),
    }

    passed = failed = 0
    with tempfile.TemporaryDirectory(prefix="sn-route-test-") as work_dir:
        home = Path(work_dir)
        image = home / "pixel.png"
        image.write_bytes(PIXEL_PNG)
        commands = {
            "image": (
                "image   sn-image-generate",
                [
                    runner,
                    "sn-image-generate",
                    "--prompt",
                    "a red square",
                    "--timeout",
                    "10",
                    "-o",
                    "json",
                ],
            ),
            "text": (
                "text    sn-text-optimize",
                [runner, "sn-text-optimize", "--user-prompt", "hello", "-o", "json"],
            ),
            "vision": (
                "vision  sn-image-recognize",
                [
                    runner,
                    "sn-image-recognize",
                    "--user-prompt",
                    "describe",
                    "--images",
                    image,
                    "-o",
                    "json",
                ],
            ),
            "caption": (
                "vision  sn-da-image-caption",
                [caption, image, "--prompt", "describe", "--json", "--no-cache"],
            ),
        }
        # Nothing from the caller's environment is passed on, so real keys cannot leak into a run.
        base_env = {
            "PATH": f"{args.python.parent}:/usr/bin:/bin",
            "HOME": str(home),
            "LANG": "en_US.UTF-8",
            **dict.fromkeys(
                (
                    "HTTPS_PROXY",
                    "https_proxy",
                    "HTTP_PROXY",
                    "http_proxy",
                    "ALL_PROXY",
                    "all_proxy",
                ),
                recorder.url,
            ),
            "NO_PROXY": "",
            "no_proxy": "",
        }

        for letter, (title, setup_env, expected) in setups.items():
            if letter not in args.setups.upper():
                continue
            print(f"\n{letter}. {title}")
            for call, (label, argv) in commands.items():
                try:
                    result = subprocess.run(
                        [str(args.python), *map(str, argv)],
                        cwd=home,
                        env={**base_env, **setup_env},
                        capture_output=True,
                        text=True,
                        timeout=120,
                        check=False,
                    )
                    output = result.stderr + result.stdout
                except subprocess.TimeoutExpired:
                    output = ""
                hits = recorder.take_hits()
                if hits:
                    observed = {host for host, _, _ in hits}
                    seen = dict.fromkeys(
                        f"{host} ({route})"
                        + (f" carrying {', '.join(auth)}" if auth else "")
                        for host, route, auth in hits
                    )
                    where = ", ".join(seen)
                else:
                    host = host_from_output(output)
                    observed = {host} if host else set()
                    where = (
                        f"{host} (direct, HTTPS_PROXY ignored)"
                        if host
                        else "nothing observed"
                    )
                ok = observed == {expected[call]}
                passed += ok
                failed += not ok
                print(
                    f"  {'PASS' if ok else 'FAIL'}  {label:<28} {where}"
                    + ("" if ok else f"  (expected {expected[call]})")
                )
                if not ok and not hits and output.strip():
                    print(
                        f"        last output: {output.strip().splitlines()[-1][:200]}"
                    )

    recorder.shutdown()
    recorder.server_close()
    print(f"\n{passed} passed, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
