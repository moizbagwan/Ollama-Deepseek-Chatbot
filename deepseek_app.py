import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import base64

st.set_page_config(
    page_title=" Ollama-Powered DeepSeek Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------- Background ----------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background:
            linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
            url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        .card {{
            background: rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border-radius: 18px;
            padding: 25px;
            margin-top: 20px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.35);
        }}

        .answer {{
            background: rgba(0, 0, 0, 0.55);
            padding: 18px;
            border-radius: 14px;
            margin-top: 15px;
            line-height: 1.6;
        }}

        h1 {{
            text-align: center;
            color: white;
            margin-bottom: 10px;
        }}

        .subtitle {{
            text-align: center;
            color: #d1d5db;
            margin-bottom: 25px;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("bg.jpg")

# ---------- Header ----------
st.markdown("<h1>🤖 Ollama-Powered DeepSeek Chatbot</h1>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Ask anything. Powered by <b>DeepSeek-R1</b> via Ollama</div>",
    unsafe_allow_html=True
)

# ---------- Card ----------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    prompt = ChatPromptTemplate.from_template(
        "Question: {question}\n\nAnswer: Let's think step by step."
    )

    model = OllamaLLM(model="deepseek-r1:1.5b")
    chain = prompt | model

    question = st.text_input("💬 Enter your question")

    if question:
        with st.spinner("Thinking... 🤔"):
            response = chain.invoke({"question": question})
            st.markdown("### 🧠 Answer")
            st.markdown(f"<div class='answer'>{response}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
