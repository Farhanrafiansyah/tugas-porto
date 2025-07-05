import gradio as gr
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

def chatbot(message, history):

    chat_history = []
    for user_msg, bot_msg in history:
        chat_history.append({"role": "user", "content" : user_msg})
        chat_history.append({"role": "assistant", "content": bot_msg})

    chat_history.append({"role": "user", "content" : message})

    # Kirim permintaan ke model
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat:free",
            messages=chat_history
        )
        reply = response.choices[0].message.content

    except Exception as e:
        print("❌ Terjadi kesalahan:", e)

    return reply

demo = gr.ChatInterface(
    fn=chatbot,
    title="Bot ai icikiwir"
)

# Jalankan di browser
demo.launch(share=True)