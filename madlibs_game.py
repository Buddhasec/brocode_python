# A Madlibs game is a word game where you create a story
# by filling in blanks with random words provided by the user.

# The first block collects the user input.
noun1 = input("Please enter a noun (person, place, thing): ")
adjective1 = input("Please enter an adjective (description): ")
verb1 = input("Please enter a verb (action): ")
noun2 = input("Please enter another noun (person, place, thing): ")
number1 = int(input("Please enter a number (1-9): "))
adjective2 = input("Please enter a different adjective :(description) ")
adjective3 = input("Please enter one more adjective (description): ")

# The second block prints the story using f-strings.
print(f"I am afraid of {noun1}, because {noun1} is very {adjective1}!")
print(f"I tried to {verb1}, but because of {noun2} my chances of {verb1}ing were close to {number1}.")
print(f"Once I {verb1}ed fast enough, I left both {noun1} and {noun2} behind. The {adjective1} couldn't hold me back.")
print(f"In the end {adjective1} is just inferior to {adjective2}, no matter how {adjective3} the situation may seem.")

