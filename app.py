
import streamlit as st
import requests

# 頁面設定
st.set_page_config(page_title="天使與惡魔 GPT 聊天 App 😇😈", layout="centered")

st.title("😇 天使 vs 😈 惡魔 GPT 回應機器人")
st.markdown("輸入你的煩惱，看看天使與惡魔怎麼說！使用 Groq + LLaMA 模型即時生成回答。")

# 使用者輸入
user_input = st.text_input("📝 請輸入你的煩惱或問題：", "")

# Groq API 設定
API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}
MODEL = "llama3-8b-8192"

def generate_reply(role_prompt, user_message):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": role_prompt},
            {"role": "user", "content": user_message}
        ]
    }
    try:
        res = requests.post(API_URL, headers=HEADERS, json=payload)
        res.raise_for_status()
        return res.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"⚠️ 發生錯誤：{e}"

if user_input:
    with st.spinner("天使與惡魔正在思考中..."):
        angel_prompt = "你是一個充滿正能量、關懷與鼓勵的天使，請用溫柔而堅定的語氣回應對方的煩惱。"
        devil_prompt = "你是一個毒舌、刻薄、有點搞笑的惡魔，請用譏諷又諷刺的語氣回應對方的煩惱。"

        angel_reply = generate_reply(angel_prompt, user_input)
        devil_reply = generate_reply(devil_prompt, user_input)

    st.success("😇 天使的回應：")
    st.markdown(angel_reply)

    st.error("😈 惡魔的回應：")
    st.markdown(devil_reply)
