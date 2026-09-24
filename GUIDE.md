# Dual LLM Pro Max — Complete Guide

> Two AI models working together as one powerful system.  
> **GitHub:** https://github.com/himanshuj003/dual-llm-promax

---

## 1. What is this?

**Dual LLM Pro Max** runs **two large language models together** so answers are stronger than a single model.

### Pipeline (default)

```
Your question
    → Model A generates
    → Model B critiques
    → Model A refines
    → Final answer
```

Other modes: **Parallel** (both answer, then merge) and **Debate** (two sides, then synthesis).

---

## 2. Pair sections (tabs)

| Section | Model A | Model B | Keys |
|---------|---------|---------|------|
| ChatGPT + Claude | GPT-4o | Claude Sonnet | OpenAI + Anthropic |
| Claude + Gemini | Claude | Gemini Flash | Anthropic + Google |
| Gemini + Grok | Gemini | Grok 3 | Google + xAI |
| ChatGPT + Gemini | GPT-4o | Gemini | OpenAI + Google |
| ChatGPT + Grok | GPT-4o | Grok | OpenAI + xAI |
| Claude + Grok | Claude | Grok | Anthropic + xAI |
| o1 + Claude | o1 | Claude | OpenAI + Anthropic |
| o1 + Gemini | o1 | Gemini | OpenAI + Google |
| o1 + Grok | o1 | Grok | OpenAI + xAI |
| Claude Opus + ChatGPT | Opus | GPT-4o | Anthropic + OpenAI |
| Gemini Pro + Claude | Gemini Pro | Claude | Google + Anthropic |
| Gemini Pro + ChatGPT | Gemini Pro | GPT-4o | Google + OpenAI |
| Grok + Claude Opus | Grok | Opus | xAI + Anthropic |
| Local + Claude | Ollama | Claude | Anthropic |
| **Universal (Any + Any)** | Your choice | Your choice | Depends |

---

## 3. Quick start

```bash
git clone https://github.com/himanshuj003/dual-llm-promax.git
cd dual-llm-promax
chmod +x install_and_run.sh
./install_and_run.sh
```

Or:

```bash
pip install -r requirements.txt
python extract_core.py
cp .env.example .env   # add keys
python dual_llm_promax.py
```

Open **http://localhost:7860**

Public link:

```bash
python dual_llm_promax.py --share
```

---

## 4. How to use

1. Open a **section tab** at the top  
2. Click **Activate**  
3. Paste the **API keys** for that section  
4. Choose mode (Critique / Parallel / Debate)  
5. Type your question → **Send**  
6. Optional: Show intermediate steps, Agent Tools, Voice, Export MD/PDF  

---

## 5. Project story (start → end)

1. Idea: integrate two AIs into one stronger system  
2. Core: Generate → Critique → Refine (+ Parallel + Debate)  
3. APIs: OpenAI, Claude, Grok, Gemini, local models  
4. Features: streaming, multi-chat, tools, voice, export  
5. Sections: every major pair + Universal any+any  
6. Ship: GitHub, Docker, install script, this guide  

---

## 6. Links

- **Repo:** https://github.com/himanshuj003/dual-llm-promax  
- **Local UI:** http://localhost:7860  

MIT License.
