import tkinter as tk
import speech_recognition as sr
import webbrowser
from googlesearch import search

# Initialize Tkinter Window
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("400x300")

# UI Elements
label = tk.Label(root, text="Press the button and speak", font=("Arial", 14))
label.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 12), foreground="blue")
status_label.pack(pady=5)

mic_label = tk.Label(root, text="🎤", font=("Arial", 24))
mic_label.pack(pady=10)

def recognize_speech():
    status_label.config(text="Listening...", foreground="blue")
    root.update()

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        status_label.config(text=f"You said: {query}")
        search_google(query)
    except sr.UnknownValueError:
        status_label.config(text="Sorry, couldn't understand.")
    except sr.RequestError:
        status_label.config(text="Check your internet connection.")

def search_google(query):
    if query:
        status_label.config(text="Searching Google...")
        root.update()
        for result in search(query, num_results=1):
            status_label.config(text="Top Result: " + result)
            webbrowser.open(result)
            break

# UI Buttons
button = tk.Button(root, text="Start Listening", command=recognize_speech, font=("Arial", 12), bg="lightblue")
button.pack(pady=20)

exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), bg="red", fg="white")
exit_button.pack(pady=10)

# Start Tkinter Loop
root.mainloop()
