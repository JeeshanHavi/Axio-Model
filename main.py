import os
import time
from Arms.Listen import mic

def start_sparc():

    print("Type in 'Wake Up' to start the model or 'exit' to quit")
    while True:

        user_log = input() # USER INPUT FORMAT
        user_log = str(user_log).lower()
        user_log_len = len(user_log)
        if user_log == 'exit':
            print("TERMINATING...")
            time.sleep(5)
            break
        elif int(user_log_len) <= 1:
                pass
        elif 'wake up' in user_log:
            os.startfile('G:\\SPARC\\sparc.py')
        else:
            print("INVALID INPUT! PLEASE TRY AGAIN....")
            continue

start_sparc()
