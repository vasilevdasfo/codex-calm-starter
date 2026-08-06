#!/usr/bin/env python3
"""Create beginner-friendly and technical local Starter preflight reports."""

from __future__ import annotations

import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
CORE = {
    "onboarding-context",
    "privacy-permissions",
    "problem-os-lite",
    "numbered-navigation",
}
OPTIONAL = {"website-helper", "email-helper", "idea-helper", "support-checkin"}


def skill_names() -> set[str]:
    skills_root = ROOT / ".agents" / "skills"
    return {
        path.parent.name
        for path in skills_root.glob("*/SKILL.md")
        if path.is_file()
    }


def main() -> int:
    found = skill_names()
    gitignore_text = (ROOT / ".gitignore").read_text(
        encoding="utf-8", errors="replace"
    )
    ignored = {
        line.strip()
        for line in gitignore_text.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }
    checks = {
        "starter_project_open": ROOT.is_dir(),
        "agents_rules_found": (ROOT / "AGENTS.md").is_file(),
        "core_skills_found": CORE.issubset(found),
        "optional_modules_found": OPTIONAL.issubset(found),
        "private_profile_ignored": {
            "ABOUT_ME.md",
            "MY_PROGRESS.md",
            "CLIENT_SYNC.json",
        }.issubset(ignored),
        "git_required_for_client": False,
    }
    codex_detected = bool(
        os.environ.get("CODEX_HOME")
        or os.environ.get("CODEX_SANDBOX")
        or os.environ.get("CODEX_THREAD_ID")
    )
    passed = all(
        value
        for key, value in checks.items()
        if key != "git_required_for_client"
    )
    recovery = []
    if not codex_detected:
        recovery.append("Откройте эту папку в Codex и напишите НАЧАТЬ.")
    if not checks["agents_rules_found"]:
        recovery.append("Скачайте Starter заново: файл AGENTS.md отсутствует.")
    if not checks["core_skills_found"]:
        recovery.append("Скачайте Starter заново: обязательные навыки неполные.")
    if not checks["private_profile_ignored"]:
        recovery.append("Не публикуйте локальные файлы профиля; обратитесь в поддержку.")

    technical = {
        "starter_version": "0.2.0-local",
        "root": str(ROOT),
        "codex_detected": codex_detected,
        "checks": checks,
        "skills": sorted(found),
        "core_expected": sorted(CORE),
        "optional_expected": sorted(OPTIONAL),
        "overall": "PASS" if passed else "FAIL",
        "recovery": recovery[:1],
    }
    (ROOT / "PREFLIGHT_TECHNICAL.json").write_text(
        json.dumps(technical, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    lines = [
        "ПРОВЕРКА STARTER",
        "",
        f"Codex запущен: {'ДА' if codex_detected else 'НУЖНА ПРОВЕРКА В ПРИЛОЖЕНИИ'}",
        f"Проект открыт: {'ДА' if checks['starter_project_open'] else 'НЕТ'}",
        f"Правила найдены: {'ДА' if checks['agents_rules_found'] else 'НЕТ'}",
        f"Обязательные навыки найдены: {'ДА' if checks['core_skills_found'] else 'НЕТ'}",
        f"Рабочие модули найдены: {'ДА' if checks['optional_modules_found'] else 'НЕТ'}",
        f"Личный профиль защищён от Git: {'ДА' if checks['private_profile_ignored'] else 'НЕТ'}",
        "Git для обычной работы клиента: НЕ НУЖЕН",
        "",
        f"Итог: {'ГОТОВО' if passed else 'НУЖНО ИСПРАВИТЬ'}",
    ]
    if recovery:
        lines.extend(["", f"Что сделать: {recovery[0]}"])
    (ROOT / "PREFLIGHT_REPORT.txt").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    print("\n".join(lines))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
