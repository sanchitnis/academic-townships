#!/usr/bin/env python3
"""
Academic Townships - Node Verification
Checks config schema only. No API or network calls are made.
"""

import argparse
import json
import os
import sys


def fail(msg: str) -> None:
    print(f"[FAIL] {msg}")
    sys.exit(1)


def ok(msg: str) -> None:
    print(f"[OK] {msg}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/anchor.json")
    args = parser.parse_args()

    if not os.path.exists(args.config):
        fail(f"Missing config file: {args.config}. Copy config/anchor.example.json first.")

    with open(args.config, "r", encoding="utf-8") as f:
        config = json.load(f)

    required = [
        "node_configuration",
        "initiative_parameters",
        "local_boundary_constraints",
    ]
    missing = [k for k in required if k not in config]
    if missing:
        fail(f"Missing required config sections: {missing}")
    ok("Config schema validated")

    ok("Node verification completed")


if __name__ == "__main__":
    main()
