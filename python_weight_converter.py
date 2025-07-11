# Python weight converter

# Ask user to input their weight (accepts decimal values).
weight = float(input("Enter your weight: "))

# Ask the user for the unit: Kilograms or Pounds.
unit = input("Kilograms or Pounds? (K or L): ")

# Check if the input is in kilograms.
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    # Each block should print only if the condition is valid.
    print(f"Your weight is: {weight:.2f} {unit}")

# Check if the iniput is in pounds.
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {weight:.2f} {unit}")

# Each if-, elif-, or else-block should be treated as a self-contained "mini-
# program" to ensure the output only appears if the conditions is valid.

# If the input was neither K nor L, print an error message.
else:
    print(f"{unit} is not valid.")
