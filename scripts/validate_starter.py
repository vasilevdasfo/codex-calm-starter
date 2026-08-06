#!/usr/bin/env python3
"""Validate the public starter structure without reading outside the repo."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "README.ru.md",
    "INSTALL.md",
    "INSTALL.ru.md",
    "AGENTS.md",
    "ABOUT_ME.template.md",
    "PRIVACY.md",
    ".gitignore",
    ".agents/skills/calm-workflow/SKILL.md",
    ".agents/skills/context-interview/SKILL.md",
    ".agents/skills/privacy-gate/SKILL.md",
)
TEXT_SUFFIXES = {".md", ".py", ".txt", ".toml", ".json", ".yml", ".yaml"}
SECRET_PATTERNS = {
    "private_key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "openai_key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "github_token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "generic_password": re.compile(
        r"(?i)\b(password|passwd|secret)\s*[:=]\s*[\"'][^\"']{8,}[\"']"
    ),
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


for relative in REQUIRED:
    if not (ROOT / relative).is_file():
        fail(f"missing required file: {relative}")

gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
if "ABOUT_ME.md" not in {line.strip() for line in gitignore.splitlines()}:
    fail("ABOUT_ME.md is not ignored")

if (ROOT / "ABOUT_ME.md").exists():
    print("NOTE: local ABOUT_ME.md exists and must remain untracked")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.suffix not in TEXT_SUFFIXES:
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    for label, pattern in SECRET_PATTERNS.items():
        if pattern.search(text):
            fail(f"possible {label} in {path.relative_to(ROOT)}")

print("PASS: starter kit is complete and public-safe")
sys.exit(0)
