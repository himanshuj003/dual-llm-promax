# Free permanent hosting (Render)

Hugging Face Gradio Spaces now require PRO. Use **Render free** instead.

## Deploy in ~5 minutes

1. Create a free account: https://render.com
2. Dashboard → **New** → **Web Service**
3. Connect GitHub → select repo `himanshuj003/dual-llm-promax`
4. Settings:
   - **Root Directory:** `space`
   - **Runtime:** Docker
   - **Plan:** Free
5. Add environment variables (optional — users can also paste keys in the UI):
   - `OPENAI_API_KEY`
   - `ANTHROPIC_API_KEY`
   - `GOOGLE_API_KEY`
   - `XAI_API_KEY`
6. Click **Create Web Service**

Your permanent URL will look like:

`https://dual-llm-promax.onrender.com`

### Free plan notes

- Spins down after ~15 minutes of idle time
- First request after sleep can take 30–60 seconds (cold start)
- Fully free — no card required for the free tier

## Files used

- `space/app.py` — Dual LLM Gradio app
- `space/Dockerfile`
- `space/requirements.txt`
- `space/render.yaml`
