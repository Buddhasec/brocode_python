# A beginner-friendly calculator using basic arithmetic operations.

# Ask the user to input an operator. Accepted values: +, -, *, /.
operator = input("Enter an operator (+ - / *): ")

# Ask the user for the first number and convert it to a float for decimal support.
num1 = float(input("Enter the first number: "))

# Ask the user for the second number.
num2 = float(input("Enter the second number: "))

# Check which operator the user entered and perform the corresponding operation.
# The result is printed using an f-string formatted to 2 decimal places.

if operator == "+":
    result = num1 + num2
    print(f"{result:.2f}")

elif operator == "-":
    result = num1 - num2
    print(f"{result:.2f}")

elif operator == "*":
    result = num1 * num2
    print(f"{result:.2f}")

elif operator == "/":
    result = num1 / num2
    print(f"{result:.2f}")

# If the operator input does not match any valid symbol, return an error message.
else:
    print(f"{operator} is not a valid operator.")
