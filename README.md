# 🤖 Ollama-Powered DeepSeek Chatbot

A modern, **fully local AI chatbot** built using  **DeepSeek-R1** ,  **Ollama** ,  **LangChain** , and  **Streamlit** , featuring a beautiful glassmorphism UI and custom background.

This project demonstrates how powerful Large Language Models (LLMs) can be run  **locally without cloud APIs** , ensuring  **privacy, low cost, and full control** .

---
<img width="1913" height="944" alt="Screenshot 2025-12-23 073704" src="https://github.com/user-attachments/assets/11273f4d-edc0-4b80-8165-f84e77aba437" />

## 🚀 Features

* ✅ Local AI inference using **Ollama**
* ✅ **DeepSeek-R1 (1.5B)** language model
* ✅ Clean & modern **Streamlit frontend**
* ✅ Glassmorphism UI with background image
* ✅ Real-time question answering
* ✅ Privacy-friendly (no external API calls)

---

## 🧠 How It Works

1. User enters a question via the Streamlit UI
2. LangChain formats the prompt
3. Ollama runs the **DeepSeek-R1** model locally
4. The response is displayed inside a styled chat card

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – frontend UI
* **LangChain** – prompt orchestration
* **Ollama** – local LLM runtime
* **DeepSeek-R1 (1.5B)** – language model
* **HTML & CSS** – custom styling

---

## 📂 Project Structure

deepseek/
├── app.py        # Main Streamlit application
└── bg.jpg        # Background image


## 🎨 UI Preview

* Dark futuristic background
* Glassmorphism chat card
* Clean input & readable responses

  *(UI designed for demo, resume, and portfolio use)*

***⚙️ Installation & Setup***

1️⃣ Prerequisites

Python 3.9+

Ollama installed on your system

👉 Install Ollama: https://ollama.com

2️⃣ Clone the Repository

git clone https://github.com/moizbagwan/Ollama-Deepseek-Chatbot.git
cd Ollama-Deepseek-Chatbot

3️⃣ Install Dependencies

pip install streamlit langchain langchain-ollama ollama

4️⃣ Pull the DeepSeek Model

ollama pull deepseek-r1:1.5b

5️⃣ Run the Application

streamlit run app.py

📬 Author

***Abdul Moiz Bagwan***

Aspiring Data Scientist | AI & ML Enthusiast

🔗 GitHub: https://github.com/moizbagwan

### 🔖 Tags

<pre class="overflow-visible! px-0!" data-start="2711" data-end="2795"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="@w-xl/main:top-9 sticky top-[calc(--spacing(9)+var(--header-height))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-text"><span><span>AI • LLM • DeepSeek • Ollama • LangChain • Streamlit • Python • Local AI</span></span></code></div></div></pre>
