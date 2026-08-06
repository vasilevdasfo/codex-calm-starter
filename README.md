# Codex Calm Starter

English · [Русский](README.ru.md)

A minimal, privacy-first workspace for a calm first experience with Codex.
It contains no personal profile, chat history, credentials, accounts, or
private project data.

**[Download Codex Calm Starter v0.1.0 (ZIP)](https://github.com/vasilevdasfo/codex-calm-starter/releases/download/v0.1.0/codex-calm-starter-v0.1.0.zip)**

## Quick start

1. Download the official ChatGPT desktop app with Codex:
   <https://chatgpt.com/download/>
2. Sign in with your own OpenAI account.
3. On GitHub, select **Code → Download ZIP**, then extract the archive.
4. Create your private local profile:

   - No terminal: duplicate `ABOUT_ME.template.md` and rename the copy to
     `ABOUT_ME.md`.
   - macOS/Linux: `cp ABOUT_ME.template.md ABOUT_ME.md`
   - Windows PowerShell: `Copy-Item ABOUT_ME.template.md ABOUT_ME.md`

5. Open the extracted folder as a local project in Codex.
6. Send this first prompt:

   `Read AGENTS.md and ABOUT_ME.md. Do not send anything or change anything outside this folder. Help me choose one small task for today.`

## What is included

- `AGENTS.md` — calm working rules and exact confirmation before external actions.
- `ABOUT_ME.template.md` — an optional preferences and work-rhythm questionnaire.
- `.agents/skills/` — three project skills Codex discovers in this repository.
- `PRIVACY.md` — boundaries for personal context.
- `scripts/validate_starter.py` — a local structure and secret-pattern check.

## Privacy rule

The filled `ABOUT_ME.md` is ignored by Git. Do not rename it or publish the
completed file. Do not add passwords, login codes, identity documents, banking
details, private keys, or another person's private messages.

## Optional validation

If Python 3 is already installed, run:

`python3 scripts/validate_starter.py`

Expected output: `PASS: starter kit is complete and public-safe`.

## Why repository skills

Codex officially discovers repository-specific skills in `.agents/skills` and
repository instructions in `AGENTS.md`. That means no global configuration or
home-directory copying is required: download, create the private profile, and
open the folder.

Official references:

- [Download ChatGPT with Codex](https://chatgpt.com/download/)
- [Codex customization and skills](https://learn.chatgpt.com/docs/customization/overview#skills)

## License

MIT. Use, adapt, and redistribute with the license included.
