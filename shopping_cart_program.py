# Shopping Cart Program.

# Initialize empty lists to store food items and their corresponding prices.
foods = []
prices = []
total = 0

# Continuously prompt the user for input.
while True:
    food = input("Enter a food to buy (q to quit): ")
    # Normalize input to lower case to allow both "Q" and "q" for quitting.
    if food.lower() == "q":
        break
    else:
        # Ask the user to enter the price of the specified food.
        price = float(input(f"Enter the price of a {food}: €"))
        # This makes sure to add the food and the price input to the end of the list.
        foods.append(food)
        prices.append(price)

# Print the shopping cart summary.
print("------- YOUR CART -------")

# Print all food items on one line, separated by spaces.
for food in foods:
    print(food, end=" ")
print() # Newline after the list of items.

# Calculate the total price of all items.
for price in prices:
    total += price

# Display the total cost.
print(f"Your total is: {total:.2f}€")
