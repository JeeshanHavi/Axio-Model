import os
import speech_recognition as sr


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
    except:
        return ""

    query = str(query).lower()
    print(query)
    return query


def wakeup():
    key_command = listen().lower()
    if "wake up" in key_command:
        os.startfile(r'') #SPARC file PATH
    else:
        pass


while True:
    wakeup()
