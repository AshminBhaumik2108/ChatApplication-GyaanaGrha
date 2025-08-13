def should_escalate(history):
    negatives = [t for t in history[-5:] if t.get("sentiment") == "NEGATIVE"]
    if len(history) >= 2 and history[-1].get("sentiment") == "NEGATIVE" and history[-2].get("sentiment") == "NEGATIVE":
        return True
    if len(negatives) >= 3:
        return True
    intents = [t.get("intent") for t in history[-5:] if t.get("intent")]
    for intent in set(intents):
        if intents.count(intent) >= 2:
            return True
    return False

def escalation_reason(history):
    if len(history) >= 2 and history[-1].get("sentiment") == "NEGATIVE" and history[-2].get("sentiment") == "NEGATIVE":
        return "Repeated negative sentiment"
    negatives = [t for t in history[-5:] if t.get("sentiment") == "NEGATIVE"]
    if len(negatives) >= 3:
        return "Multiple negative turns"
    intents = [t.get("intent") for t in history[-5:] if t.get("intent")]
    for intent in set(intents):
        if intents.count(intent) >= 2:
            return f"Repeated intent: {intent}"
    return ""
