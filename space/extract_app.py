#!/usr/bin/env python3
"""Extract app.py from app.py.gz.b64 (run once after clone if needed)."""
import base64, gzip
from pathlib import Path

def main():
    b64 = Path(__file__).with_name("app.py.gz.b64")
    out = Path(__file__).with_name("app.py")
    if out.exists() and out.stat().st_size > 1000:
        print("app.py already present")
        return
    data = gzip.decompress(base64.b64decode(b64.read_text().strip()))
    out.write_bytes(data)
    print("Wrote", out, "bytes", len(data))

if __name__ == "__main__":
    main()
