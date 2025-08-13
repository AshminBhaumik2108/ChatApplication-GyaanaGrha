from backend.sentiment import analyze_sentiment

def test_sentiment():
    result = analyze_sentiment("I am very unhappy and frustrated with your service.")
    assert result["label"] == "NEGATIVE", "Should detect NEGATIVE sentiment"

if __name__ == "__main__":
    test_sentiment()
    print("Sentiment test passed.")
