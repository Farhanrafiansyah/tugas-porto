import gradio as gr
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",  
)

def chatbot(message, history):
    chat_history = []
    for user_msg, bot_msg in history:
        chat_history.append({"role": "user", "content": user_msg})
        chat_history.append({"role": "assistant", "content": bot_msg})

    chat_history.append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct:free",  
            messages=chat_history
        )
        reply = response.choices[0].message.content
        return reply

    except Exception as e:
        print("❌ Terjadi kesalahan:", e)
        return "Maaf, terjadi kesalahan dalam memproses pesan Anda."

demo = gr.ChatInterface(
    fn=chatbot,
    title="Bazz AI"
)

demo.launch(share=True)
