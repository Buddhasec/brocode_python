# input() = A function that prompts the user to enter data.
# It always returns the input as a string.

# input() examples:
name = input("What is your name?: ")

# Option 1 (longer way):
# age = input("How old are you?: ")
# age = int(age)

# Option 2 (shorter and cleaner way):
age = int(input("How old are you?: "))

# Since input() always returns a string,
# you must typecast it to int before performing math operations.
# The order of execution matters: Python runs code top to bottom.

age = age + 1

print(f"Hi, {name}!")
print("Happy Birthday!")
print(f"You are {age} years old!")
