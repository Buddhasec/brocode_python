# Python compound interest calculator with while loops.

# Initialize variables.
principal = 0
rate = 0
time = 0

# Prompt until the principal is a valid positive amount.
while principal <= 0:
    principle = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal must be greater than zero.")

# Prompt until the interest rate is a valid positive number.
while rate <= 0:
    rate = float(input("Enter the annual interest rate (in %): "))
    if rate <= 0:
        print("Interest rate must be greater than zero.")

# Prompt until the time period is a valid positive number of years.
while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time must be greater than zero.")

# Calculate compound interest.
total = principal * pow((1 + rate / 100), time)

# Output the result, formatted to two decimal places.
print(f"The balance after {time} year/s is: {total:.2f}€.")
