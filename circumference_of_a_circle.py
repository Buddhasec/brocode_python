# First, import the math module to access advanced math functions.
import math

# Get the radius from the user, typecast it to a float.
radius = float(input("Enter the radius (can be a whole number or decimal): "))

# Calculate the circumference using the formula: 2 * pi * radius.
# math.pi provides the value of pi.
circumference = 2 * math.pi * radius

# Print the result using an f-string, rounded to 2 decimal places.
print(f"The circumference is: {circumference:.2f}.")
