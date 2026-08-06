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
            "scripts/support_preflight.py",
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

        agents_text = (candidate / "AGENTS.md").read_text(encoding="utf-8")
        loop_text = (
            candidate / ".agents/skills/problem-solving-loop/SKILL.md"
        ).read_text(encoding="utf-8")
        navigation_text = (
            candidate / ".agents/skills/numbered-navigation/SKILL.md"
        ).read_text(encoding="utf-8")
        if "problem-solving-loop" not in agents_text:
            fail("Problem Solving Loop is not routed from AGENTS.md")
        if "Verify" not in loop_text or "Continue" not in loop_text:
            fail("Problem Solving Loop is incomplete")
        if "After every non-trivial answer" not in navigation_text:
            fail("numbered navigation is not mandatory")
        if "Do not configure a bridge" not in agents_text:
            fail("no-bridge boundary is absent")

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
            "scripts/support_build_preview.py",
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
            "scripts/support_preflight.py",
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

        client_surfaces = (
            candidate / "AGENTS.md",
            candidate / ".agents/skills/onboarding-context/SKILL.md",
            candidate / ".agents/skills/support-checkin/SKILL.md",
            candidate / "START_HERE.md",
            candidate / "НАЧАТЬ_ЗДЕСЬ.md",
        )
        if any("python3 " in path.read_text(encoding="utf-8") for path in client_surfaces):
            fail("beginner path still invokes Python")

        release_gate = run(
            sys.executable,
            "scripts/check_release_gate.py",
            cwd=candidate,
        )
        if "PASS: one release manifest" not in release_gate.stdout:
            fail("release gate did not confirm the canonical manifest")

        send_attempt = subprocess.run(
            (
                sys.executable,
                "scripts/check_release_gate.py",
                "--for-client-send",
            ),
            cwd=candidate,
            text=True,
            capture_output=True,
        )
        if send_attempt.returncode == 0:
            fail("unpublished candidate was incorrectly allowed for client send")
        if "client distribution is blocked" not in send_attempt.stdout:
            fail("client-send failure did not explain the exact release gate")

        readme_ru = candidate / "README.ru.md"
        clean_readme = readme_ru.read_text(encoding="utf-8")
        readme_ru.write_text(
            clean_readme
            + "\nhttps://github.com/example/project/releases/tag/v0.1.0\n",
            encoding="utf-8",
        )
        stale_attempt = subprocess.run(
            (sys.executable, "scripts/check_release_gate.py"),
            cwd=candidate,
            text=True,
            capture_output=True,
        )
        if stale_attempt.returncode == 0:
            fail("stale v0.1.0 client link was not rejected")
        if "stale client version v0.1.0" not in stale_attempt.stdout:
            fail("stale-link failure did not identify the blocked version")
        readme_ru.write_text(clean_readme, encoding="utf-8")

        loop_path = candidate / ".agents/skills/problem-solving-loop/SKILL.md"
        loop_backup = loop_path.read_text(encoding="utf-8")
        loop_path.unlink()
        incomplete_attempt = subprocess.run(
            (sys.executable, "scripts/check_release_gate.py"),
            cwd=candidate,
            text=True,
            capture_output=True,
        )
        if incomplete_attempt.returncode == 0:
            fail("incomplete core skill set was not rejected")
        if "release skill set mismatch" not in incomplete_attempt.stdout:
            fail("incomplete-core failure did not identify the skill mismatch")
        loop_path.parent.mkdir(parents=True, exist_ok=True)
        loop_path.write_text(loop_backup, encoding="utf-8")

    print(
        "PASS: fresh copy, complete Problem Solving Loop, mandatory numbering, "
        "no bridge, no-Python client path, first-result evidence, restart-safe "
        "local context, preview-only check-in, and stale-release rejection"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
