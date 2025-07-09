import math

# The formula to calculate the hypotenuse is: c = sqrt(a² + b²).
# We need two input values, side A and side B, to calculate side C.

length1 = float(input("Please enter the length of side A: "))
length2 = float(input("Please enter the length of side B: "))

# It is important to use parantheses around the full expression,
# to ensure that the square root applies to the entire sum.
length3 = math.sqrt(pow(length1, 2) + pow(length2, 2))

# Print the result, optionally rounded to 2 decimal places.
print(f"The length of side C (the hypotenuse) is: {length3:.2f}")
