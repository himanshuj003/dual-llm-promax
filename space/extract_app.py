#!/usr/bin/env python3
"""Build app.py from compressed parts (for Docker / Render)."""
import base64, gzip
from pathlib import Path

def main():
    here = Path(__file__).parent
    out = here / "app.py"
    parts = sorted(here.glob("app.py.gz.b64.part*"))
    if parts:
        b64 = "".join(p.read_text().strip() for p in parts)
    else:
        single = here / "app.py.gz.b64"
        if not single.exists():
            raise SystemExit("No app payload found")
        b64 = single.read_text().strip()
    data = gzip.decompress(base64.b64decode(b64))
    out.write_bytes(data)
    print("Wrote", out, len(data), "bytes")

if __name__ == "__main__":
    main()
