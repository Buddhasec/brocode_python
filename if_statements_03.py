# Ask the user to enter a name and store it in the variable.
name = input("Enter your name: ")

# Check if the input is an empty string (i.e., the user entered nothing).
if name == "":
    print("You did not enter a name!")

# If the input is not empty, greet the user by name.
else:
    print(f"Welcome to the party {name}.")
