# For loops execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.

# Example for basic Syntax of a for loop using an integer:
for x in range(1, 11):
    print(x)
print("End.")

# Example for reversed counting:
for x in reversed(range(1, 11)):
    print(x)
print("End.")

# Example for counting in steps:
for x in (range(1, 11, 2)):
    print(x)
print("End.")

# Example for basic Syntax of a for loop using a string:
credit_num = "1234-5678-90"
for x in  credit_num:
    print(x)
print("End.")

# Example for basic Syntax of a for loop skipping an iteration:
for x in range(1, 21):
    # If the number is exactly 13, no number will be printed.
    if x == 13:
        continue
    else:
        print(x)
print("No unlucky numbers today.")

# Example for basic Syntax of a for loop breaking an iteration:
for x in range(1, 21):
    # If the number is exactly 8, the iteration stops.
    if x == 8:
        break
    else:
        print(x)
print("7 is a lucky number.")
