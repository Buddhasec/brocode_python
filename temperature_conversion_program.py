# Ask the user for the unit of the temperature: Celsius or Fahrenheit.
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")

# Ask the user for the temperature value and convert it to a float.
temp = float(input("Enter the temperature: "))

# If the unit is Celsius and exactly "C", convert to Fahrenheit:
if unit == "C":
    temp = 9 * temp / 5 + 32
    print(f"The temperature conversion is: {temp:.1f}°F")

# If the unit is Fahrenheit and exactly "F", convert to Celsius:
elif unit == "F":
    temp = (temp - 32) * 5 / 9
    print(f" The temperature conversion is: {temp:.1f}°C")

# If the input is neither exactly "C" nor "F", return an error:
else:
    print(f"{temp}' is not a valid unit. Pleaser enter 'C' or 'F'.")
