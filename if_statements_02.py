# Ask the user a yes/no question and store the answer in a variable.
response = input("Would you like food? (Y/N): ")

# Check if the user's input matches "Y" exactly.
if response == "Y":
    # If yes, print a positive message.
    print("Be my guest.")

else:
    # If anything else is entered, print a different message.
    print("You are missing out!")
