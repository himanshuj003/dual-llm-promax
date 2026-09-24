"""Gradio UI for Dual LLM Pro Max"""
from dual_llm_core import *
import gradio as gr

def create_ui():
    dual = DualLLM()
    model_choices = [(cfg["label"], key) for key, cfg in MODEL_CONFIGS.items()]

    with gr.Blocks(title="Dual LLM Pro Max") as demo:

        gr.Markdown("# Dual LLM Pro Max")
        gr.Markdown(
            "Two models working as one • Streaming • Multi-chat • Tools • Voice • Export"
        )

        with gr.Row():
            with gr.Column(scale=1, min_width=280):
                gr.Markdown("### Conversations")
                conv_dropdown = gr.Dropdown(
                    choices=dual.get_conversation_list(),
                    value=dual.current_conv_id,
                    label="Select Chat",
                    interactive=True
                )
                with gr.Row():
                    new_chat_btn = gr.Button("New Chat", size="sm")
                    delete_chat_btn = gr.Button("Delete", size="sm", variant="stop")

                gr.Markdown("### Models")
                model_a = gr.Dropdown(choices=model_choices, value="gpt-4o", label="Model A (ChatGPT)")
                temp_a = gr.Slider(0.0, 1.5, value=0.7, step=0.05, label="Temperature A")
                model_b = gr.Dropdown(choices=model_choices, value="claude-sonnet", label="Model B (Claude)")
                temp_b = gr.Slider(0.0, 1.5, value=0.5, step=0.05, label="Temperature B")

                mode = gr.Dropdown(
                    choices=[
                        ("Generate → Critique → Refine", "critique_refine"),
                        ("Parallel + Synthesize", "parallel"),
                        ("Debate Mode", "debate"),
                    ],
                    value="critique_refine",
                    label="Mode"
                )

                show_steps = gr.Checkbox(label="Show intermediate steps", value=False)
                stream_final = gr.Checkbox(label="Stream final answer", value=True)
                enable_tools = gr.Checkbox(label="Enable Agent Tools (Search + Code)", value=False)

                gr.Markdown("### API Keys (ChatGPT + Claude)")
                key_openai = gr.Textbox(label="OpenAI / ChatGPT Key", type="password", placeholder="sk-... (required for GPT-4o / o1)")
                key_anthropic = gr.Textbox(label="Anthropic / Claude Key", type="password", placeholder="sk-ant-... (required for Claude)")
                key_xai = gr.Textbox(label="xAI / Grok Key (optional)", type="password", placeholder="xai-... (only if using Grok)")

            with gr.Column(scale=4):
                chatbot = gr.Chatbot(height=480, render_markdown=True)

                with gr.Row():
                    msg = gr.Textbox(
                        placeholder="Ask anything... (or use microphone)",
                        label="Message",
                        lines=2,
                        scale=5
                    )
                    audio_input = gr.Audio(
                        sources=["microphone"],
                        type="filepath",
                        label="Voice",
                        scale=1
                    )

                with gr.Row():
                    submit_btn = gr.Button("Send", variant="primary")
                    clear_btn = gr.Button("Clear Current Chat")
                    export_md_btn = gr.Button("Export MD")
                    export_pdf_btn = gr.Button("Export PDF")

                with gr.Row():
                    save_btn = gr.Button("Save All (JSON)")
                    load_btn = gr.UploadButton("Load JSON", file_types=[".json"])
                    download_file = gr.File(label="Download", visible=False)

        with gr.Accordion("System Prompts (Advanced)", open=False):
            prompt_generator = gr.Textbox(value=DEFAULT_PROMPTS["generator"], label="Generator", lines=4)
            prompt_critic = gr.Textbox(value=DEFAULT_PROMPTS["critic"], label="Critic", lines=3)
            prompt_refiner = gr.Textbox(value=DEFAULT_PROMPTS["refiner"], label="Refiner", lines=3)
            prompt_debate_a = gr.Textbox(value=DEFAULT_PROMPTS["debate_a"], label="Debater A", lines=2)
            prompt_debate_b = gr.Textbox(value=DEFAULT_PROMPTS["debate_b"], label="Debater B", lines=2)
            prompt_synthesizer = gr.Textbox(value=DEFAULT_PROMPTS["synthesizer"], label="Synthesizer", lines=2)
            apply_prompts_btn = gr.Button("Apply Prompt Changes")

        def refresh_conv_list():
            return gr.Dropdown(choices=dual.get_conversation_list(), value=dual.current_conv_id)

        def on_new_chat():
            dual.new_conversation()
            return refresh_conv_list(), []

        def on_delete_chat():
            dual.delete_conversation(dual.current_conv_id)
            return refresh_conv_list(), []

        def on_switch_chat(conv_id):
            if conv_id:
                dual.switch_conversation(conv_id)
                return [{"role": m.role, "content": m.content} for m in dual.current_history()]
            return []

        def user_message(message, history, audio):
            history = history or []
            text = (message or "").strip()
            if audio and not text:
                try:
                    text = dual.transcribe_audio(audio)
                except Exception as e:
                    text = f"[Voice error: {e}]"
            if not text:
                return "", history, None
            return "", history + [{"role": "user", "content": text}], None

        def bot_response(
            history, model_a_val, model_b_val, temp_a_val, temp_b_val,
            mode_val, show_steps_val, stream_val, tools_val,
            p_gen, p_crit, p_ref, p_da, p_db, p_syn,
            k_xai, k_anthropic, k_openai
        ):
            dual.model_a = model_a_val
            dual.model_b = model_b_val
            dual.temp_a = temp_a_val
            dual.temp_b = temp_b_val
            dual.enable_tools = tools_val
            dual.prompts = {
                "generator": p_gen, "critic": p_crit, "refiner": p_ref,
                "debate_a": p_da, "debate_b": p_db, "synthesizer": p_syn
            }
            dual._update_clients(xai_key=k_xai or None, anthropic_key=k_anthropic or None, openai_key=k_openai or None)

            history = history or []
            if not history:
                history = [{"role": "user", "content": "(empty)"}]
            user_msg = history[-1].get("content", "") if isinstance(history[-1], dict) else str(history[-1])
            history = list(history) + [{"role": "assistant", "content": "Thinking..."}]

            try:
                for partial in dual.run(
                    user_msg, mode=mode_val,
                    show_steps=show_steps_val, stream_final=stream_val
                ):
                    history[-1] = {"role": "assistant", "content": partial}
                    yield history, gr.update()
                yield history, refresh_conv_list()
            except Exception as e:
                import traceback
                err = f"**Error:** {str(e)}\n\n```\n{traceback.format_exc()[-800:]}\n```"
                history[-1] = {"role": "assistant", "content": err}
                yield history, refresh_conv_list()

        def clear_current():
            dual.conversations[dual.current_conv_id].history = []
            return []

        def save_all():
            from datetime import datetime
            content = dual.export_all()
            fname = f"dual_llm_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(fname, "w", encoding="utf-8") as f:
                f.write(content)
            return gr.File(value=fname, visible=True)

        def load_all(file):
            if file is None:
                return [], refresh_conv_list()
            with open(file.name, "r", encoding="utf-8") as f:
                dual.import_all(f.read())
            history = [{"role": m.role, "content": m.content} for m in dual.current_history()]
            return history, refresh_conv_list()

        def export_md():
            from datetime import datetime
            md = dual.export_markdown()
            fname = f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            with open(fname, "w", encoding="utf-8") as f:
                f.write(md)
            return gr.File(value=fname, visible=True)

        def export_pdf():
            path = dual.export_pdf()
            if path:
                return gr.File(value=path, visible=True)
            return gr.File(value=None, visible=False)

        def apply_prompts(p_gen, p_crit, p_ref, p_da, p_db, p_syn):
            dual.prompts = {
                "generator": p_gen, "critic": p_crit, "refiner": p_ref,
                "debate_a": p_da, "debate_b": p_db, "synthesizer": p_syn
            }

        new_chat_btn.click(on_new_chat, outputs=[conv_dropdown, chatbot])
        delete_chat_btn.click(on_delete_chat, outputs=[conv_dropdown, chatbot])
        conv_dropdown.change(on_switch_chat, inputs=conv_dropdown, outputs=chatbot)

        submit_btn.click(
            user_message, [msg, chatbot, audio_input], [msg, chatbot, audio_input], queue=False
        ).then(
            bot_response,
            [chatbot, model_a, model_b, temp_a, temp_b, mode, show_steps, stream_final, enable_tools,
             prompt_generator, prompt_critic, prompt_refiner, prompt_debate_a, prompt_debate_b, prompt_synthesizer,
             key_xai, key_anthropic, key_openai],
            [chatbot, conv_dropdown]
        )

        msg.submit(
            user_message, [msg, chatbot, audio_input], [msg, chatbot, audio_input], queue=False
        ).then(
            bot_response,
            [chatbot, model_a, model_b, temp_a, temp_b, mode, show_steps, stream_final, enable_tools,
             prompt_generator, prompt_critic, prompt_refiner, prompt_debate_a, prompt_debate_b, prompt_synthesizer,
             key_xai, key_anthropic, key_openai],
            [chatbot, conv_dropdown]
        )

        clear_btn.click(clear_current, outputs=chatbot)
        save_btn.click(save_all, outputs=download_file)
        load_btn.upload(load_all, inputs=load_btn, outputs=[chatbot, conv_dropdown])
        export_md_btn.click(export_md, outputs=download_file)
        export_pdf_btn.click(export_pdf, outputs=download_file)
        apply_prompts_btn.click(
            apply_prompts,
            [prompt_generator, prompt_critic, prompt_refiner, prompt_debate_a, prompt_debate_b, prompt_synthesizer],
            None
        )

        gr.Markdown("""
### Quick Tips
- **Default pair**: ChatGPT (GPT-4o) + Claude Sonnet — paste both keys on the left
- **Tools**: Enable "Agent Tools" for web search + code execution
- **Voice**: Microphone works if you paste an OpenAI key (Whisper)
- **Export**: Download chat as Markdown or PDF
- You can still switch to Grok, o1, or local models anytime
        """)

    return demo
