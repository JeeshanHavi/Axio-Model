import os

print("BOOTING UP, Please wait...")

from Nervous_sys.brain import conversation
from Arms.Speak import speak
from Arms.Listen import  mic
from Computer_Vision import virtual_mouse, object_tracking
from Function.AppAuto import web_auto
from Function.AppAuto import music_auto
from Function.TaskAuto import media_control
from Function.GeneralAuto import date_time
import json
from Nervous_sys.neural_node import chatbot

# Track the state of virtual mouse, object tracker, web automation, and browser windows
virtual_mouse_running = False
object_tracker_running = False
web_auto_running = False
browser_windows = []  # List to store opened browser windows

# DATA LOADER FUNCTION FOR INTENTS______________________________________________________
def load_intents(file_path):

  with open(file_path, 'r') as f:
    data = json.load(f)

  intents = {}
  for intent in data['intents']:
    intents[intent['tag']] = intent['patterns']
  return intents

file_path = "G:\SPARC\DataBase\intents.json"
intents_data = load_intents(file_path)


# Get user input
def deploy():
    # GLOBAL VARIABLES______________________________________________________________________
    global virtual_mouse_running, object_tracker_running, web_auto_running, browser_windows

    while True:
        # TAKEN--IINPUT FROM THE USER_______________________________________________________
        try:
            # print("ENTER your command:")
            user_input = input("Enter your command: ")
            user_input =user_input.lower()

            if not user_input.strip():
                print("No input provided. Please enter a command.")
                continue
            user_input = str(user_input).strip()
            print(f"User input received: {user_input}")
            print("Processing request...[This may take a few seconds...]")
        except Exception as e:
            print(f"Error: {e}")
            return ""

        # Handle the 'exit' command to break the loop and stop the program
        if user_input in intents_data.get("exit", []):
            print("Exiting the program...")
            break

        # Virtual Mouse Handling
        # START VIRTUAL MOUSE____________________________________________
        elif user_input in intents_data.get("start virtual mouse", []):
            if not virtual_mouse_running:
                virtual_mouse.v_mouse()
                virtual_mouse_running = True
                continue
            else:
                print("Virtual mouse is already running.")
        # STOP VIRTUAL MOUSE______________________________________________
        elif user_input in intents_data.get("close virtual mouse", []):
            if virtual_mouse_running:
                print('Terminating virtual mouse')
                virtual_mouse.stop_v_mouse()
                virtual_mouse_running = False
            else:
                print("Virtual mouse is not currently running.")
                continue

        # Object Tracker Handling
        # START OBJECT TRACKER______________________________________________
        elif user_input in intents_data.get("start object tracker", []):
            print("Activating object tracker...")
            object_tracking.object_tracking()
            
        #STOP OBJECT TRACKER__________________________________________________
        elif user_input in intents_data.get("close object tracker", []):
            if object_tracker_running:
                print("Terminating object tracker...")
                os.system("taskkill /f /im  YOLOv 10 Object tracking.exe")
                object_tracker_running = False
            else:
                print("Object tracker is not currently running.")

        # WEB AUTOMATION________________________________________________________
        elif 'visit' in user_input.lower() or 'launch' in user_input.lower() or 'open' in user_input.lower():
            print("Processing request...")
            browser_window = web_auto.web_auto(user=user_input)
            browser_windows.append(browser_window)  # Store the window
            web_auto_running = True

        # MEDIA CONTROL___________________________________________________________
        elif any(command in user_input.lower() for command in [
            "play media", "pause media", "play next track", "play previous track",
            "system volume up", "increase system volume", "system volume down",
            "decrease system volume", "increase system brightness", "decrease system brightness"]):
            print("Executing media control...")
            media_control.main(user=user_input)

        elif user_input in intents_data.get("music", []):
            # chatbot(user=user_input)
            mu_in = input("Enter music name:")
            music_auto.play_music(user=mu_in)

        # DATE_TIME________________________________________________________________
        elif any(command in user_input.lower() for command in ["what is the time","what is the date",
                                                               "the time","the date","date","time",
                                                               "whats the date","whats the time"]):
            date_time.main(user=user_input)

        else:
            conversation(user=user_input)
if __name__ == '__main__':
    deploy()
