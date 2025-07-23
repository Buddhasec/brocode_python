# While loops execute code as long as a condition remains True.

name = input("Please enter your name: ")

# Repeat the prompt as long as no name was entered.
while name == "":
    print("You did not enter a name.")
    # Ask again to prevent an infinite loop with an empty string.
    name = input("Please enter your name: ")
print(f"Hello, {name}.")


# Ask for age and convert it to an integer.
age = int(input("Please enter your age: "))

# Repeat the prompt as long as the input is negative.
while age < 0:
    print("Age can't be negative.")
    age = int(input("Please enter your age: "))
print(f"Your age is {age}, thank you.")

# Example using a logical operator in a while loop:
food = input("Enter a food you like (q to quit): ")

# Keep looping until the user input is exactly "q" to quit.
while not food == "q":
    print(f"You like {food}.")
    food = input("Enter another food you like (q to quit): ")

print("I am hungry now, goodbye.")

# Ask for a number between 1 and 10.
num = int(input("Enter a number between 1 - 10: "))

# Keep asking until the input is within the valid range.
while num < 1 or num > 10:
    print(f"{num} is not a valid number.")
    num = int(input("Enter a number between 1 and 10: "))

print(f"Your number is: {num}.")

