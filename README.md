# Dual LLM Pro Max

Two AI models working together as one powerful system.

A flexible dual-agent architecture that combines the strengths of different large language models (Grok, Claude, GPT-4o, o1, or local models) through collaboration modes, with tools, voice, and export capabilities.

## Features

| Feature | Description |
|---------|-------------|
| **Generate → Critique → Refine** | Model A answers → Model B critiques → Model A produces improved final answer |
| **Parallel + Synthesize** | Both models answer independently, then one synthesizes the best result |
| **Debate Mode** | Models take different positions → synthesizer produces balanced final answer |
| **Streaming** | Final answer streams token-by-token |
| **Show Intermediate Steps** | View the initial answer, critique, or debate arguments |
| **Multi-conversation** | Create, switch, and delete multiple chat sessions |
| **Save / Load** | Export and restore full state (conversations + settings + prompts) |
| **Editable System Prompts** | Fully customize every role |
| **Temperature Control** | Independent temperature per model |
| **Local Models** | Ollama and LM Studio supported |
| **Agent Tools** | Web Search (DuckDuckGo) + Code Interpreter |
| **Voice Input** | Microphone → Whisper transcription (needs OpenAI key) |
| **Export** | Download current chat as Markdown or PDF |
| **Docker** | One-command deployment |

## Recommended Model Pairings

| Pair | Strength | Best For |
|------|----------|----------|
| **GPT-4o + Claude Sonnet** (default) | Strong general + careful analysis | Best overall starting pair |
| Claude + o1 | Structure + deep reasoning | Hard reasoning / planning |
| Grok 3 + Claude | Truth-seeking + careful analysis | Unfiltered + structured |
| Any cloud + Local (Ollama) | Privacy + cost control | Offline / sensitive use |

## Quick Start (Local)

```bash
cd dual-llm-promax
pip install -r requirements.txt

# Set your keys
cp .env.example .env
# edit .env with your keys

python dual_llm_promax.py
```

Open → http://localhost:7860

## Quick Start (Docker)

```bash
cd dual-llm-promax
cp .env.example .env
# edit .env

docker compose up --build
```

Open → http://localhost:7860

## One-Click Install & Run

```bash
cd dual-llm-promax
chmod +x install_and_run.sh
./install_and_run.sh
```

This script will:
1. Create a virtual environment
2. Install all dependencies
3. Create `.env` from the example (you fill in the keys)
4. Launch the application

## Public Website Link (Temporary)

```bash
python dual_llm_promax.py --share
```

Gradio will print a link like `https://xxxxxxxx.gradio.live` (usually lasts ~72 hours).

For a **permanent** public website, use **Hugging Face Spaces**.

## Environment Variables

```env
OPENAI_API_KEY=...          # ChatGPT / GPT-4o / o1 + Whisper voice
ANTHROPIC_API_KEY=...       # Claude
XAI_API_KEY=...             # optional — only if using Grok
```

For the default setup you only need **OpenAI** and **Anthropic** keys.

## Agent Tools

Enable the **“Enable Agent Tools”** checkbox. The generator can request:

```
TOOL: web_search | your search query
TOOL: code | print(2 + 2)
```

## Voice Input

Click the microphone, speak, then Send (requires OpenAI key for Whisper).

## Export

- **Export MD** → Markdown file
- **Export PDF** → PDF version

## Project Structure

```
dual-llm-promax/
├── dual_llm_promax.py      # Main application
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env.example
├── install_and_run.sh
└── README.md
```

## Architecture Overview

### Generate → Critique → Refine (default)
1. Generator produces an initial answer (can call tools)
2. Critic evaluates accuracy, completeness, reasoning, clarity, bias
3. Refiner produces the final improved answer

### Parallel Mode
Both models answer → synthesizer merges the strongest ideas.

### Debate Mode
Debater A takes a position → Debater B challenges it → neutral synthesizer delivers the final answer.

## License

MIT – free to use and modify.
