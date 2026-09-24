#!/usr/bin/env python3
"""Extract dual_llm_core.py from compressed payload."""
import gzip
import base64
from pathlib import Path

def main():
    root = Path(__file__).parent
    target = root / "dual_llm_core.py"
    b64_path = root / "dual_llm_core.py.gz.b64"
    if target.exists() and target.stat().st_size > 1000:
        print("dual_llm_core.py already present")
        return
    if not b64_path.exists():
        raise SystemExit("Missing dual_llm_core.py.gz.b64")
    data = gzip.decompress(base64.b64decode(b64_path.read_text().strip()))
    target.write_bytes(data)
    print(f"Wrote {target} ({len(data)} bytes)")

if __name__ == "__main__":
    main()
