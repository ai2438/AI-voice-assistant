import speech_recognition as sr 
listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("listaning")
        voice = listener.listen(source)
        command = listener.recognizer_google(voice)
        print(command)
except:
    pass