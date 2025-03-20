import pyttsx3
import speech_recognition as sr
from transformers import pipeline

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Load sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Sorry, I'm having trouble accessing the speech service."

def main():
    speak("Hi, I'm Stella, your emotional support assistant. How are you feeling today?")
    while True:
        text = listen()
        if "exit" in text.lower() or "bye" in text.lower():
            speak("Take care! I'm always here if you need to talk.")
            break
        result = sentiment_pipeline(text)
        sentiment = result[0]['label']
        response = f"I sense that you are feeling {sentiment.lower()}. I'm here to support you."
        print(response)
        speak(response)

if __name__ == "__main__":
    main()
