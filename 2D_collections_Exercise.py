# We want to create a numpad. Since a tuple is ordered and immutable,
# and we don't need to change or duplicate the values, it's a good fit.

num_pad = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9),
          ("*", 0, "#"),

)
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
