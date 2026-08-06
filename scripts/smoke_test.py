#!/usr/bin/env python3
"""Exercise the local-first Starter pipeline in a fresh temporary copy."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(*args: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=cwd,
        text=True,
        capture_output=True,
        check=True,
    )


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="codex-calm-smoke-") as tmp:
        candidate = Path(tmp) / "starter"
        shutil.copytree(
            ROOT,
            candidate,
            ignore=shutil.ignore_patterns(
                ".git",
                "ABOUT_ME.md",
                "MY_PROGRESS.md",
                "CLIENT_SYNC.json",
                ".starter_install_id",
                "PREFLIGHT_REPORT.txt",
                "PREFLIGHT_TECHNICAL.json",
                "FIRST_RESULT.md",
                "my-first-site",
                "my-first-email.md",
                "__pycache__",
            ),
        )

        run(sys.executable, "scripts/validate_starter.py", cwd=candidate)
        run(
            sys.executable,
            ".agents/skills/onboarding-context/scripts/preflight.py",
            cwd=candidate,
        )
        technical = json.loads(
            (candidate / "PREFLIGHT_TECHNICAL.json").read_text(encoding="utf-8")
        )
        if technical["overall"] != "PASS":
            fail("fresh preflight did not pass")
        if not technical["checks"]["core_skills_found"]:
            fail("core skills were not discovered")
        if technical["checks"]["git_required_for_client"]:
            fail("Git was incorrectly required for the client")

        shutil.copy(candidate / "ABOUT_ME.template.md", candidate / "ABOUT_ME.md")
        shutil.copy(
            candidate / "MY_PROGRESS.template.md",
            candidate / "MY_PROGRESS.md",
        )
        (candidate / "FIRST_RESULT.md").write_text(
            "# First visible result\n\nLocal smoke-test artifact.\n",
            encoding="utf-8",
        )
        private_before = {
            name: digest(candidate / name)
            for name in ("ABOUT_ME.md", "MY_PROGRESS.md")
        }

        run(
            sys.executable,
            ".agents/skills/support-checkin/scripts/build_preview.py",
            cwd=candidate,
        )
        preview = json.loads(
            (candidate / "CLIENT_SYNC.json").read_text(encoding="utf-8")
        )
        if preview["mode"] != "PREVIEW_ONLY":
            fail("support report is not preview-only")
        if preview["destination"] != "UNCONFIGURED":
            fail("support destination must remain unconfigured")
        if preview["consent_to_send"] is not False:
            fail("support preview must not contain send consent")
        if preview["onboarding_level"] != "L3":
            fail("first visible result did not produce local L3 evidence")

        run(
            sys.executable,
            ".agents/skills/onboarding-context/scripts/preflight.py",
            cwd=candidate,
        )
        private_after = {
            name: digest(candidate / name)
            for name in ("ABOUT_ME.md", "MY_PROGRESS.md")
        }
        if private_before != private_after:
            fail("repeat preflight changed private local context")

        private_outputs = {
            "ABOUT_ME.md",
            "MY_PROGRESS.md",
            "CLIENT_SYNC.json",
            ".starter_install_id",
            "PREFLIGHT_REPORT.txt",
            "PREFLIGHT_TECHNICAL.json",
        }
        ignored = {
            line.strip()
            for line in (candidate / ".gitignore").read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        }
        if not private_outputs.issubset(ignored):
            fail("one or more local private artifacts are not ignored")

    print(
        "PASS: fresh copy, preflight, core discovery, first-result evidence, "
        "restart-safe local context, and preview-only check-in"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
