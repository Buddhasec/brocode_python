# A 2D collection is a list of lists.It's used if a grid or matrix of
# data is needed, similiar to an Excel spreadsheet.

# These are all one dimensional lists:
# fruits = ["apples", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# To create a two dimensional list, we create a list that contains
# the other lists.
# groceries = [fruits, vegetables, meats]

# Alternatively, we can create the 2D list directly without using variables,
# using nested brackets. Each inner list must be seperated by comma:
groceries = [
            ["apples", "orange", "banana", "coconut"],
            ["celery", "carrots", "potatoes"],
            ["chicken", "fish", "turkey"]
]

# To access a specific item in a 2D list, use two indices:
# The first index selects the inner list (row),
# and the second index selects the item within that list (column).
# Examples: print(groceries [0][1]) -> "orange".

# Using nested loops, we can iterate over all items in the 2D list:.
for category in groceries:
    for item in category:
        print(item, end=" ")
    print() # Newline after each sublist.

# A 2D collection can also mix types, e.g.:
# - A list of tuples
# - A tuple of tuples
# - A list of sets
# and so on.
