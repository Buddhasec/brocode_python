name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")

# The len() function returns the total number of characters in the string.
name_length = len(name)
print(name_length)

# The find() method returns the index of the first occurrence of the given
# character, counting from 0. It returns -1 if the character is not found.
first_index = name.find("d")
print(first_index)

# The rfind() method returns the index of the last occurrence of the given character.
# It also returns -1 if the character is not found.
last_index = name.rfind("d")
print(last_index)

# The capitalize() method returns a copy of the string with the first character
# in uppercase and all other cahracters in lowercase.
capitalized_name = name.capitalize()
print(capitalized_name)

# The upper() method returns a copy of the string converted to uppercase.
uppercase_name = name.upper()
print(uppercase_name)

# The lower() method returns a copy of the string converted to lowercase.
lowercase_name = name.lower()
print(lowercase_name)

# The isdigit() method returns True if all character in the string are digits,
# otherwise, it returns False.
isdigit_name = name.isdigit()
print(isdigit_name)

# The isalpha() method returns True if all characters in the string are letters.
# Note: Spaces or punctuation cause this to return False.
isalpha_name = name.isalpha()
print(isalpha_name)

# The count() method returns the number of times a specified character appears
# in the string.
count_num = phone_number.count("8")
print(count_num)

# The replace() method returns a copy of the string with all occurrences of the
# first argument replaced by the second. Here, all "7"s are removed from the
# phone number.
replace_num = phone_number.replace("7", "")
print(replace_num)

# To get an overview of all available string methods, use help(str).
# Press Space in the terminal to scroll through the help text.
