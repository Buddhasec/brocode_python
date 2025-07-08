# This program starts by setting different variables with different values.
# The goal is to see built-in math functions in action.

x = 3.14
y = -4
z = 5

# round() rounds a number to the nearest integer.
result1 = float(round(x))

# abs() returns the absolute value of a number (ignores the minus sign).
result2 = abs(y)

# pow() returns the result of a number raised to a given power (base ** exponent).
result3 = pow(x, z)

# max() returns the largest value among the arguments.
result4 = max(x, y, z)

# min() returns the smallest value among the arguments.
result5 = min(x, y, z)

# Using f-strings to format the output.
# The {:.2f} format rounds the float to 2 decimal places for display.
print(f"The rounded value is: {result1:.2f}.")
print(f"The absolute value is: {result2}.")
print(f"The power result is: {result3}.")
print(f"The maximum value is: {result4}.")
print(f"The minimum value is: {result5}.")
