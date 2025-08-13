# 📞 Customer Support Chat (Gyaana-grha Platform)

To enhance the user experience, **GyaanaGrha** now features a **Streamlit-based AI Chatbot for Customer Support**. This chatbot is designed to:

- Analyze customer **sentiment and escalation patterns**.
- Provide **empathetic and effective responses** to **user queries**.
- Offer **instant help** for **navigating the platform and understanding recommendations**.

---

## 🚀 Features

- **Live Chat Interface** using Streamlit's `st.chat_message`
- **Sentiment Analysis** to detect customer tone
- **Escalation Detection** for urgent issues
- **Customizable Chat UI**
- **Integration Ready** for Hugging Face, Gemini, or other AI APIs

---

## 📋 Installation

Make sure you have Python 3.8+ installed.  
Clone this repository and install dependencies:

# 🛠 Environment Configuration Guide

This file explains the environment variables required for the **Customer Support Chat** application.  
All configuration values should be placed inside a `.env` file in the project root.

---

## 📄 `.env` File Format (Chat Support GyaanaGrha)

```env
GOOGLE_API_KEY = YOUR_API_KEY_HERE
GEMINI_MODEL = models/gemini-1.5-flash
EMBEDDING_MODEL = sentence-transformers/all-MiniLM-L6-v2
CHROMA_DIR = data/chroma
KB_DIR = data/knowledge_base
RETRIEVE_K = 4
TEMPERATURE = 0.5
```

## 📦 How to Clone and Run Locally

```bash
git clone https://github.com/AshminBhaumik2108/ChatApplication-GyaanaGrha.git
cd customer-support-rag-gemini
pip install setup.sh
```



