# Logical operators = evaluate multiple conditions (or, and, not).
# or   = at least one condition must be True.
# and  = both conditions must be True.
# not  = inverts the condition (not False, not True).

# Example 1: Using 'or'
temp = 25
is_raining = False

# if one of these conditions is True, the entire statement is True.
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The outdoor event is still scheduled.")


# Example 2: Using 'and' and 'not'
# Set temperature and sunshine status.
temp = 27
is_sunny = False

# If it is SUNNY and HOT (28°C or more).
if temp >= 28 and is_sunny:
    print("It is HOT outside.")
    print("It is SUNNY.")

# If  it is SUNNY and freezing (0°C or below).
elif temp <= 0 and is_sunny:
    print("It is COLD outside.")
    print("It is SUNNY.")

# If it is SUNNY and in the mild range(between 0 and 28).
elif 0 < temp < 28 and is_sunny:
    print("It is WARM outside.")
    print("It is SUNNY.")

# Example 3: Inverting the Boolean
# If it is NOT SUNNY and HOT (28°C or more).
elif temp >= 28 and not is_sunny:
    print("It is HOT outside.")
    print("It is CLOUDY.")

# If  it is NOT SUNNY and freezing (0°C or below).
elif temp <= 0 and not is_sunny:
    print("It is COLD outside.")
    print("It is CLOUDY.")

# If it is NOT SUNNY and in the mild range(between 0 and 28).
elif 0 < temp < 28 and not is_sunny:
    print("It is WARM outside.")
    print("It is CLOUDY.")

