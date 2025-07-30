# The first user input is a string, so we can keep it as is.
item = input("What item would you like to buy?: ")

# The second input is a float, so we need to typecast it accordingly.
price = float(input("What is the price?: "))

# The third input is an integer, so we typecast it to int.
quantity = int(input("How many would you like to buy?: "))

# To calculate the total, we multiply price by quantity and store it in a new variable.
total = price * quantity

# Now we print a summary of the order using an f-string.
print(f"You have bought {quantity}x {item}(s).")

# Finally, we print the total amount using an f-string as well.
# The {total:.2f} format the number to always show two decimal places,
# even if the result is a whole number (e.g. 12.00 instead of 12).
print(f"The total amount is: {total:.2f} €")
