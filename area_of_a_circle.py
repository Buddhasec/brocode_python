# First, import the math module.
import math

# Get the radius from the user and convert it to a float.
radius = float(input("Please enter a radius (whole number or decimal): "))

# Option 1 (commented out): Using the exponentiation operator (**).
# area = math.pi * radius ** 2

# Option 2: Using the built-in pow() function instead.
area = math.pi * pow(radius, 2)

# Print the result, rounded to 2 decimal places.
# Note: The "²" symbol is only visual - the value itself is in square units.
print(f"The area of the circle is: {area:.2f} m².")
