# Nested loop are loops placed inside antoher loop.
# The indentation reflects this structure:
#   outer loop:
#       inner loop:

# The outer loop controls how many times the inner loop runs.
# for x in range(3):
    # The inner loop prints numbers 1 to 9 (end value is exclusive).
    # for y in range(1, 10):
        # The end="" argument keeps the output on the same line.
        # print(y, end="")
    # This print() adds a line break after each row of numbers.
    # print()

# Example:
# Ask for user inputs, typecasted as integers for numbers.
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

# Use the user's input to control the outer loop (number of rows).
for x in range(rows):
    # The inner loop controls how many symbols to print per row.
    for y in range(columns):
        # Print the symbol on the same line, without line breaks.
        print(symbol, end="")
    # After each row, move to the next line.
    print()
