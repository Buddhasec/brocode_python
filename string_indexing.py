# Indexing means accessing elements of a sequence using [] (index operator).
# General syntax: [start: end: step]

credit_num = "0979-8098-7855-3466"

# Accessing a single character by its index (0-based).
# Here: The 4th position (index 3)
print(credit_num[3])

# Slicing: Returns a substring from index 0 up to, but not including, index 4.
print(credit_num[0:4])
print(credit_num[5:9])

# Omitting the start index returns everything from the start index to the end.
print(credit_num[0:])

# Omitting the start index returns everything up to (but not including) index 4.
print(credit_num[:4])

# Negative indexing starts from the end (-1 is the last character).
# This returns the last 4 characters.
print(credit_num[-4:])

# Using step: skip every n-th character.
# Every second character:
print(credit_num[::2])
# Every third character:
print(credit_num[::3])

# To mask a credit card and show only the last 4 digits:
last_num = credit_num[-4:]
print(f"Your Cardnumber is:XXXX-XXXX-XXXX-{last_num}")

# Reverse the string using slicing with step -1.
print(credit_num[::-1])
