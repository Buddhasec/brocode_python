# Conditional expression = A one-line shorthand for an if-else statement.
# Syntax: x if condition else y
# Use this form when:
# - the condition is simple
# - the expression is used only once.

# For repeated use or readability, assign the result to a variable instead.
# Example:
#   result = "Yes" if value > 0 else "No"


num = 4

# if the condition is True print (X), otherwise print (Y)
print("Positive." if num > 0 else "Negative.")
print("Even." if num % 2 == 0 else "Odd.")

# Comparing two values.
a = 6
b = 7
# a, b = 6, 7

max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)
# print(a if a > b else b) # max()
# print(a if a < b else b) # min()


# Age check
age = 25

status = "Adult." if age >= 18 else "Minor."
print(status)
# print("Adult." if age >= 18 else "Minor.")

# Weather condition
temperature = 19

weather = "Hot." if temperature > 20 else "Cold."
print(weather)
# print("Hot." if temperature > 20 else "Cold.")

# Access Level
user_role = "Admin"

access_level = "Full Access." if user_role == "Admin" else "Limited Access."
print(access_level)
# print("Full Access." if user_role == "Admin" else "Limited Access.")
