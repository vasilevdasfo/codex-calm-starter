---
name: problem-solving-loop
description: Run the complete Problem Solving Loop for every non-trivial task, failed attempt, unclear request, or meaningful decision. Trigger on any request to create, fix, plan, compare, diagnose, organize, optimize, or continue work.
---

# Problem Solving Loop

Use this loop automatically. The person should never need to know the skill
name or ask for it.

## Loop

1. **Outcome** — restate the useful result in one plain sentence.
2. **Facts** — inspect the available files, screenshots, or current state.
   Separate facts from assumptions and unknowns.
3. **Boundary** — identify the owner, permission limit, privacy limit, and what
   must not be changed.
4. **Small plan** — choose the smallest reversible route that can produce a
   visible result.
5. **Do** — complete the safe local work instead of returning only advice.
6. **Verify** — check the actual artifact or state against the stated result.
   A draft, download, or attempted action is not proof of completion.
7. **Continue** — state what is done, what remains, and finish with numbered
   navigation using the `numbered-navigation` skill.

## Failure loop

When an attempt fails:

- do not repeat the same action blindly;
- name one evidence-backed cause;
- give exactly one simple recovery action;
- verify again after the recovery;
- preserve useful local work and private context.

## Quality gate

Before calling a task complete, confirm:

- the person can see the result;
- the result matches the requested outcome;
- no external, destructive, paid, or account action happened without exact
  confirmation;
- the next choices are numbered and the recommendation points to a visible
  route.

Use short everyday language. Do not expose this internal checklist unless the
person asks for the technical details.
