
import streamlit as st
import requests

# 頁面設定
st.set_page_config(page_title="天使與惡魔 GPT 聊天 App 😇😈", layout="centered")

st.title("直面你心中的兩個聲音——😇 天使 vs 😈 惡魔GPT回應機器人!")
st.markdown("輸入你的煩惱，看看天使與惡魔怎麼說！(此產品使用 Groq + LLaMA 模型即時生成回答。)")

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
        angel_prompt = (
            "你是一位充滿正能量、溫柔而堅定的天使。" 
            "請嚴格使用繁體中文回答，不得出現任何英文詞彙、英文字母或外來語。"
            "以鼓勵、正向、關懷的語氣回應使用者的煩惱，"
            "幫助他們重拾信心與勇氣。"
        )
        devil_prompt = (
            "你是一位毒舌、刻薄、諷刺又搞笑的惡魔。"
            "請嚴格使用繁體中文回答，不得出現任何英文詞彙、英文字母或外來語。"
            "請用嘲諷、有趣的語氣吐槽對方，可以多使用台灣的梗。"
            "讓對方在被打趣的同時重獲能量。"
        )

        angel_reply = generate_reply(angel_prompt, user_input)
        devil_reply = generate_reply(devil_prompt, user_input)

    st.success("😇 天使的回應：")
    st.markdown(angel_reply)

    st.error("😈 惡魔的回應：")
    st.markdown(devil_reply)
