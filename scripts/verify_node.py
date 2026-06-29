#!/usr/bin/env python3
"""
Academic Townships - Node Verification
Checks config schema and local inference endpoint availability.
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request


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
        "inference_backend",
        "initiative_parameters",
        "local_boundary_constraints",
    ]
    missing = [k for k in required if k not in config]
    if missing:
        fail(f"Missing required config sections: {missing}")
    ok("Config schema validated")

    backend = config["inference_backend"]
    base_url = backend.get("base_url", "").rstrip("/")
    provider = backend.get("provider", "unknown")
    ping_url = f"{base_url}/api/tags" if provider == "ollama" else base_url

    try:
        with urllib.request.urlopen(ping_url, timeout=4) as resp:
            if resp.status == 200:
                ok(f"Inference backend reachable ({provider})")
    except urllib.error.URLError:
        print(f"[WARN] Inference backend not reachable ({provider})")

    ok("Node verification completed")


if __name__ == "__main__":
    main()
