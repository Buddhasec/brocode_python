# For loops execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.

# Example 1: Basic for-loop over a range.
for x in range(1, 11):
    print(x)
print("End.")

# Example 2: Reversed counting.
for x in reversed(range(1, 11)):
    print(x)
print("End.")

# Example 3: Counting in steps of 2.
for x in (range(1, 11, 2)):
    print(x)
print("End.")

# Example 4: Iterating over characters in a string.
credit_num = "1234-5678-90"
for char in  credit_num:
    print(char)
print("End.")

# Example 5: Skipping an iteration (e.g., skipping number 13).
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)
print("No unlucky numbers today.")

# Example 6: Breaking the loop early (e.g., stopping at 8).
for x in range(1, 21):
    if x == 8:
        break
    print(x)
print("7 is a lucky number.")
