# Collections = A single variable used to store multiple values.

# List = [] ordered and mutable. Duplicates allowed.
# Set = {} unordered and mutable (in terms of elements). No duplicates allowed.
# Tuple = () ordered and immutable. Duplicates are allowed. Faster than lists.

# ------------------------------------------------------------------------------

# Each item in a list is called an "element", and each element has an index,
# starting at 0.

# LIST EXAMPLES:

# fruits = ["Apple", "Orange", "Banana", "Coconut"]

# Use dir() to list all attributes and methods available for the list object:
# print(dir(fruits))

# Use help() to get descriptions of each method:
# print(help(fruits))

# Get the number of elements in a list:
# print(len(fruits))

# Check if an element exists in the list (returns a boolean):
# print("Apple" in fruits)

# Lists are mutable, so we can change idividual elements:
# fruits[0] = "Pineapple"

# Add an element to the end of a list:
# fruits.append("Pineapple")

# Remove a specific element by value:
# fruits.remove("Apple")

# Insert an element at a specific index:
# fruits.insert(0, "Pineapple")

# Sort the list alphabetically:
# fruits.sort()

# Reverse the order of the list:
# fruits.reverse()

# Sort in reverse alphabetical order (by combining both):
# fruits.sort()
# fruits.reverse()

# Remove all elements from the list:
# fruits.clear()

# Get the index of a specific element:
# print(fruits.index("Orange"))

# Count how many times an element appears in the list:
# print(fruits.count("Apple"))

# Slice the list to get specific elements:
# print(fruits[:::])

# Iterate over the list and print each element:
# for fruit in fruits
#   print(fruit)

# ------------------------------------------------------------------------------

# SET Examples
# A set is unordered and does not allow duplicate elements.

# fruits = {"Apple", "Orange", "Banana", "Coconut"}

# Use dir() to list all attributes and methods for a set:
# print(dir(fruits))

# Use help() for detailed method descriptions:
# print(help(fruits))

# Get the number of elements in the set:
# print(len(fruits))

# Check if an element exists in the set:
# print("Apple" in fruits)

# Sets are unordered, so index access like fruits[0] will raise an error.

# Add a new element to the set:
# fruits.add("Pineapple")

# Remove a specific element:
# fruits.remove("Apple")

# Remove and return a random element (since sets are unordered):
# fruits.pop()

# Remove all elements from the set:
# fruits.clear()

# Sets are great for storing unique values, such as a fixed list of colors:
# print(fruits)

# ------------------------------------------------------------------------------

# TUPLE Examples
# Tuples are ordered, immutable collections. They allow duplicates.

# fruits = ("Apple", "Orange", "Banana", "Coconut")

# Use dir() to list all available attributes and methods:
# print(dir(fruits))

# Use help() to view method descriptions:
# print(help(fruits))

# Get the number of elements in the tuple:
# print(len(fruits))

# Check if an element exists in the tuple:
# print("Apple" in fruits)

# Get the index of a specific element:
# print(fruits.index("Orange"))

# Count how many times an element appears:
# print(fruits.count("Apple"))

# Iterate through the tuple:
# for fruit in fruits:
#     print(fruit)
