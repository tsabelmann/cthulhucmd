"""Module provides utility functions that are useful in the context of the Cthulhu pen and paper game.
"""

# Import C
from colorama import Fore, Back


# Import R
import random


# Probe Message Computation
def probe_message(probe_value: int, die_value: int):
    if die_value == 1:
        return Back.GREEN + Fore.LIGHTWHITE_EX + "Critical success"
    elif die_value <= (probe_value // 5):
        return Fore.GREEN + "Extreme success"
    elif die_value <= (probe_value // 2):
        return Fore.GREEN + "Difficult success"
    elif die_value <= probe_value:
        return Fore.GREEN + "Regular success"
    else:
        if probe_value < 50:
            if die_value >= 96:
                return Back.RED + Fore.LIGHTWHITE_EX + "You are doomed!"
            else:
                return Fore.RED + "You have screwed up!"
        else:
            if die_value == 100:
                return Back.RED + Fore.LIGHTWHITE_EX + "You are doomed!"
            else:
                return Fore.RED + "You have screwed up!"


# Compute bonus
def compute_bonus(die_10: int, die_1: int, bonus_dice: int = 0):
    # Throw bonus_dice amount of bonus d10 dice
    dice = [random.randint(0, 9) * 10 for _ in range(bonus_dice)]

    # Compute dice value
    die_value = dice2value(die_10, die_1)

    # Decide if bonus is applicable
    if 0 <= die_value <= 10:
        return die_10, dice, False
    else:
        new_dice = [die_10, *dice]
        if 0 in new_dice and die_1 == 0:
            new_dice = [die for die in new_dice if die != 0]

        # Compute new 10 part
        new_die_10 = min(new_dice)

        if new_die_10 == die_10:
            return die_10, dice, False
        else:
            return new_die_10, dice, True


# Compute malus
def compute_malus(die_10: int, die_1: int, malus_dice: int = 0):
    # Throw malus_dice amount of malus d10 dice
    dice = [random.randint(0, 9) * 10 for _ in range(malus_dice)]

    # Decide based on die_1 if 100 can be created
    if die_1 == 0:
        if 0 in dice:
            new_die_10 = 0
        else:
            new_die_10 = max([die_10, *dice])
    else:
        new_die_10 = max([die_10, *dice])

    if new_die_10 == die_10:
        return die_10, dice, False
    else:
        return new_die_10, dice, True


def dice2value(die_10: int, die_1: int):
    if die_10 == 0 and die_1 == 0:
        return 100
    else:
        return die_10 + die_1


def value2dice(value):
    if value == 100:
        return 0, 0
    else:
        die_10 = (value // 10) * 10
        die_1 = value % 10
        return die_10, die_1
