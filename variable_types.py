# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it is the value it contains.

#            String-example:
first_name = "Buddha."

print(first_name)

#            You can use a variable inside a string using an f-string.
#            The variable has to be placed inside curly braces {}.

#            f-string example:
print(f"Hi {first_name}!")

#            An integer is a whole number.
#            make sure to not write numbers in quotes.

#            Integer-example:
age = 42

print(f"You are {age} years old!")

#            A float is a number with a decimal point.

#            Float-example:
price = 10.99

print(f"The price is {price}€ per piece.")

#            A boolean is a True or False value.
#            Note: Use a capital T in True and a capital F in False.

#            Boolean-example:
is_student = False

print(f"Are you a student?: {is_student}.")

#            A common use for booleans is within an if/else statement,
#            rather than just printing them directly.
#            The 'if' blockkis executed if the value is True,
#            the 'else' block if it is False.

#            Boolean-example in an if/else statement:
if is_student:
    print("You are a student.")

else:
    print("You aren't a student.")
