# Codex Calm Starter v0.2 — acceptance report

Status values: `HAVE`, `PARTIAL`, `MISSING`, `UNVERIFIED`, `PASS`, `FAIL`.

## Baseline audit before v0.2 P0 repairs

| Requirement | Baseline | Evidence / gap |
|---|---|---|
| Fresh download and unzip | HAVE | The v0.1 release asset downloaded, extracted, and passed its repository validator. |
| Official Codex opens project | PARTIAL | A local Codex CLI read-only smoke-test opened the extracted project on macOS. A new owner's desktop app was not tested. |
| `НАЧАТЬ` triggers onboarding | MISSING | No dedicated first-run trigger or single-path guide existed. |
| Private context ignored by Git | HAVE | `.gitignore` contains `ABOUT_ME.md`; the release contains only the template. |
| Core skills discovered without global install | PARTIAL | Codex discovered the three v0.1 project skills, but the required v0.2 core was incomplete. |
| First task creates visible artifact | MISSING | No deterministic first-result scenario existed. |
| Restart/resume preserves local context | UNVERIFIED | No restart/resume test existed. |
| Opt-in report previews fields and sends nothing | MISSING | No local check-in preview contract existed. |
| Failure gives one human-readable recovery action | MISSING | The validator targeted maintainers, not a beginner. |
| Platform claims are evidence-backed | PARTIAL | macOS CLI was exercised; desktop-owner, Windows, and device model remain unverified. |

## Current target computer

- Owner: `UNKNOWN`
- Operating system: `UNKNOWN`
- Device model: `UNKNOWN`

## Post-repair result

| Requirement | Current | Evidence / remaining gate |
|---|---|---|
| Fresh download and unzip | PASS | RC1 was rebuilt with null-delimited UTF-8 paths, self-extracted, and passed validator plus smoke-test. `НАЧАТЬ_ЗДЕСЬ.md` is present; private local files are absent. |
| Official Codex opens project | PARTIAL | Codex CLI v0.144.1 opened a fresh temporary copy on macOS. A new owner's desktop app remains untested. |
| `НАЧАТЬ` triggers onboarding | PASS | A fresh Codex session invoked the repository onboarding skill, ran preflight, and continued the Russian first-run route. |
| Private context ignored by Git | PASS | Validator and smoke-test confirm all private profile, progress, preview, and report files are ignored and absent from the candidate file list. |
| Core skills discovered without global install | PASS | Fresh-copy preflight found all four required core skills and three optional modules plus support skill in `.agents/skills`. |
| Numbered navigation is stable | PASS | A fresh read-only Codex session produced two routes plus `0`, exactly one recommended star, a separate `Почему:` line, and a valid `Реко:` target. |
| First task creates visible artifact | PASS | The Codex pilot created `my-first-site/index.html` with title, heading, viewport, Russian content, and no external resource links. |
| Restart/resume preserves local context | PASS | A separate ephemeral Codex session read the saved name, goal, and first-result path and returned `CONTEXT_RESUME_PASS`. |
| Opt-in report previews fields and sends nothing | PASS | The local builder produced `mode=PREVIEW_ONLY`, `destination=UNCONFIGURED`, `consent_to_send=false`, `L3`, and an explicit excluded-data list. |
| Failure gives one human-readable recovery action | PASS | Preflight emits one Russian recovery action for missing Codex signal, rules, core skills, or privacy ignore coverage. |
| Platform claims are evidence-backed | PARTIAL | macOS CLI is tested. New-owner desktop, exact device model, and Windows remain `UNVERIFIED`. |

## System-learning closure

- Rule: release PASS requires validating the extracted archive, including non-ASCII filenames.
- Skill: onboarding requires the repository-local skill path and no global copy.
- Pipeline: the release builder uses null-delimited UTF-8 Git paths and self-extracts the ZIP.
- Check: validator and smoke-test run both before packaging and against the extracted candidate.
