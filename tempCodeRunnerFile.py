import speech_recognition as sr
import webbrowser
from googlesearch import search

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results, please check your internet connection.")
        return None

def search_google(query):
    if query:
        print("Searching Google...")
        from googlesearch import search

def search_google(query):
    for result in search(query, num_results=1):  # Use `num_results` instead of `num`
        print("Top search result:", result)

        print(f"Top Result: {result}")
        webbrowser.open(result)
        break
    else:
        print("No query to search.")

if __name__ == "__main__":

    query = recognize_speech()
    search_google(query)