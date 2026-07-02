# Academic Townships — Human Control Loop (v0.2)

This file is the single control document for the charter evolution process.
A single human operator works through each sprint by following the checklist below.
All AI work is done through **skill files** in `.github/skills/`. No live API calls are used.
Local Python scripts handle file validation and stub generation only.

---

## Sprint setup

Before starting a sprint, confirm:
- [ ] `memory/project-state.md` has the current sprint goal recorded.
- [ ] The canonical charter version is known (check `memory/project-state.md` → Active Charter).

---

## Step 1 — Sprint Planning Gate

1. Open `memory/project-state.md` and update:
   - `Current Sprint Goal`
   - `Active tensions to address` (list the 1–3 tensions from the prior synthesis, or seed tensions for Sprint 1)
2. Decide the critique focus lenses for this sprint (e.g. `governance`, `inclusion`, `industry`, `ecology`, `urban-systems`).
3. Record the sprint start date.

**Gate 1 — Human approval required before proceeding.**

---

## Step 2 — Critique Wave

For each focus lens chosen in Step 1:

1. Open `.github/skills/critique.md` — read the skill instructions.
2. Invoke the AI agent using the skill prompt against `docs/charter_evolution/POLYCENTRIC_CHARTER_v<current>.md`.
3. Save the AI output as `docs/charter_evolution/critiques/critique_<YYYYMMDD>_<focus>_v0.1.md`.
4. After each critique is saved, run the structure validator:
   ```bash
   python scripts/agentic_orchestrator.py balance
   ```
   Fix any `[WARN]` before moving on.
5. Repeat for all lenses.

**Gate 2 — All critiques must pass `balance` check before proceeding.**

---

## Step 3 — Aggregate & Synthesize

1. Open `.github/skills/synthesize.md` — read the skill instructions.
2. Invoke the AI agent using the synthesize skill against all critique files.
3. Save the output as `docs/charter_evolution/SYNTHESIS_WAVE_<N>.md`.
   - Alternatively, generate a stub and then fill it using the AI agent:
     ```bash
     python scripts/agentic_orchestrator.py synthesize
     ```
4. Review the synthesis for completeness: convergences, divergences, proposed revisions shortlist, and unresolved tensions must all be present.

**Gate 3 — Human synthesis review and approval required before proceeding.**

---

## Step 4 — Polycentric Arbitration

1. Open `.github/skills/arbitrate.md` — read the skill instructions.
2. Invoke the AI agent using the arbitrate skill against the latest synthesis wave.
3. Review the arbitration record:
   - Resolvable tensions → note the resolution.
   - Irreducible tensions → these go to `docs/governance/dissensus_ledger.md`.
4. Update `docs/governance/dissensus_ledger.md` with any new irreducible tension entries.

**Gate 4 — Human arbitration approval required before proceeding.**

---

## Step 5 — Draft Proposal & Validation

1. Open `.github/skills/draft-proposal.md` — read the skill instructions.
2. Invoke the AI agent using the draft-proposal skill to produce `docs/charter_evolution/PROPOSAL_WAVE_<N>.md`.
3. Re-run adversarial validation: invoke the AI agent using `.github/skills/critique.md` with the `governance` lens against the draft proposal.
4. Review the adversarial critique of the proposal. Incorporate or document any objections raised.

**Gate 5 — Human proposal review and validation approval required before proceeding.**

---

## Step 6 — Lock, Tag, Retrospective

1. Open `.github/skills/lock-tag.md` — read the skill instructions.
2. Invoke the AI agent using the lock-tag skill to:
   - Produce the updated canonical charter as `docs/charter_evolution/POLYCENTRIC_CHARTER_v<new>.md`.
   - Draft updates to `memory/project-state.md`, `memory/decision-registry.md`, `memory/failure-registry.md`.
3. Review all changes before committing.
4. Commit and create a Git tag:
   ```bash
   git tag sprint-<N>-locked
   ```
5. Update `memory/project-state.md` with the new sprint state.

**Gate 6 — Final human signoff and tag required.**

---

## Quick reference — local scripts

| Command | What it does |
|---|---|
| `python scripts/verify_node.py --config config/anchor.json` | Validate config schema (no network calls) |
| `python scripts/agentic_orchestrator.py pilot --focus <lens>` | Create a critique stub for a focus lens |
| `python scripts/agentic_orchestrator.py balance` | Validate all critique files for required sections |
| `python scripts/agentic_orchestrator.py synthesize` | Create a synthesis wave stub |

## Quick reference — skill files

| Skill file | Loop step |
|---|---|
| `.github/skills/critique.md` | Step 2 |
| `.github/skills/balance.md` | Step 2 (gate) |
| `.github/skills/synthesize.md` | Step 3 |
| `.github/skills/arbitrate.md` | Step 4 |
| `.github/skills/draft-proposal.md` | Step 5 |
| `.github/skills/lock-tag.md` | Step 6 |

