import streamlit as st
import os
from backend.chains import run_chain
from backend.satisfaction import record_score

st.set_page_config(page_title="Customer Support RAG + Sentiment", layout="wide")

if "session_id" not in st.session_state:
    st.session_state.session_id = os.urandom(8).hex()
if "history" not in st.session_state:
    st.session_state.history = []

# Setting the Sidebar of the file for the..
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Google API Key", type="password", value="Gemini_API_Key_Here")
if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.5)
k = st.sidebar.slider("Top K", 1, 10, 4)
st.sidebar.markdown("---")

# Sidebar for feedback......
st.sidebar.subheader("Feedback")
satisfaction = st.sidebar.slider("Satisfaction (1–5)", 1, 5, 5)
if st.sidebar.button("Submit rating"):
    avg = record_score(st.session_state.session_id, satisfaction)
    st.sidebar.success(f"Avg: {avg:.2f}")

st.title("Customer Support Chat (Gyaana-grha Application for Customer Support)")
st.caption("Analyzing customer sentiment and escalation patterns to provide empathetic and effective responses.")

# for turn in st.session_state.history:
#     if turn["role"] == "user":
#         st.chat_message(turn["role"]).markdown(turn["text"])
#     else:
#         st.chat_message(turn["role"]).markdown(turn["text"])

for turn in st.session_state.history:
    if turn["role"] != "user":  
        st.chat_message(turn["role"]).markdown(turn["text"])

query = st.chat_input("Type your question...")
if query:
    st.session_state.history.append({"role": "user", "text": query})
    result, latency = run_chain(query, st.session_state.history)
    st.session_state.history.append({
        "role": "assistant",
        "text": result["answer"],
        "sentiment": result["sentiment"]["label"]
    })
    st.chat_message("assistant").markdown(result["answer"])
    st.markdown(f"**Sentiment:** {result['sentiment']['label']} ({result['sentiment']['score']:.2f}) \n\n| Mood: {result['sentiment']['mood']}")
    if result["escalation"]["flag"]:
        st.warning(f"Escalation triggered: {result['escalation']['reason']}\n\nOffer handoff to human.")
    st.markdown("**Sources:**")
    for src in result["sources"]:
        st.caption(f"{src['title']}: {src['snippet']}")
    st.caption(f"Latency: {latency} ms")

with st.expander("Metrics"):
    st.write(f"Avg latency: {latency if query else 'N/A'} ms")
    negatives = [t for t in st.session_state.history if t.get("sentiment") == "NEGATIVE"]
    st.write(f"Negatives in last 10: {len(negatives)}")
