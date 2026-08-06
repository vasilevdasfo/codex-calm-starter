# Codex Calm Starter v0.2 — product specification

## Outcome

A person with no technical background completes one route:

`official Codex -> open Starter -> type НАЧАТЬ -> answer short questions -> get one visible result`

The starter never needs another person's account, files, profile, memory, or
secrets.

## Target computer

- Owner: `UNKNOWN`
- Operating system: `UNKNOWN`
- Device model: `UNKNOWN`

Do not claim platform-specific support until that platform has been tested.
The package itself remains platform-neutral. OpenAI's official installer is
outside this package.

## Source of truth

- OpenAI's current Codex documentation for `AGENTS.md` and repository-local
  skills in `.agents/skills`.
- This repository and its release for client-facing rules, skills, templates,
  validators, and acceptance evidence.
- The client's own local `ABOUT_ME.md` and `MY_PROGRESS.md` for personal context.

## One visible path

1. Download the official ChatGPT desktop application with Codex.
2. Download and extract the Starter.
3. Open the extracted Starter folder in Codex.
4. Type `НАЧАТЬ` or `START`.
5. Answer at most five simple questions:
   - preferred name;
   - language;
   - today's goal;
   - current experience level;
   - permission to perform a local read-only check.
6. Choose one numbered task.
7. Receive a visible local result and one simple verification step.

Contact details and any status transmission are separate, optional actions.

## Three layers

### Layer 1 — required core

- `onboarding-context` — first run, short interview, and first result.
- `privacy-permissions` — local-first boundaries and exact approval gates.
- `problem-solving-loop` — outcome, facts, boundaries, safe action, verification,
  learning, and continuation for every non-trivial task.
- `numbered-navigation` — mandatory stable choices after every non-trivial result.

### Layer 2 — optional work modules

- `website-helper` — create and check a small local site; publish separately.
- `email-helper` — find or draft email; send separately.
- `idea-helper` — generate, filter, and choose ideas.

Load a module when the person's task matches it. Do not ask the beginner to
learn or select skill names.

### Layer 3 — opt-in support

- `support-checkin` — calculate a local onboarding level and preview a minimal
  support request. Perform zero network writes without exact consent.

## Level model

- `L0 Downloaded` — Starter downloaded.
- `L1 Ready` — project opened; rules and core skills detected.
- `L2 First task` — local context started and one task completed.
- `L3 Created` — a useful artifact such as a site, document, or email draft exists.
- `L4 Independent` — the person can choose, execute, verify, and continue a workflow.

Levels describe onboarding progress, not intelligence, competence, or personal worth.

## Local files

- `ABOUT_ME.md` — optional preferences; ignored by Git.
- `MY_PROGRESS.md` — local progress and help request; ignored by Git.
- `CLIENT_SYNC.json` — optional preview payload; ignored by Git.

Never store passwords, one-time codes, financial details, identity documents,
private messages, full chat history, or client files in a support payload.

## Human-readable preflight

The first run must report:

- whether Codex is running;
- whether the Starter project is open;
- whether `AGENTS.md` exists;
- which core and optional skills are visible;
- whether local private files are protected from Git;
- that Git is not required for ordinary client use;
- one recovery action for every failed check.

The client sees plain language. A separate technical report may contain paths,
versions, and diagnostic details for support.

## Future website interface

The starter may prepare a preview containing:

- random installation ID;
- starter version;
- language and operating system;
- current onboarding level;
- completed setup checks;
- optional help category;
- optional contact supplied by the person;
- consent timestamp.

The preview is not telemetry. It remains local until the person confirms the
exact destination and fields. The endpoint, domain, retention period, privacy
notice, storage owner, and deletion route are unresolved gates.

Use distinct funnel events:

`download != install != first_run != first_result`

GitHub download counts prove only asset downloads, not installations or people.

The download page must include:

- one official OpenAI installer link;
- one verified Starter release link;
- one public GitHub source link;
- the release version and SHA-256 checksum;
- a privacy summary and explicit no-hidden-tracking statement;
- accurate contributor or acknowledgement credits only after consent and proof.

## Personal integrations

Gmail, Calendar, Telegram, Drive, GitHub, and other accounts are not bundled.
Connect them one at a time using the new owner's local authorization and a
separate identity check. Never migrate tokens, cookies, sessions, or secrets.

The Olya Starter does not create a bridge, server, remote control, Obsidian or
VS Code synchronization, telemetry, or background reporting.

## Acceptance matrix

- Fresh download/unzip passes.
- Official Codex opens the Starter project.
- `НАЧАТЬ` triggers onboarding.
- Local private context remains ignored by Git.
- Core skills are discovered without global installation.
- The first task produces a visible local artifact.
- Restart/resume preserves local context.
- Opt-in report previews exact fields and sends nothing without confirmation.
- Every failure path gives one human-readable recovery action.
- macOS/Windows support is claimed only after an actual test on that platform.

## Proof plan

- Run the deterministic repository validator and public-surface guard.
- Build a release candidate from tracked public files.
- Extract it into a fresh temporary directory.
- Run Codex in read-only, ephemeral mode with user configuration ignored.
- Verify rule and skill discovery, onboarding, numbering, privacy, check-in
  preview, and zero need for an outside personal profile.
- Produce a PASS/PARTIAL/MISSING/UNVERIFIED acceptance report.

## Gates

- Local implementation and validation: approved by route `10+`.
- Publishing a new GitHub release: separate approval after proof.
- Connecting a website endpoint or database: confirmed domain, owner, fields,
  retention, privacy notice, and destination.
- Sending a client check-in: the client's explicit consent.
