#!/usr/bin/env python3
"""Fail closed when a client package, link, or skill set is stale."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path


CLIENT_DOCS = (
    "README.md",
    "README.ru.md",
    "INSTALL.md",
    "INSTALL.ru.md",
    "START_HERE.md",
    "НАЧАТЬ_ЗДЕСЬ.md",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def load_manifest(root: Path) -> dict:
    path = root / "CLIENT_RELEASE_MANIFEST.json"
    if not path.is_file():
        fail("CLIENT_RELEASE_MANIFEST.json is missing")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"release manifest is unreadable: {exc}")


def skill_names(root: Path) -> set[str]:
    return {
        path.parent.name
        for path in (root / ".agents" / "skills").glob("*/SKILL.md")
        if path.is_file()
    }


def check_source(root: Path, manifest: dict, for_client_send: bool) -> None:
    version = manifest.get("version")
    archive_name = manifest.get("archive_name")
    if not isinstance(version, str) or not version:
        fail("manifest version is missing")
    if archive_name != f"codex-calm-starter-v{version}.zip":
        fail("archive_name does not match manifest version")

    preflight = json.loads(
        (root / "PREFLIGHT_MANIFEST.json").read_text(encoding="utf-8")
    )
    if preflight.get("starter_version") != version:
        fail("PREFLIGHT_MANIFEST version differs from client release manifest")

    expected = set(
        manifest.get("required_core_skills", [])
        + manifest.get("required_work_modules", [])
        + manifest.get("required_support_skills", [])
    )
    found = skill_names(root)
    if found != expected:
        fail(
            "release skill set mismatch: "
            f"expected {sorted(expected)}, found {sorted(found)}"
        )

    blocked = tuple(manifest.get("blocked_client_versions", []))
    for relative in CLIENT_DOCS:
        path = root / relative
        if not path.is_file():
            fail(f"client instruction is missing: {relative}")
        text = path.read_text(encoding="utf-8", errors="replace")
        if "/releases/latest" in text:
            fail(f"floating GitHub latest link is forbidden: {relative}")
        for stale in blocked:
            if stale in text:
                fail(f"stale client version {stale} appears in {relative}")

    state = manifest.get("state")
    allowed = manifest.get("client_send_allowed")
    public_url = manifest.get("public_release_url")
    if state == "CANDIDATE_LOCAL_ONLY":
        if allowed is not False or public_url is not None:
            fail("local candidate must have send=false and public_release_url=null")
    elif state == "PUBLIC_VERIFIED":
        if allowed is not True:
            fail("public verified state must explicitly allow client send")
        if not isinstance(public_url, str) or version not in public_url:
            fail("public verified URL must contain the exact manifest version")
    else:
        fail(f"unknown release state: {state}")

    if for_client_send and not (
        state == "PUBLIC_VERIFIED" and allowed is True and public_url
    ):
        fail(
            "client distribution is blocked: exact public release and approval "
            "are not verified"
        )


def check_archive(archive: Path, manifest: dict) -> str:
    if archive.name != manifest["archive_name"]:
        fail("archive filename differs from release manifest")
    if not archive.is_file():
        fail(f"archive is missing: {archive}")
    prefix = "codex-calm-starter/"
    with zipfile.ZipFile(archive) as bundle:
        names = set(bundle.namelist())
        manifest_name = prefix + "CLIENT_RELEASE_MANIFEST.json"
        if manifest_name not in names:
            fail("release manifest is absent from archive")
        packed = json.loads(bundle.read(manifest_name).decode("utf-8"))
        if packed != manifest:
            fail("packed release manifest differs from source manifest")
        for skill in (
            manifest["required_core_skills"]
            + manifest["required_work_modules"]
            + manifest["required_support_skills"]
        ):
            expected = prefix + f".agents/skills/{skill}/SKILL.md"
            if expected not in names:
                fail(f"archive is missing skill: {skill}")
        bad = bundle.testzip()
        if bad:
            fail(f"archive integrity failed at: {bad}")
    return hashlib.sha256(archive.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="")
    parser.add_argument("--archive", default="")
    parser.add_argument("--for-client-send", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parents[1]
    manifest = load_manifest(root)
    check_source(root, manifest, args.for_client_send)
    if args.archive:
        checksum = check_archive(Path(args.archive).resolve(), manifest)
        print(f"ARCHIVE_SHA256: {checksum}")
    print(
        "PASS: one release manifest, exact skill set, no stale client links, "
        f"state={manifest['state']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
