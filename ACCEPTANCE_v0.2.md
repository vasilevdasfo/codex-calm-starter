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
| Fresh download and unzip | PASS | RC4 was rebuilt with null-delimited UTF-8 paths, self-extracted, and passed validator plus smoke-test. `НАЧАТЬ_ЗДЕСЬ.md` is present; private local files are absent. |
| Official Codex opens project | PARTIAL | Codex CLI v0.144.1 opened a fresh temporary copy on macOS. A new owner's desktop app remains untested. |
| `НАЧАТЬ` triggers onboarding | PASS | A fresh extracted RC4 session loaded the repository-local core, reported readiness without Terminal/Python, asked one question, and produced valid numbered navigation. Olya's own desktop repeat remains the release gate. |
| Private context ignored by Git | PASS | Validator and smoke-test confirm all private profile, progress, preview, and report files are ignored and absent from the candidate file list. |
| Core skills discovered without global install | PASS | Fresh-copy preflight found all four required core skills and three optional modules plus support skill in `.agents/skills`. |
| Problem Solving Loop is complete | PASS | The validator confirms all seven phases: outcome, facts, boundary, small plan, action, verification, and continuation. |
| Numbered navigation is stable | PASS | The workspace rule and skill require a numbered menu after every non-trivial result, with exactly one recommendation and a valid `Реко:` target. |
| Olya screenshot diagnosis | PASS | Her screenshot shows the old v0.1 package with only `calm-workflow`, `context-interview`, and `privacy-gate`; it is not evidence of RC3. |
| Bridge and background sync disabled | PASS | Workspace rules forbid bridge, server, remote control, Obsidian/VS Code sync, telemetry, and background status reporting. |
| First task creates visible artifact | PASS | The Codex pilot created `my-first-site/index.html` with title, heading, viewport, Russian content, and no external resource links. |
| RC4 first result is visible | PASS | A separate fresh RC4 session created and verified `FIRST_RESULT.md` with exactly three safe site-planning steps, no external links, no account connection, and no bridge. |
| Restart/resume preserves local context | PASS | A separate ephemeral Codex session read the saved name, goal, and first-result path and returned `CONTEXT_RESUME_PASS`. |
| Opt-in report previews fields and sends nothing | PASS | The local builder produced `mode=PREVIEW_ONLY`, `destination=UNCONFIGURED`, `consent_to_send=false`, `L3`, and an explicit excluded-data list. |
| Failure gives one human-readable recovery action | PASS | The manifest route gives one Russian recovery action and explicitly tells a macOS user to cancel any developer-tools prompt. |
| Platform claims are evidence-backed | PARTIAL | macOS CLI is tested. New-owner desktop, exact device model, and Windows remain `UNVERIFIED`. |

## Screenshot audit: Olya

- The browser tab shows the GitHub release `v0.1.0`.
- Codex reports exactly three old skills: `calm-workflow`,
  `context-interview`, and `privacy-gate`.
- The model selector shows `5.6 Sol Light`.
- The sidebar shows recent chats but no pinned project.
- Therefore the screenshots do not test v0.2 RC4 and cannot prove a defect in
  its eight repository-local skills.

## Mistake-learning closure

```text
ProblemOS:
P1 — Olya received v0.1.0 with only three old skills.
U1 — GitHub latest, demis.world, vda.vc, and the local package named different versions.
L1 — One release manifest owns version, archive name, exact skill set, state, and send gate.
R1 — The build now runs the release gate before packaging and against the finished archive.
N1 — A stale client version, floating latest link, missing core skill, or unapproved send must fail.
```

- Rule: never give a client a floating release URL or a package that differs
  from `CLIENT_RELEASE_MANIFEST.json`.
- Skill: the complete Problem Solving Loop and mandatory numbered navigation
  remain part of the exact required core.
- Pipeline: `build_release.py` reads the version from the release manifest and
  validates both source and packed archive.
- Check: the smoke-test injects a v0.1.0 link, removes the Problem Solving Loop,
  and attempts an unpublished client send; all three scenarios must fail.

System maintenance:

- `attention_return`: prevents repeated client reinstall/debug cycles caused by
  stale links and incomplete skill packages.
- `maintenance_cost`: update one small manifest and run the existing build for
  each release.
- `retire_or_keep`: keep.

## Current external gate

- GitHub `releases/latest`: v0.1.0.
- `demis.world/codex`: v0.2.0-rc1.
- `vda.vc/codex`: v0.2.0-rc1 through the demis.world download.
- RC4 state: `CANDIDATE_LOCAL_ONLY`; client send is blocked.

## System-learning closure

- Rule: release PASS requires validating the extracted archive, including non-ASCII filenames.
- Skill: onboarding requires the repository-local skill path and no global copy.
- Pipeline: the release builder uses null-delimited UTF-8 Git paths and self-extracts the ZIP.
- Check: validator and smoke-test run both before packaging and against the extracted candidate.
