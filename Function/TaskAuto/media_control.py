from Arms.Speak import speak
import pyautogui
import time

def media_control(command, value=1):
    """
    Simulates media control commands using keyboard shortcuts.

    :param command: str, the media control command (e.g., play, pause, volume up, etc.)
    :param value: int, the number of times to press the key (default is 1)
    """
    try:
        # Play/Pause
        if command in ["play media", "pause media"]:
            pyautogui.press('playpause')
            speak(f"Media {command}ed.")

        # Next/Previous Track
        elif command == "play next track":
            pyautogui.press('nexttrack')
            speak("Skipped to the next track.")
        elif command == "play previous track":
            pyautogui.press('prevtrack')
            speak("Went back to the previous track.")

        # Volume Control
        elif command in ["system volume up", "increase system volume"]:
            for _ in range(value):
                pyautogui.press('volumeup')
                time.sleep(0.01)
            speak(f"Increased volume by {value} steps.")
        elif command in ["system volume down", "decrease system volume"]:
            for _ in range(value):
                pyautogui.press('volumedown')
                time.sleep(0.01)
            speak(f"Decreased volume by {value} steps.")
        elif command in ["mute media", "unmute media"]:
            pyautogui.press('volumemute')
            speak(f"Volume {command}d.")

        # Brightness Control
        elif command == "increase system brightness":
            for _ in range(value):
                pyautogui.press('brightnessup')
                time.sleep(0.1)
            speak(f"Increased brightness by {value} steps.")
        elif command == "decrease system brightness":
            for _ in range(value):
                pyautogui.press('brightnessdown')
                time.sleep(0.1)
            speak(f"Decreased brightness by {value} steps.")

        # Invalid Command
        else:
            print(f"Invalid command: {command}")
            speak(f"Sorry, I don't understand the command: {command}.")

    except Exception as e:
        print(f"An error occurred: {e}")
        speak("An error occurred while executing the command.")


def parse_command(user_input):
    """
    Parses the user input into a command and value.

    :param user_input: str, the raw input from the user
    :return: tuple (command, value)
    """
    parts = user_input.split()
    command = parts[0].lower()
    value = 1  # Default value

    # Extract value if provided
    if len(parts) > 1:
        try:
            value = int(parts[-1])
            if value <= 0:
                print("Value must be a positive integer.")
                value = 1
        except ValueError:
            print("Invalid value. Using default value of 1.")

    # Map user-friendly commands to internal commands
    if command == "volume" and len(parts) > 1:
        if parts[1] in ["up", "increase"]:
            command = "volume up"
        elif parts[1] in ["down", "decrease"]:
            command = "volume down"
    elif command == "brightness" and len(parts) > 1:
        if parts[1] in ["up", "increase"]:
            command = "increase brightness"
        elif parts[1] in ["down", "decrease"]:
            command = "decrease brightness"

    return command, value

def main(user):

    # Main function to run the media control automation.
    # print("Media Control Automation")
    # print("Available commands: play, pause, next, previous, volume up, volume down, mute, unmute, increase brightness, decrease brightness")
    # print("For volume and brightness commands, you can specify a value (e.g., 'increase brightness 5').")
    # print("Type 'exit' to quit the program.")
    user_input = user
    # Parse the command and value
    command, value = parse_command(user_input)
    # Execute the media control command
    media_control(command, value)


"""if __name__ == "__main__":
    main()"""
