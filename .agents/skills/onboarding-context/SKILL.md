---
name: onboarding-context
description: Start a beginner's first Codex session when they type "НАЧАТЬ", "START", "первый запуск", or ask to set up the Starter. Run a plain-language local preflight, ask at most five optional questions one at a time, save only approved local context, and guide one first useful result.
---

# Onboarding context

## First-run workflow

1. Respond in the person's language.
2. Use this repository-local skill path. Do not search for or require a copy
   under `~/.codex/skills` or `~/.agents/skills`.
3. Run `python3 .agents/skills/onboarding-context/scripts/preflight.py` when
   Python is available. If it is unavailable, perform the same read-only checks
   directly and explain one recovery action per failed check.
4. Show only the plain-language summary. Keep technical details in
   `PREFLIGHT_TECHNICAL.json`.
5. Ask no more than five questions, one at a time:
   - preferred name;
   - language;
   - one goal for today;
   - experience level: first time / some experience / confident;
   - permission to save these answers locally.
6. Skip any question the person does not want to answer.
7. With permission, create or update `ABOUT_ME.md`. Never require contact
   details, biography, medical, financial, family, or third-party information.
8. Offer one numbered choice based on today's goal. Do not ask the person to
   select a skill.
9. Complete one small local result, show where it is, and give one simple check.
10. Update `MY_PROGRESS.md` locally only after a visible result exists. Keep
    `Experience` separate from `Current onboarding level`. Set the evidence-based
    level explicitly; a verified first artifact is `L3`.

## Beginner rules

- Use everyday language and short messages.
- Give one action at a time.
- Explain unfamiliar words immediately.
- Prefer a reversible local preview.
- Never treat missing Git, terminal knowledge, or coding experience as failure.
- If something fails, give exactly one recovery action before offering alternatives.
