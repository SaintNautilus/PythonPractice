import random

dice = int(input("Input number of dice: "))
sides = int(input("Number of sides:"))


if (dice <= 0):
    print("Not Enough Dice!!! Please enter either 1 or 2 dice.")

elif (dice < 2):
    print("Too Many Dice!!! Please enter either 1 or 2 dice.")

else:
    print(f"There are {dice} dice with {sides} sides")


if (sides < 6):
    print("Not enough sides")
else:
    print(f"These are {sides} sides.")

def dice_roll(dice, sides):

    roll = []

    for i in (0, dice):
        face = random.randint(1, sides)
        roll.append(face)
    return roll

roll = dice_roll(dice, sides)

print(f"These are your rolls!!!! {roll}")