#!/usr/bin/env bash
set -e

echo "=========================================="
echo "  Dual LLM Pro Max - Install & Run"
echo "=========================================="

if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is required."
    exit 1
fi

if [ ! -d "venv" ]; then
    echo "→ Creating virtual environment..."
    python3 -m venv venv
fi

echo "→ Activating virtual environment..."
source venv/bin/activate

echo "→ Upgrading pip..."
pip install --upgrade pip -q

echo "→ Installing dependencies..."
pip install -r requirements.txt -q

echo "→ Extracting dual_llm_core.py..."
python extract_core.py

if [ ! -f ".env" ]; then
    echo "→ Creating .env from .env.example..."
    cp .env.example .env
    echo ""
    echo "⚠️  Please edit .env and add your API keys:"
    echo "   OPENAI_API_KEY=..."
    echo "   ANTHROPIC_API_KEY=..."
    echo ""
    read -p "Press Enter after you have added your keys (or Ctrl+C to exit)..."
fi

echo ""
echo "→ Starting Dual LLM Pro Max..."
echo "   Open http://localhost:7860 in your browser"
echo ""

python dual_llm_promax.py
