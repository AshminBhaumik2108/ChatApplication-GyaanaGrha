import streamlit as st
import os
from backend.chains import run_chain
from backend.satisfaction import record_score

# Setting the page configuration for the Streamlit app...
st.set_page_config(page_title="CSC Gyaana-grha", layout="wide")

# Creates a unique session ID for the current user’s chat session....
# os.urandom(8) generates 8 bytes of cryptographically random data....
# Eg. : "f4a7c12b9d8e4f67" (Example SessionID)....
if "session_id" not in st.session_state:
    # In Our App, this is later used when recording Satisfaction scores....
    st.session_state.session_id = os.urandom(8).hex()
if "history" not in st.session_state:
    st.session_state.history = []

# Setting the Sidebar of the file for the..
st.sidebar.title("Settings")
# Sidebar for API key and parameters (We can set the API key and parameters here).....
api_key = st.sidebar.text_input("Google API Key", type="password", value="", placeholder="Enter API Key")
if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key
# Temperature and Top K sliders for LLM parameters...
# (Mainly Not Implemented) ---- 
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.5)
k = st.sidebar.slider("Top K", 1, 10, 4)
st.sidebar.markdown("---")

# Sidebar for feedback......
st.sidebar.subheader("Feedback")
satisfaction = st.sidebar.slider("Satisfaction (1–5)", 1, 5, 5)
if st.sidebar.button("Submit rating"):
    avg = record_score(st.session_state.session_id, satisfaction)
    st.sidebar.success(f"Avg: {avg:.2f}")

# Title and description of the Streamlit app...
st.title("Customer Support Chat (Gyaana-grha Application for Customer Supports)")
st.caption("Analyzing customer sentiment and escalation patterns to provide empathetic and effective responses.")

# for turn in st.session_state.history:
#     if turn["role"] == "user":
#         st.chat_message(turn["role"]).markdown(turn["text"])
#     else:
#         st.chat_message(turn["role"]).markdown(turn["text"])

for turn in st.session_state.history:
    if turn["role"] != "user":  
        st.chat_message(turn["role"]).markdown(turn["text"])

# Input for user query... (Prompt Area...)
query = st.chat_input("Type your Question here ...")

if query:
    st.session_state.history.append({"role": "user", "text": query})
    try:
        result, latency = run_chain(query, st.session_state.history)
    except Exception as e:
        st.error(f"Error during LLM response: {e}")
        result, latency = {"answer": "Sorry, the system is currently overloaded or unavailable.", "sources": [], "sentiment": {"label": "NEUTRAL", "score": 0.0, "mood": "calm"}, "escalation": {"flag": False, "reason": ""}}, 0
    st.session_state.history.append({
        "role": "assistant",
        "text": result["answer"],
        "sentiment": result["sentiment"]["label"],
        "sentiment_score": result["sentiment"].get("score", None)
    })
    # Store result and latency in session_state for later use in Metrics expander
    st.session_state.last_result = result
    st.session_state.last_latency = latency

    st.chat_message("assistant").markdown(result["answer"])
    st.markdown(f"**Sentiment:** {result['sentiment']['label']} ({result['sentiment']['score']:.2f}) \n\n| Mood: {result['sentiment']['mood']}")
    if result["escalation"]["flag"]:
        st.warning(f"Escalation triggered: {result['escalation']['reason']}\nOffer handoff to human.")
        print(f"Escalation triggered: {result['escalation']['reason']}\nOffer handoff to human.")
    st.markdown("**Sources:**")
    for src in result["sources"]:
        st.caption(f"{src['title']}: {src['snippet']}")
    st.caption(f"Latency: {latency} ms")

with st.expander("Metrics"):
    # Use session_state to persist result and latency across reruns
    last_result = st.session_state.get("last_result", None)
    last_latency = st.session_state.get("last_latency", None)
    st.write(f"Avg latency: {last_latency if last_latency is not None else 'N/A'} ms")
    negatives = [t for t in st.session_state.history if t.get("sentiment") == "NEGATIVE"]
    st.write(f"Negatives in last 10: {len(negatives)}")
    if last_result is not None:
        st.markdown("**Sources:**")
        for src in last_result["sources"]:
            st.caption(f"{src['title']}: {src['snippet']}")
        st.caption(f"Latency: {last_latency} ms")
