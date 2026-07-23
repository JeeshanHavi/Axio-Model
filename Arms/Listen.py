import speech_recognition as sr


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User : {query}")
    except:
        return

    query = str(query).lower()
    return query


def mic():
    query = listen()
    return query
