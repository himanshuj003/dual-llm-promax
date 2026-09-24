"""
Dual LLM Pro Max - entry point
Pair sections: ChatGPT+Claude, Claude+Gemini, Gemini+Grok, ... + Universal
"""
from pathlib import Path

_root = Path(__file__).parent
_core = _root / "dual_llm_core.py"
if not _core.exists() or _core.stat().st_size < 1000:
    import extract_core
    extract_core.main()

from dual_llm_ui import create_ui
from dual_llm_core import DualLLM, MODEL_CONFIGS, DEFAULT_PROMPTS, PAIR_PRESETS

__all__ = ["create_ui", "DualLLM", "MODEL_CONFIGS", "DEFAULT_PROMPTS", "PAIR_PRESETS"]

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Dual LLM Pro Max")
    parser.add_argument("--share", action="store_true", help="Create a public Gradio link")
    parser.add_argument("--port", type=int, default=7860, help="Port to run on")
    args = parser.parse_args()
    demo = create_ui()
    demo.launch(server_name="0.0.0.0", server_port=args.port, share=args.share, show_error=True)
