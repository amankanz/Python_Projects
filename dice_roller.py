import random

# Python Dice Roller


# dice_art = {
#     1: """
#      -----
#     |     |
#     |  •  |
#     |     |
#      -----
#     """,
#     2: """
#      -----
#     | •   |
#     |     |
#     |   • |
#      -----
#     """,
#     3: """
#      -----
#     | •   |
#     |  •  |
#     |   • |
#      -----
#     """,
#     4: """
#      -----
#     | • • |
#     |     |
#     | • • |
#      -----
#     """,
#     5: """
#      -----
#     | • • |
#     |  •  |
#     | • • |
#      -----
#     """,
#     6: """
#      -----
#     | • • |
#     | • • |
#     | • • |
#      -----
#     """
# }

# unicode_digits = {
#     1: '\u0031',  # Unicode for '1'
#     2: '\u0032',  # Unicode for '2'
#     3: '\u0033',  # Unicode for '3'
#     4: '\u0034',  # Unicode for '4'
#     5: '\u0035',  # Unicode for '5'
#     6: '\u0036',  # Unicode for '6'
#     7: '\u0037',  # Unicode for '7'
# }

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
#  ● ┌ ─ ┐ │ └ ┘

# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"),
    2: ("┌─────────┐", 
        "│ ●       │", 
        "│         │", 
        "│       ● │", 
        "└─────────┘"),
    3: ("┌─────────┐", 
        "│ ●       │", 
        "│    ●    │", 
        "│       ● │", 
        "└─────────┘"),
    4: ("┌─────────┐", 
        "│ ●     ● │", 
        "│         │", 
        "│ ●     ● │", 
        "└─────────┘"),
    5: ("┌─────────┐", 
        "│ ●     ● │", 
        "│    ●    │", 
        "│ ●     ● │", 
        "└─────────┘"),
    6: ("┌─────────┐", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "└─────────┘")
    }

dice = []
total = 0
num_of_dice = int(input("How many dice, from 1 to 6?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line], end="")
#     print()


for die in dice:
    total += die 

print(dice)
print(total)



# Example of printing dice face 3
# print(dice_art[5])
