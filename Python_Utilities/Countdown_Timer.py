"""
Python script to build a countdown timer that allows user to set a timer in seconds. The script should:
1. Ask the user for seconds to set the timer.
2. Show a live countdown in the terminal. 

NEW LEARNING:
divmod()
time formatting - {mins:02}

end="\r" changes how the print function finishes the line.
"\r" is a carriage return, it moves the cursor back to the start of the same line. The next print call overwrites the previous output.
"""
import time

while True:
    try:
        seconds = int(input("Enter seconds: "))
        if seconds<1:
            print("Enter a real time ")
            continue #restarts
        break #exits
    except ValueError:
        print("Enter a valid number!")

print("⏱️Timer starts.....")

for remaining in range(seconds, 0, -1):
    mins, secs = divmod(remaining, 60)
    time_format = f"{mins:02}:{secs:02}"
    print(f"Time left: {time_format}", end="\r")
    time.sleep(1)

print("Time's Up!!")