# Typecasting = the process of converting a variable from one data type to another.
# Common functions: str(), int(), float(), bool()

name = "Buddha Sec"
age = 36
decimal = 3.14
is_student = False

# The type() function returns the data type of a value.
# To make it visible, we need to use print().

# type() function examples:
print(type(name))
print(type(age))
print(type(decimal))
print(type(is_student))

# Typecasting can be used to explicitly convert a value to another type.

# Typecast-example:
decimal = int(decimal)
# 3.14 becomes 3

print(type(decimal))
# You can't add strings and integers directly.
# str(decimal) would turn 3 into "3", which is a string.
# instead, we keep it as an integer and do math.
decimal += 1
# 3 + 1 = 4

print(f"This is originally a float (3.14) + 1, but since we typecasted it to an integer, the result is 4 instead of 4.14. Value: {decimal}")
