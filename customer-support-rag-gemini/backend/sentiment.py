from transformers import pipeline

try:
    sentiment_pipe = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
except Exception:
    sentiment_pipe = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text: str):
    result = sentiment_pipe(text)[0]
    label = result['label'].upper()
    score = float(result['score'])
    mood = "calm"
    if label == "NEGATIVE":
        if any(w in text.lower() for w in ["angry", "frustrated", "not happy", "bad"]):
            mood = "frustrated"
        else:
            mood = "disappointed"
    elif label == "POSITIVE":
        mood = "relieved"
    else:
        if any(w in text.lower() for w in ["urgent", "asap", "now"]):
            mood = "urgent"
        else:
            mood = "calm"
    return {"label": label, "score": score, "mood": mood}
