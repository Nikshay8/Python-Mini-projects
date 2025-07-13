'''
EXPLANATION

lines explained:-
print(f"You Chose {reverseDict[you]}")
print(f"Computer Chose {reverseDict[computer]}")


Exp:

These are formatted print statements (using f-strings in Python), used to display what the user and the computer chose — in words, not in numbers.

But right now, your and the computer's choices are stored as numbers:

Snake = 1

Water = -1

Gun = 0


The dictionary:
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

is used to convert:

1 → "Snake"

-1 → "Water"

0 → "Gun"


Let's say:

The user typed 's' (snake), so:
you = youDict["s"] = 1

The computer randomly chose -1, i.e., water:
computer = -1

Now, your code runs:
print(f"You Chose {reverseDict[you]}")
# reverseDict[1] = "Snake"
# Output: You Chose Snake


print(f"Computer Chose {reverseDict[computer]}")
# reverseDict[-1] = "Water"
# Output: Computer Chose Water

Why Use reverseDict?
Because internally you're using numbers (1, -1, 0) to compare who wins.
But you can't show the user:

You Chose 1
Computer Chose -1

That would be confusing. So, you convert numbers back into readable choices (Snake, Water, Gun) using reverseDict.

'''