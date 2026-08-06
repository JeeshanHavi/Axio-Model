def screenshot():
        path = takecommand()
        path_name = path + ".png"
        path = "DataBase/Screenshots/"+ path_name
        path_var = pyautogui.screenshot()
        parth_var.save(path)
        Speak("Your Screenshot has been saved!") 


