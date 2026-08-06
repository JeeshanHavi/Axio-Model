import datetime
from Arms.Speak import speak

# Function to get the current date and time
def get_datetime_info():
    now = datetime.datetime.now()
    return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"

def main(user):

    user_input = user

    if any(command in user_input for command in ["what is the time", "what is the date", "the time", "the date",
                                                "whats the date", "whats the time"]):
        result = get_datetime_info()
        print(result)
        speak(result)
    else:
        result = "Sorry, I could not get that, you might like to try again"
        print(result)
        speak(result)


