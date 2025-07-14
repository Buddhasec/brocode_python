# Logical operators evaluate multiple conditions at once: (or, and, not)
# The "or" operator returns True if at least one condition is True.

# Set the current temperature and rain condition.
temp = 36
is_raining = False

# if the temperature is too high, too low, or it is raining we cancel the event.
if (temp > 35 or temp < 12 or is_raining):
    print("The outdoor event is cancelled.")

# Otherwise, all conditions are fine the event goes on.
else:
    print("The outdoor event is still scheduled.")




# For the "and"-operator, both conditions have to be True.
temp = 20
is_sunny = True

# if the temperature is above 19 AND the sun is shining, we have a party.
if temp > 19 and is_sunny:
    print("The party is scheduled.")

# Otherwise, one condition is not met, the party is cancelled.
else:
    print("The party is cancelled.")




# The "not" operator inverts the Boolean value: True becomes Fals and vice versa.
temp = 24
is_windy = False

# If the temperature is 25 or below and it's not windy, the party can still be held.
if temp <= 25 and not is_windy:
    print("The party can still be held.")
else:
    print("The party is cancelled.")
