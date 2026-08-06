#!/usr/bin/env python3
"""Build a local support preview. This script performs no network operations."""

from __future__ import annotations

import json
import platform
import uuid
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELEASE = json.loads(
    (ROOT / "CLIENT_RELEASE_MANIFEST.json").read_text(encoding="utf-8")
)
INSTALL_ID_PATH = ROOT / ".starter_install_id"
OUTPUT_PATH = ROOT / "CLIENT_SYNC.json"


def installation_id() -> str:
    if INSTALL_ID_PATH.is_file():
        value = INSTALL_ID_PATH.read_text(encoding="utf-8").strip()
        if value:
            return value
    value = str(uuid.uuid4())
    INSTALL_ID_PATH.write_text(value + "\n", encoding="utf-8")
    return value


def main() -> int:
    profile_exists = (ROOT / "ABOUT_ME.md").is_file()
    preflight_exists = (ROOT / "PREFLIGHT_TECHNICAL.json").is_file()
    first_result_exists = any(
        path.exists()
        for path in (
            ROOT / "FIRST_RESULT.md",
            ROOT / "my-first-site" / "index.html",
            ROOT / "my-first-email.md",
        )
    )
    if first_result_exists:
        level = "L3"
    elif profile_exists and preflight_exists:
        level = "L2"
    elif preflight_exists:
        level = "L1"
    else:
        level = "L0"

    preview = {
        "mode": "PREVIEW_ONLY",
        "destination": "UNCONFIGURED",
        "consent_to_send": False,
        "installation_id": installation_id(),
        "starter_version": RELEASE["version"],
        "language": "unknown",
        "operating_system": platform.system() or "unknown",
        "onboarding_level": level,
        "completed_checks": {
            "preflight_created": preflight_exists,
            "local_profile_exists": profile_exists,
            "first_visible_result_exists": first_result_exists,
        },
        "help_category": None,
        "contact": None,
        "preview_created_at": datetime.now(timezone.utc).isoformat(),
        "excluded": [
            "chat_history",
            "prompts",
            "file_contents",
            "passwords",
            "tokens",
            "credentials",
        ],
    }
    OUTPUT_PATH.write_text(
        json.dumps(preview, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Preview saved locally: {OUTPUT_PATH.name}")
    print("Nothing was sent. Destination is UNCONFIGURED.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
