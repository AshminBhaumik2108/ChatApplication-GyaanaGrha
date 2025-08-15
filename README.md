# 📞 Gyaana-grha Chat Application – Intelligent ChatAPP

The **primary objective** of the application is to provide a **Conversational Interface** for Customers to Interact with a **customer support system**. The application aims to understand the **customer's query, sentiment, and intent, and respond accordingly**.\
To **enhance** the user experience, **GyaanaGrha** now features a **Streamlit-based AI Chatbot for Customer Support**. This chatbot is designed to:

- Analyze customer **sentiment and escalation patterns**.
- Provide **empathetic and effective responses** to **user queries**.
- Offer **instant help** for **navigating the platform and understanding recommendations**.

---

## 🎯 Target Audience

The primary target audience for this application is **customers seeking support or information** related to a specific product or service.

These users may require assistance with:

- 🛠 **Troubleshooting**
- 📘 **Product usage**
- 🗂 **Account inquiries**
- ℹ️ **General information requests**

The application is designed to serve:

- 👥 **End customers** who prefer a fast, self-service support option.
- 💡 **Users with varying technical expertise**, offering an intuitive and accessible chat-based interface.
- ❤️ **Customers seeking empathetic, context-aware responses**, especially in situations involving dissatisfaction or frustration.

By integrating **Conversational AI**, **Sentiment Analysis**, and **Knowledge Base Retrieval**, the application delivers a **seamless, efficient, and personalized support experience**.

---

## 🚀 Deployed Link of the Project

🔗 [**Gyaana-Grha Chat Application**](https://chatapplication-gyaanagrha.streamlit.app/)

---

## ✨ Key Features

| Feature                                       | Description                                                                                                                                             |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 💬 **Conversational Interface**               | Provides an intuitive, chat-like interface where customers can type their queries and receive relevant, context-aware responses.                        |
| 😊 **Sentiment & Intent Analysis**            | Analyzes customer sentiment and intent in real time, enabling more empathetic and tailored responses.                                                   |
| 📚 **Knowledge Base Integration**             | Seamlessly connects to an internal or external knowledge base to retrieve accurate information for customer queries.                                    |
| 🧠 **Large Language Model (LLM) Integration** | Utilizes an advanced LLM to generate human-like, contextually appropriate responses.                                                                    |
| ⚠️ **Error Handling & Escalation**            | Detects and manages errors gracefully, with automatic escalation to human support agents when necessary.                                                |
| 🔌 **API Integration**                        | Allows users to configure API keys directly from the sidebar, enabling integration with external APIs for additional data retrieval and task execution. |

---

## 🎯 Secondary Objectives

| Objective                              | Description                                                                                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 🌟 **Enhancing Customer Satisfaction** | Delivers accurate, helpful, and empathetic responses to improve the overall customer experience.                                      |
| 📉 **Reducing Support Ticket Volume**  | Automates responses to common queries, minimizing workload for human support teams.                                                   |
| 📊 **Analytics & Insights**            | Provides detailed analytics on customer interactions, sentiment trends, and behavior — empowering teams to refine support strategies. |

---

## ⚙️ Tech Stack

| Component                 | Technology                        |
| ------------------------- | --------------------------------- |
| 🖥 **Frontend**            | Streamlit                         |
| 🔧 **Backend**            | Python, LangChain                 |
| 🧠 **LLM**                | Gemini                            |
| 📦 **Vector Store**       | Chroma                            |
| 📊 **Embeddings**         | HuggingFace Sentence Transformers |
| 😊 **Sentiment Analysis** | HuggingFace Models                |

---

# 🛠 Environment Configuration Guide

This guide explains the **environment variables** required for the **💬 Customer Support Chat** application.  
All configuration values should be placed inside a `.env` file in the **project root directory**.

---

## 📂 How to Create Your `.env` File

- 📁 Go to your **project root**.
- 📝 Create a **new file** named `.env`.
- ⚙️ Add the following **variables** with your **own values**.

---

## 🔑 Required Environment Variables

| Variable          | Description                                                               | Example                                  |
| ----------------- | ------------------------------------------------------------------------- | ---------------------------------------- |
| `GOOGLE_API_KEY`  | 🔐 API key for accessing Google Gemini LLM services.                      | `AIzaSy...`                              |
| `GEMINI_MODEL`    | 🧠 Model name for Gemini LLM.                                             | `models/gemini-1.5-flash`                |
| `EMBEDDING_MODEL` | 📊 Embedding model used for text vectorization.                           | `sentence-transformers/all-MiniLM-L6-v2` |
| `CHROMA_DIR`      | 📂 Directory path for Chroma vector database storage.                     | `data/chroma`                            |
| `KB_DIR`          | 📚 Directory containing your knowledge base documents.                    | `data/knowledge_base`                    |
| `RETRIEVE_K`      | 🔍 Number of top results to retrieve from the vector store.               | `4`                                      |
| `TEMPERATURE`     | 🌡 Controls randomness in LLM responses (0 = deterministic, 1 = creative). | `0.5`                                    |

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
cd customer-support-chat
pip install setup.sh
```

> 📝 _Developed with ❤️ to make customer support faster, smarter, and more human by Ashmin Bhaumik._
