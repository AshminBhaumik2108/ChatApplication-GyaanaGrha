from transformers import pipeline

# Sentiment Model : is needed for the file for the Sentiment-analysis....
# If one model Stops Working than another model comes into Existance...
try:
    sentiment_pipe = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
except Exception:
    sentiment_pipe = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Sentiment Analysis Function : 
def analyze_sentiment(text: str):
    result = sentiment_pipe(text)[0]
    # The Ashmin's sentiment analysis result is: [{'label': 'neutral', 'score': 0.8815408945083618}] : Without [0]...
    # Print the raw result from the sentiment model.....
    # print("The Ashmin's sentiment analysis result is:", result).....
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
