---
name: support-checkin
description: Prepare a local progress level or optional support request when a person asks "мой уровень", "что уже настроено", "нужна помощь", "отчёт", "progress", "check-in", or wants to share setup status. Always preview exact fields and send nothing without explicit consent.
---

# Support check-in

1. Read only local setup evidence needed for the level:
   - project opened;
   - core skills detected;
   - local profile started;
   - first visible result exists;
   - independent verified workflow completed.
2. Assign `L0` through `L4` from evidence, not self-worth or technical identity.
   Keep the person's self-described experience separate from this onboarding level.
3. Run `python3 .agents/skills/support-checkin/scripts/build_preview.py` to create
   `CLIENT_SYNC.json`.
4. Show the exact preview, destination, purpose, and fields.
5. If the destination is `UNCONFIGURED`, stop with one recovery action.
6. Even with a configured destination, send nothing until the person explicitly
   confirms the exact payload and destination.
7. Never include chats, prompts, file contents, secrets, credentials, or another
   person's data.
