from transformers import pipeline

# Load LLM-based sentiment analysis pipeline (BERT or RoBERTa)
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result['label'].lower()
    if 'positive' in label:
        return "positive"
    elif 'negative' in label:
        return "negative"
    else:
        return "neutral"
