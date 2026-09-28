#!/usr/bin/env python3
"""Build app.py from compressed parts (for Docker / Render)."""
import base64, gzip
from pathlib import Path

def main():
    here = Path(__file__).parent
    out = here / "app.py"
    parts = sorted(here.glob("app.py.gz.b64.part*"))
    single = here / "app.py.gz.b64"
    if single.exists():
        b64 = single.read_text().strip()
    elif parts:
        b64 = "".join(p.read_text().strip() for p in parts)
    else:
        raise SystemExit("No app.py.gz.b64 or part files found")
    data = gzip.decompress(base64.b64decode(b64))
    out.write_bytes(data)
    print("Wrote", out, len(data), "bytes")

if __name__ == "__main__":
    main()
