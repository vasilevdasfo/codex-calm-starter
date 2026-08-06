#!/usr/bin/env python3
"""Validate the Starter structure and public-safe defaults."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "onboarding-context",
    "privacy-permissions",
    "problem-os-lite",
    "numbered-navigation",
    "website-helper",
    "email-helper",
    "idea-helper",
    "support-checkin",
}
CORE = {
    "onboarding-context",
    "privacy-permissions",
    "problem-os-lite",
    "numbered-navigation",
}
PRIVATE_LOCAL = {
    "ABOUT_ME.md",
    "MY_PROGRESS.md",
    "CLIENT_SYNC.json",
    ".starter_install_id",
    "PREFLIGHT_REPORT.txt",
    "PREFLIGHT_TECHNICAL.json",
}
REQUIRED = {
    "README.md",
    "README.ru.md",
    "INSTALL.md",
    "INSTALL.ru.md",
    "AGENTS.md",
    "ABOUT_ME.template.md",
    "MY_PROGRESS.template.md",
    "НАЧАТЬ_ЗДЕСЬ.md",
    "START_HERE.md",
    "PRIVACY.md",
    "SPEC_v0.2.md",
    "ACCEPTANCE_v0.2.md",
    "SITE_TRUST_BLOCK.md",
    "CREDITS.template.md",
    ".gitignore",
    ".agents/skills/onboarding-context/scripts/preflight.py",
    ".agents/skills/support-checkin/scripts/build_preview.py",
    "scripts/smoke_test.py",
    "scripts/build_release.py",
}
TEXT_SUFFIXES = {".md", ".py", ".txt", ".toml", ".json", ".yml", ".yaml"}
SECRET_PATTERNS = {
    "private_key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "openai_key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "github_token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "generic_password": re.compile(
        r"(?i)\b(password|passwd|secret)\s*[:=]\s*[\"'][^\"']{8,}[\"']"
    ),
}
NETWORK_MARKERS = (
    "import requests",
    "from requests",
    "urllib.request",
    "http.client",
    "import socket",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


for relative in sorted(REQUIRED):
    if not (ROOT / relative).is_file():
        fail(f"missing required file: {relative}")

skill_paths = list((ROOT / ".agents" / "skills").glob("*/SKILL.md"))
found_skills = {path.parent.name for path in skill_paths}
if found_skills != SKILLS:
    fail(f"skill set mismatch: expected {sorted(SKILLS)}, found {sorted(found_skills)}")
if not CORE.issubset(found_skills):
    fail("required core skills are incomplete")

for path in skill_paths:
    text = path.read_text(encoding="utf-8", errors="replace")
    if "[TODO" in text or "TODO:" in text:
        fail(f"unfinished skill template: {path.relative_to(ROOT)}")
    if not re.search(r"^name:\s*[a-z0-9-]+\s*$", text, re.MULTILINE):
        fail(f"invalid skill name metadata: {path.relative_to(ROOT)}")
    if not re.search(r"^description:\s*\S.+$", text, re.MULTILINE):
        fail(f"missing skill description: {path.relative_to(ROOT)}")

gitignore = {
    line.strip()
    for line in (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.lstrip().startswith("#")
}
missing_ignores = PRIVATE_LOCAL - gitignore
if missing_ignores:
    fail(f"private local files are not ignored: {sorted(missing_ignores)}")

for private_name in PRIVATE_LOCAL:
    if (ROOT / private_name).exists():
        print(f"NOTE: local private file exists and must remain untracked: {private_name}")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.suffix not in TEXT_SUFFIXES:
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    for label, pattern in SECRET_PATTERNS.items():
        if pattern.search(text):
            fail(f"possible {label} in {path.relative_to(ROOT)}")

for relative in (
    ".agents/skills/onboarding-context/scripts/preflight.py",
    ".agents/skills/support-checkin/scripts/build_preview.py",
):
    text = (ROOT / relative).read_text(encoding="utf-8")
    if any(marker in text for marker in NETWORK_MARKERS):
        fail(f"network-capable code is forbidden in local helper: {relative}")

onboarding_text = (
    ROOT / ".agents/skills/onboarding-context/SKILL.md"
).read_text(encoding="utf-8")
if "~/.codex/skills" not in onboarding_text or "Do not search" not in onboarding_text:
    fail("onboarding must forbid dependency on a global skill copy")

print(
    "PASS: Starter has 4 core skills, 3 optional modules, "
    "1 opt-in support skill, and public-safe defaults"
)
sys.exit(0)
