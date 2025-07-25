# For the countdown timer, we need to import the time module.
import time

# Store the user input as an integer (number of seconds).
user_time = int(input("Please enter a time in seconds: "))

# Create a for loop that counts down from the user input to 1,
# using a negative step of -1 (range: start, stop, step).
for x in range(user_time, 0, -1):
    # Calculate the seconds by taking the remainder of x divided by 60,
    # since there are 60 seconds in a minute.
    seconds = x % 60

    # Calculate the minutes by dividing x by 60 and taking the remainder
    # modulo 60. The int cast ensures the result is not a float.
    minutes = int(x / 60) % 60

    # Calculate the hours by dividing x by 3600 (number of seconds in an hour).
    # No modulo needed here, since we're not tracking full days.
    hours = int(x / 3600)

    # Pause the program for 1 second between updates.
    time.sleep(1)

    # Print the remaining time formatted as HH:MM:SS with leading zeros.
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

print("Time is up.")
