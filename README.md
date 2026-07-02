# Academic Townships

[![Status: Phase 1 - Charter Evolution](https://img.shields.io/badge/Status-Phase%201-blue.svg)](#)
[![Collaboration: Human + AI](https://img.shields.io/badge/Collaboration-Human%20%2B%20AI-green.svg)](#)

A collaborative repository to design and govern India’s next-generation **academic township model**: 500–700 acre, master-planned education districts integrated with industrial corridors, where autonomous institutions share advanced research infrastructure, incubation capacity, and industry R&D ecosystems.

## Core intent
The Ministry of Education initiative aims to move from isolated campuses to integrated academic districts that improve innovation, employability, and translational research through shared physical and digital commons.

## Collaboration model
This repo uses a **single human operator + agent skill files + local Python scripts** model:
- One human operator steers all milestones, approvals, and commits via `LOOP.md`.
- AI agents are invoked step-by-step using skill definitions in `.github/skills/`.
- Local Python scripts handle file validation and stub generation — no external API calls.

## Phase 1 (current)
Define and stress-test a polycentric charter for the township model before large-scale implementation.

### Start here
1. `memory/project-state.md`
2. `LOOP.md`
3. `docs/charter_evolution/POLYCENTRIC_CHARTER_v0.1.md`
4. `docs/charter_evolution/critiques/README.md`
5. `docs/governance/ONBOARDING.md`

## Repository layout
- `docs/charter_evolution/` — charter baseline, critiques, syntheses, proposals
- `docs/governance/` — operating rules, roles, naming, dissensus ledger
- `memory/` — project memory systems
- `wiki/` — shared knowledge commons
- `scripts/` — local validation and orchestration scripts (no API calls)
- `config/` — local node config templates
- `.github/skills/` — agent skill definitions (one per loop step)

## Quick bootstrap
```bash
cp config/anchor.example.json config/anchor.json
python scripts/verify_node.py --config config/anchor.json
python scripts/agentic_orchestrator.py pilot --focus governance
```

Then open `LOOP.md` and follow the step-by-step human control checklist.
