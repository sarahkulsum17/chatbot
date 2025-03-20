def get_response(sentiment):
    responses = {
        "positive": "I'm so happy to hear that! You're doing great, keep going 💖",
        "neutral": "Thanks for sharing. I'm here if you want to talk more.",
        "negative": "I'm really sorry you're feeling this way. You're not alone, and I'm here to listen ❤️"
    }
    return responses.get(sentiment, "I'm here for you no matter what.")
