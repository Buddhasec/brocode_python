# To accurately calculate the area of the rectangle, we need to define the length
# and width. Since the user input comes as a string, we typecast it to float to
# allow decimal values.
length = float(input("Please enter the length (in meters): "))
width = float(input("Please enter a width (in meters): "))

# To perform the calculation, we multiply length and width and store the result
# as a new variable.
area = length * width

# We use an f-string to format the output.
# For the square meter symbol (²), you can press NumLock + Alt + 0178.S
print(f"The area is {area}m²!")
