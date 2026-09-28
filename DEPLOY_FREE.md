# Free permanent hosting — Render

Hugging Face Gradio Spaces require PRO now. Use **Render free** instead.

## 5-minute deploy

1. Sign up free: https://render.com (GitHub login works)
2. **New +** → **Web Service**
3. Connect the repo: `himanshuj003/dual-llm-promax`
4. Configure:
   - **Name:** dual-llm-promax
   - **Root Directory:** `space`
   - **Runtime:** Docker
   - **Instance type:** Free
5. (Optional) Environment variables — users can also paste keys in the UI:
   - `OPENAI_API_KEY`
   - `ANTHROPIC_API_KEY`
   - `GOOGLE_API_KEY`
   - `XAI_API_KEY`
6. Click **Create Web Service**

After build finishes, your public URL is:

`https://dual-llm-promax.onrender.com`

(or whatever name you chose)

## Free plan behavior

- Sleeps after ~15 min idle
- First visit after sleep: 30–60 sec cold start
- No credit card required for free tier

## Temporary link (works now)

Until Render is ready, you can still use Gradio share when launched:
`python space/app.py` with `share=True` (local) or the existing gradio.live link.

## Source

https://github.com/himanshuj003/dual-llm-promax
