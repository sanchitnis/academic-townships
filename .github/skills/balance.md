# Skill: balance

## Purpose
Validate that every critique file in `docs/charter_evolution/critiques/` contains all eight required sections and flag any structural gaps.

## Trigger
Human invokes this skill from `LOOP.md` Step 2 (Critique Wave) as a quality gate, or on demand at any point.

## Inputs
- All files matching `docs/charter_evolution/critiques/critique_*.md`

## Steps
1. Run `python scripts/agentic_orchestrator.py balance` — this checks each file for the eight required section headers and prints `[OK]` or `[WARN]` per file.
2. For any file flagged `[WARN]`, list the missing sections.
3. If any warnings exist, the human must decide whether to:
   - Patch the critique file manually, or
   - Re-invoke the `critique` skill for that focus lens.

## Required sections (checked by script)
1. SEMANTIC VULNERABILITIES
2. POWER AND GOVERNANCE GAPS
3. CROSS-STAKEHOLDER COHERENCE
4. TEMPORAL AND SCALE RISKS
5. IMPLEMENTATION RED FLAGS
6. PROPOSED REVISIONS
7. DISSENT
8. EPISTEMIC TRANSPARENCY

## Outputs
- Console report from `agentic_orchestrator.py balance`
- Human decision recorded in `LOOP.md` gate checkpoint

## No API calls
Validation is performed entirely by the local Python script. No external endpoints are contacted.
