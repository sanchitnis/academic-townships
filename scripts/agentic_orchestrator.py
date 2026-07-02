#!/usr/bin/env python3
"""
Academic Townships - Agentic Orchestrator
Creates critique stubs, synthesis snapshots, and profile balance summaries.
Skill definitions live in .github/skills/. No API calls are made.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

SKILLS_DIR = Path(".github") / "skills"

REQUIRED_SECTIONS = [
    "SEMANTIC VULNERABILITIES",
    "POWER AND GOVERNANCE GAPS",
    "CROSS-STAKEHOLDER COHERENCE",
    "TEMPORAL AND SCALE RISKS",
    "IMPLEMENTATION RED FLAGS",
    "PROPOSED REVISIONS",
    "DISSENT",
    "EPISTEMIC TRANSPARENCY",
]


class Orchestrator:
    def __init__(self, workspace: Path) -> None:
        self.workspace = workspace
        self.charter_dir = workspace / "docs" / "charter_evolution"
        self.critiques_dir = self.charter_dir / "critiques"
        self.critiques_dir.mkdir(parents=True, exist_ok=True)

    def pilot(self, focus: str) -> Path:
        skill_file = SKILLS_DIR / "critique.md"
        now = dt.datetime.now(dt.UTC)
        stamp = now.strftime("%Y%m%d_%H%M%S")
        filename = f"critique_{stamp}_{focus}_v0.1.md"
        path = self.critiques_dir / filename

        content = f"""# Critique: {focus}\n
Timestamp: {now.isoformat()}Z\n
Skill: {skill_file}\n
## 1. SEMANTIC VULNERABILITIES\n- TBD\n
## 2. POWER AND GOVERNANCE GAPS\n- TBD\n
## 3. CROSS-STAKEHOLDER COHERENCE\n- TBD\n
## 4. TEMPORAL AND SCALE RISKS\n- TBD\n
## 5. IMPLEMENTATION RED FLAGS\n- TBD\n
## 6. PROPOSED REVISIONS\n- TBD\n
## 7. DISSENT\n- TBD\n
## 8. EPISTEMIC TRANSPARENCY\n- Focus: {focus}\n"""

        path.write_text(content, encoding="utf-8")
        manifest = {
            "timestamp": now.isoformat() + "Z",
            "skill": str(skill_file),
            "focus": focus,
            "output": str(path.relative_to(self.workspace)),
        }
        manifest_path = path.with_suffix(".manifest.json")
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        print(f"Created {path}")
        return path

    def synthesize(self) -> Path:
        skill_file = SKILLS_DIR / "synthesize.md"
        critiques = sorted(self.critiques_dir.glob("critique_*.md"))
        existing = sorted(self.charter_dir.glob("SYNTHESIS_WAVE_*.md"))
        wave = len(existing) + 1
        synth_path = self.charter_dir / f"SYNTHESIS_WAVE_{wave}.md"
        lines = [
            f"# Synthesis Wave {wave}",
            "",
            f"Skill: {skill_file}",
            f"Critiques ingested: {len(critiques)}",
            "",
        ]
        for c in critiques:
            lines.append(f"- {c.name}")
        lines.append("")
        lines.append("## Convergences")
        lines.append("- TBD")
        lines.append("")
        lines.append("## Divergences")
        lines.append("- TBD")
        lines.append("")
        lines.append("## Proposed revisions shortlist")
        lines.append("- TBD")
        lines.append("")
        lines.append("## Unresolved tensions")
        lines.append("- TBD")
        synth_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"Created {synth_path}")
        return synth_path

    def balance(self) -> None:
        skill_file = SKILLS_DIR / "balance.md"
        critiques = sorted(self.critiques_dir.glob("critique_*.md"))
        print(f"Skill: {skill_file}")
        print(f"Critiques available: {len(critiques)}")
        for c in critiques:
            text = c.read_text(encoding="utf-8", errors="ignore").upper()
            missing = [section for section in REQUIRED_SECTIONS if section not in text]
            if missing:
                print(f"[WARN] {c.name} missing sections: {', '.join(missing)}")
            else:
                print(f"[OK] {c.name} structure valid")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    p_pilot = sub.add_parser("pilot", help="Create a critique stub (skill: critique.md)")
    p_pilot.add_argument("--focus", default="comprehensive", help="Focus lens for the critique")

    sub.add_parser("synthesize", help="Aggregate critiques into a synthesis wave (skill: synthesize.md)")
    sub.add_parser("balance", help="Validate critique structure completeness (skill: balance.md)")

    args = parser.parse_args()
    o = Orchestrator(Path("."))

    if args.command == "pilot":
        o.pilot(args.focus)
    elif args.command == "synthesize":
        o.synthesize()
    elif args.command == "balance":
        o.balance()


if __name__ == "__main__":
    main()
