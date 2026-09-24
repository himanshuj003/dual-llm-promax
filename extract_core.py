#!/usr/bin/env python3
"""Extract dual_llm_core.py and dual_llm_ui.py."""
import gzip
import base64
from pathlib import Path

def extract_b64(name: str):
    root = Path(__file__).parent
    target = root / name
    b64_path = root / f"{name}.gz.b64"
    if target.exists() and target.stat().st_size > 1000:
        print(f"{name} already present")
        return True
    if not b64_path.exists():
        return False
    data = gzip.decompress(base64.b64decode(b64_path.read_text().strip()))
    target.write_bytes(data)
    print(f"Wrote {target} ({len(data)} bytes)")
    return True

def assemble_parts(name: str):
    root = Path(__file__).parent
    target = root / name
    if target.exists() and target.stat().st_size > 1000:
        print(f"{name} already present")
        return True
    parts = sorted(root.glob(f"{name}.part*"))
    if not parts:
        return False
    data = b"".join(p.read_bytes() for p in parts)
    target.write_bytes(data)
    print(f"Assembled {target} from {len(parts)} parts ({len(data)} bytes)")
    return True

def main():
    extract_b64("dual_llm_core.py") or print("core: use dual_llm_core.py.gz.b64")
    if not extract_b64("dual_llm_ui.py"):
        assemble_parts("dual_llm_ui.py") or print("ui: missing parts or b64")

if __name__ == "__main__":
    main()
