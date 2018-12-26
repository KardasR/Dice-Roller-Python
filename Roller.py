# Welcome to my program! I hope your having a good time so far,
# and that you will use this for all of your dice rolling needs.

# TODO: Find a way to make a GUI for this

# We're going to start this program off with some imports.
import random
import time

# Now we will start with the fun stuff, variables! Even though there's only one it's still fun.
result = 0


class Dice:
    d4 = 1, 2, 3, 4
    d6 = 1, 2, 3, 4, 5, 6
    d8 = 1, 2, 3, 4, 5, 6, 7, 8
    d10 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    d12 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    d20 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20


# Roll!
def roll():
    # First off, we have to ask the user what dice they would like to roll.
    sides = int(input("How many sides does the dice have that you are trying to roll? Numbers only please. \n"))
    print("Rolling!")
    # Loop to create suspense.
    time.sleep(0.5)
    for i in range(1, 4):
        print("Duh")
        time.sleep(0.5)

    # This is what will "roll" the dice
    if sides == 4:
        holder = random.choice(Dice.d4)
        print(holder)
    elif sides == 6:
        holder = random.choice(Dice.d6)
        print(holder)
    elif sides == 8:
        holder = random.choice(Dice.d8)
        print(holder)
    elif sides == 10:
        holder = random.choice(Dice.d10)
        print(holder)
    elif sides == 12:
        holder = random.choice(Dice.d12)
        print(holder)
    elif sides == 20:
        holder = random.choice(Dice.d20)
        checker(holder)
    elif sides == 100:
        holder = random.choice(Dice.d20)
        print(holder)
        holder = holder + random.choice(Dice.d20)
        print(holder)
        holder = holder + random.choice(Dice.d20)
        print(holder)
        holder = holder + random.choice(Dice.d20)
        print(holder)
        holder = holder + random.choice(Dice.d20)
        print(holder)
    else:
        print("Please enter a different number. ")


# Checks to see if the user rolled a critical.
def checker(holder):
    if holder == 1:
        print("Critical Fail!")
        print(holder)
    elif holder == 20:
        print("Critical Success!")
        print(holder)
    elif holder != 1 and holder != 20:
        print(holder)


def main():
    roll()
    answer = str(input("Would you like to roll again? (y/n) \n"))
    if answer == "y":
        main()
    else:
        print("Peace out boyscout!")


if __name__ == '__main__':
    main()

