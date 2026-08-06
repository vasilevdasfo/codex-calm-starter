#!/usr/bin/env python3
"""Build a validated local release candidate without private local files."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
RELEASE_MANIFEST = json.loads(
    (ROOT / "CLIENT_RELEASE_MANIFEST.json").read_text(encoding="utf-8")
)
VERSION = RELEASE_MANIFEST["version"]
ARCHIVE = DIST / RELEASE_MANIFEST["archive_name"]
PREFIX = "codex-calm-starter/"


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def public_files() -> list[Path]:
    result = subprocess.run(
        ("git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"),
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    files = []
    for raw in result.stdout.split(b"\0"):
        if not raw:
            continue
        path = ROOT / raw.decode("utf-8")
        if path.is_file() and ".git" not in path.parts and "dist" not in path.parts:
            files.append(path)
    return sorted(files)


def main() -> int:
    run(sys.executable, "scripts/check_release_gate.py")
    run(sys.executable, "scripts/validate_starter.py")
    run(sys.executable, "scripts/smoke_test.py")
    DIST.mkdir(exist_ok=True)
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for path in public_files():
            bundle.write(path, PREFIX + path.relative_to(ROOT).as_posix())
    with tempfile.TemporaryDirectory(prefix="codex-calm-release-check-") as tmp:
        with zipfile.ZipFile(ARCHIVE) as bundle:
            bundle.extractall(tmp)
        extracted = Path(tmp) / PREFIX.rstrip("/")
        subprocess.run(
            (sys.executable, "scripts/validate_starter.py"),
            cwd=extracted,
            check=True,
        )
        subprocess.run(
            (sys.executable, "scripts/smoke_test.py"),
            cwd=extracted,
            check=True,
        )
    run(
        sys.executable,
        "scripts/check_release_gate.py",
        "--archive",
        str(ARCHIVE),
    )
    checksum = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
    checksum_path = ARCHIVE.with_suffix(".zip.sha256")
    checksum_path.write_text(f"{checksum}  {ARCHIVE.name}\n", encoding="utf-8")
    print(f"PASS: {ARCHIVE.name}")
    print(f"SHA256: {checksum}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
