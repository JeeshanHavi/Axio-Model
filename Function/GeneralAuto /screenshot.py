from Speak.py import speak
from Listen.py import mic
import pyautogui

def src():
        speak("What name should I save this screenshot with ?")
        path = mic()
        path = path.lower()
        path_name = path + ".png"
        path_var = "DataBase//Screenshots/" + pathname
        src_x = pyautogui.screenshot()
        src_x.save(path_var)
        
