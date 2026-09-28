# Dual LLM Pro Max

Two AI models working together as one powerful system.

A flexible dual-agent architecture that combines the strengths of different large language models (Grok, Claude, GPT-4o, o1, Gemini, or local models) through collaboration modes, with tools, voice, and export capabilities.

## How to Use (Presentation)

**Interactive Gamma slides:** [How to Use Dual LLM Pro Max](https://gamma.app/docs/owkqmluiaxehvf8)

**PowerPoint download:** see [docs/PRESENTATION.md](docs/PRESENTATION.md) for the `.pptx` export link.

## Features

| Feature | Description |
|---------|-------------|
| **Generate → Critique → Refine** | Model A answers → Model B critiques → Model A produces improved final answer |
| **Parallel + Synthesize** | Both models answer independently, then one synthesizes the best result |
| **Debate Mode** | Models take different positions → synthesizer produces balanced final answer |
| **Pair sections** | ChatGPT+Claude, Claude+Gemini, Gemini+Grok, Universal (Any+Any), and more |
| **Streaming** | Final answer streams token-by-token |
| **Show Intermediate Steps** | View the initial answer, critique, or debate arguments |
| **Multi-conversation** | Create, switch, and delete multiple chat sessions |
| **Save / Load** | Export and restore full state |
| **Agent Tools** | Web Search + Code Interpreter |
| **Voice Input** | Microphone → Whisper (needs OpenAI key) |
| **Export** | Markdown or PDF |
| **Docker** | One-command deployment |

## Recommended Model Pairings

| Pair | Strength | Best For |
|------|----------|----------|
| **GPT-4o + Claude Sonnet** (default) | Strong general + careful analysis | Best overall starting pair |
| Claude + Gemini | Structure + speed | Everyday dual use |
| Gemini + Grok | Google + truth-seeking | Fast + unfiltered |
| o1 + Claude | Deep reasoning + critique | Hard problems |
| Universal (Any + Any) | Your choice | Full flexibility |

## Quick Start (Local)

```bash
git clone https://github.com/himanshuj003/dual-llm-promax.git
cd dual-llm-promax
chmod +x install_and_run.sh
./install_and_run.sh
```

Or manually:

```bash
pip install -r requirements.txt
python extract_core.py
cp .env.example .env   # add your keys
python dual_llm_promax.py
```

Open → http://localhost:7860

## Quick Start (Docker)

```bash
cp .env.example .env
docker compose up --build
```

## Public share link

```bash
python dual_llm_promax.py --share
```

## Environment Variables

```env
OPENAI_API_KEY=...          # ChatGPT / GPT-4o / o1 + Whisper
ANTHROPIC_API_KEY=...       # Claude
GOOGLE_API_KEY=...          # Gemini
XAI_API_KEY=...             # Grok (optional)
```

## License

MIT – free to use and modify.
