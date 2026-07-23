import pyttsx3

def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)
    engine.setProperty('rate', 180)
    print(" ")
    print(f"User : {text}.")
    print(" ")
    engine.say(text)
    engine.runAndWait()
  
