# Format specifiers {:flags} format a value based on the inserted flags.
num1 = 6.785675
num2 = 12.333
num3 = -234.234

num11 = 10006.785675
num21 = 100012.333
num31 = -1000234.234

# :.nf formats the number to n decimal places (fixed-point notation).
print(f"{num1:.3f}")
print(f"{num2:.3f}")
print(f"{num3:.3f}")


# :n reserves a total width of n characters for the output.
# If the number is shorter, spaces are added in front (right-aligned by default).
print(f"{num1:9}")
print(f"{num2:9}")
print(f"{num3:9}")

# :0n reserves a width of n characters and pads with leading zeros.
print(f"{num1:09}")
print(f"{num2:09}")
print(f"{num3:09}")

# :<n left-aligns the output in a field of n characters.
# Extra spaces appear after the number.
print(f"{num1:<9}")
print(f"{num2:<9}")
print(f"{num3:<9}")

# :>n right-aligns the output (default).
# Extra spaces appear before the number.
print(f"{num1:>9}")
print(f"{num2:>9}")
print(f"{num3:>9}")

# :^n centers the output in a field of n characters.
# Spaces are distributed evenly around the number.
print(f"{num1:^20}")
print(f"{num2:^20}")
print(f"{num3:^20}")

# :+ always displays the sign, even for positive numbers.
print(f"{num1:+}")
print(f"{num2:+}")
print(f"{num3:+}")

# :(space) adds a leading space for positive numbers (instead of a +),
# but still shows - for neagtives. Useful for aligning values by sign.
print(f"{num1: }")
print(f"{num2: }")
print(f"{num3: }")

# :, adds a comma as a thousands seperator.
print(f"{num11:,}")
print(f"{num21:,}")
print(f"{num31:,}")

# :,.2f combines comma seperator and fixed-point formatting to 2 decimal places.
print(f"{num11:,.2f}")
print(f"{num21:,.2f}")
print(f"{num31:,.2f}")

example = 123456789
# Example with all format options in the right order combined:

# {[variable]:[alignment][sign][#][0][width][,][.precision][type]}
print(f"{example:^+020,.2f}")

# All Smart Zebras Stay Properly Typed
# Alignment-Sign-Zero/Width-Seperator(comma)-Precision-Type
