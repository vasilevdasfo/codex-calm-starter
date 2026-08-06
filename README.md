# Codex Calm Starter

English · [Русский](README.ru.md)

A calm Codex start for a person with no technical background. The starter
contains no other person's chats, accounts, memory, keys, or filled profile.

**[Download the current public release](https://github.com/vasilevdasfo/codex-calm-starter/releases/latest)**

## Simplest start

- Install the official ChatGPT desktop app with Codex:
  <https://chatgpt.com/download/>
- Extract the Starter and open the entire folder in Codex.
- Type: `START`.

Detailed instructions: `START_HERE.md`.

## What happens

- a plain-language local setup check;
- no more than five short optional questions;
- one useful task and one visible result;
- clear numbered choices for what to do next.

## Three layers

- Required core: onboarding, privacy, the complete Problem Solving Loop, and
  mandatory numbered navigation.
- On-demand work modules: website, email, and ideas.
- Optional support: a local preview of progress level and requested help.

The person does not need to select or install skills manually. Codex discovers
them from `.agents/skills` after the folder is opened.

## Privacy

Local `ABOUT_ME.md`, `MY_PROGRESS.md`, reports, and first results are ignored by
Git. Nothing is sent automatically. Account connection, email sending, and
site publishing each require separate confirmation.

The Starter includes no bridge, server, remote control, Obsidian/VS Code sync,
telemetry, or background status reporting.

## Trust and verification

- [Source on GitHub](https://github.com/vasilevdasfo/codex-calm-starter)
- [Public releases](https://github.com/vasilevdasfo/codex-calm-starter/releases)
- Every new ZIP receives a SHA-256 checksum.
- Contributors are named only with a verified role and consent.

## Support validation

If Python 3 is available:

`python3 scripts/validate_starter.py`

The expected result starts with `PASS`.
