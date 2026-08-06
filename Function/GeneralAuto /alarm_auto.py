import time
import \
    winsound  # This is for Windows; use other libraries for different OS (e.g., `os` or `pygame` for cross-platform sound)
import datetime


def set_alarm():
    # Take the user input for the alarm time
    alarm_time = input("Set alarm time (in hh:mm format, lowercase): ").strip()
    ringtone_path = input("Enter the path to the ringtone (e.g., 'C:/path/to/ringtone.wav'): ").strip()

    # Convert the input time to a datetime object
    try:
        alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M")
    except ValueError:
        print("Invalid time format. Please use 'hh:mm' format.")
        return

    # Get the current time
    current_time = datetime.datetime.now()

    # Set the alarm to the correct time, adjusting for the next day if needed
    if alarm_time <= current_time:
        # Alarm time is in the past, set it for the next day
        alarm_time = alarm_time.replace(day=current_time.day + 1)

    print(f"Alarm set for {alarm_time.strftime('%H:%M')}.")

    # Wait until it's time for the alarm to go off
    while True:
        if datetime.datetime.now() >= alarm_time:
            print("Alarm ringing!")
            play_ringtone(ringtone_path)
            break
        time.sleep(10)


def set_timer():
    # Take the user input for the timer duration
    duration_input = input("Set timer duration (in minutes, lowercase): ").strip()
    ringtone_path = input("Enter the path to the ringtone (e.g., 'C:/path/to/ringtone.wav'): ").strip()

    try:
        duration_minutes = int(duration_input)
    except ValueError:
        print("Invalid input. Please enter a number for minutes.")
        return

    if duration_minutes <= 0:
        print("Please enter a positive number of minutes.")
        return

    print(f"Timer set for {duration_minutes} minute(s).")

    # Wait until the timer reaches the set duration
    time.sleep(duration_minutes * 60)

    print("Timer finished!")
    play_ringtone(ringtone_path)


def play_ringtone(ringtone_path):
    # Play the ringtone sound (this works on Windows with .wav files)
    try:
        winsound.PlaySound(ringtone_path, winsound.SND_FILENAME)
    except Exception as e:
        print(f"Error playing the ringtone: {e}")


# Main menu to select which function to use
def main():

    choice = input().strip()

    if choice == "alarm":
        set_alarm()
    elif choice == "timer":
        set_timer()
    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()


