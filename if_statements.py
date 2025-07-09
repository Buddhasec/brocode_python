# Always check for exceptions and blocking conditions first.
# The else block should only allow access if all checks pass.

age = int(input("Please enter your age: "))

if age <1:
    print("That age is invalid.")
elif age >=99:
    print("You are too old.")
elif age <=17:
    print("You are not eligible due to your age.")

else:
    print("You are eligible, welcome.")

# With >= x → always check the largest values first.
# With <= x → always check the smallest values first.

# age = int(input("What is your age?: "))

# if age >=120:
    # print("We do not believe you.")
# elif age >=65:
    # print("Senior ticket.")
# elif age <1:
    # print("Invalid.")
# elif age <=3:
    # print("Entry free.")
# elif age <=11:
    # print("Kid price.")
# elif age <=17:
    # print("Juvi price.")
# else:
    # print("Normal price.")

