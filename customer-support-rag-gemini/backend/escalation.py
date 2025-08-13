def should_escalate(history, N=2):
    """
    Returns True if escalation is needed based on:
    - Last N user messages have NEGATIVE sentiment.
    - Same user question/complaint repeated in last N user messages.
    - Any user message in last N has sentiment score <= 0.3.
    If not enough history, returns False.
    """
    # Filter only user turns
    user_turns = [t for t in history if t.get("role") == "user"]
    if len(user_turns) < N:
        return False

    lastN = user_turns[-N:]

    # Rule 1: Last N user messages have NEGATIVE sentiment
    if all(t.get("sentiment") == "NEGATIVE" for t in lastN):
        return True

    # Rule 2: Same user question/complaint repeated in last N
    texts = [t.get("text", "").strip().lower() for t in lastN]
    if len(set(texts)) == 1 and texts[0] != "":
        return True

    # Rule 3: Any user message in last N has sentiment_score <= 0.3
    for t in lastN:
        score = t.get("sentiment_score")
        if score is not None and score <= 0.3:
            return True

    return False

def escalation_reason(history, N=2):
    """
    Returns a short reason string for escalation based on which rule matched.
    """
    user_turns = [t for t in history if t.get("role") == "user"]
    if len(user_turns) < N:
        return ""
    lastN = user_turns[-N:]
    if all(t.get("sentiment") == "NEGATIVE" for t in lastN):
        return f"{N} consecutive negative user messages"
    texts = [t.get("text", "").strip().lower() for t in lastN]
    if len(set(texts)) == 1 and texts[0] != "":
        return f"Repeated user complaint/question in last {N} turns"
    for t in lastN:
        score = t.get("sentiment_score")
        if score is not None and score <= 0.3:
            return "Strongly negative sentiment detected"
    return ""
