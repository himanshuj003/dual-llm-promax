"""Entry point for Dual LLM Pro Max"""
from pathlib import Path

_root = Path(__file__).parent
if not (_root / "dual_llm_core.py").exists() or (_root / "dual_llm_core.py").stat().st_size < 1000:
    import extract_core
    extract_core.main()

from dual_llm_ui import create_ui
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dual LLM Pro Max")
    parser.add_argument("--share", action="store_true")
    parser.add_argument("--port", type=int, default=7860)
    args = parser.parse_args()
    demo = create_ui()
    demo.launch(server_name="0.0.0.0", server_port=args.port, share=args.share, show_error=True)
