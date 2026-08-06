# Installation

## What to download

- Official ChatGPT desktop app with Codex:
  <https://chatgpt.com/download/>
- This repository: select **Code → Download ZIP**.
- Nothing else is required for the starter workspace.

Use your own OpenAI account. Do not share a password, sign-in code, API key, or
an existing `.codex` directory with another person.

## Set up

1. Extract the ZIP to a local folder.
2. Duplicate `ABOUT_ME.template.md` in Finder or Explorer and rename the copy
   to `ABOUT_ME.md`.
3. Or create the private profile from a terminal:
   `cp ABOUT_ME.template.md ABOUT_ME.md`
4. On Windows PowerShell:
   `Copy-Item ABOUT_ME.template.md ABOUT_ME.md`
5. Open the folder as a local Codex project.
6. Confirm Codex can see the root `AGENTS.md`.
7. Send:

   `Read AGENTS.md and ABOUT_ME.md. Do not send anything or change anything outside this folder. Suggest one small next step.`

## Why the skills are already available

The project skills live in `.agents/skills`, the official repository-local
location for Codex skills. There is no need to copy them into a home directory
or overwrite global settings.

## Optional safety check

If Python 3 is already installed, run:

`python3 scripts/validate_starter.py`

Then ask Codex to list the project skills and explain when each one applies.
