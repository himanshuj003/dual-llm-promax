#!/usr/bin/env python3
"""Extract dual_llm_core.py and dual_llm_ui.py from compressed payloads."""
import gzip
import base64
from pathlib import Path

def extract(name: str):
    root = Path(__file__).parent
    target = root / name
    b64_path = root / f"{name}.gz.b64"
    if target.exists() and target.stat().st_size > 1000:
        print(f"{name} already present ({target.stat().st_size} bytes)")
        return
    if not b64_path.exists():
        print(f"Skip {name}: missing {b64_path.name}")
        return
    data = gzip.decompress(base64.b64decode(b64_path.read_text().strip()))
    target.write_bytes(data)
    print(f"Wrote {target} ({len(data)} bytes)")

def main():
    extract("dual_llm_core.py")
    extract("dual_llm_ui.py")

if __name__ == "__main__":
    main()
