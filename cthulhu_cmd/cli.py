"""Module provides CLI class.
"""

# Import C
import cmd
from colorama import Fore, Style, init as colorama_init
from cthulhu_cmd.utils import *

# Import R
import re
import random

# Colorama
colorama_init(autoreset=True)


class CthulhuCmd(cmd.Cmd):
    """A CLI for the Cthulhu dice throwing."""

    prompt = 'cthulhu> '
    intro = ""

    __dice_regex__ = re.compile(
        r'(?P<dice>(\s*\+?\s*([1-9][0-9]{0,2})([dDwW])([1-9][0-9]*))+)\s*(?P<values>(\s*([+\-])\s*[0-9]{1,2})*\s*)'
    )

    __die_regex__ = re.compile(
        r"\s*(?P<die>[1-9][0-9]{0,2})([dDwW])(?P<value>([1-9][0-9]*))\s*"
    )

    __calculus_regex__ = re.compile(
        r'\s*((?P<sign>([+\-]))\s*(?P<value>[0-9]{1,2}))\s*'
    )

    __probe_regex__ = re.compile(
        r'\s*(?P<probe>[0-9]{1,3})'
        r'(\s*(?P<id>[mM]|[bB]|[bB][oO][nN][uU][sS]|[mM][aA][lL][uU][sS])\s*(?P<value>[0-9]{1,2}))?'
        r'\s*'
    )

    __bonus_malus_regex__ = re.compile(
        r'\s*(?P<value>([0-9]{1,2}))\s*'
    )

    def __init__(self):
        super(CthulhuCmd, self).__init__()

    def do_probe(self, message):
        match = self.__probe_regex__.search(message)

        if match:
            # Compute transmitted probe (ability) value
            probe_value = match.group("probe")
            probe_value = int(probe_value)

            # Throw 1d10 as tens unit
            die_10 = random.randint(0, 9) * 10

            # Throw 1d10
            die_1 = random.randint(0, 9)

            # Bonus / Malus computation
            if match.group("id") and match.group("id").lower() in ["b", "bonus"]:
                # Get amount of bonus dice
                bonus_dice = match.group("value")
                bonus_dice = int(bonus_dice)

                # Compute bonus
                new_die_10, dice, applied = compute_bonus(die_10, die_1, bonus_dice)

                # Compute die_value
                die_value = dice2value(new_die_10, die_1)

                # Probe message
                probe_mess = probe_message(probe_value, die_value)

                if applied:
                    # Compute index in dice that holds the die_10 value
                    index = dice.index(new_die_10)

                    # Compute new dice string
                    lst = [f"{Style.BRIGHT}{die:02d}{Style.NORMAL}"
                           if i == index else f"{die:02d}" for i, die in enumerate(dice)]
                    dice_str = f"[{', '.join(lst)}]"

                    # Print message
                    print(f"\tRoll: [{die_10:02d}][{Style.BRIGHT}{die_1}{Style.NORMAL}] "
                          f"Ability: {Style.BRIGHT}{probe_value}{Style.NORMAL}")
                    print(f"\tBonus: {dice_str}")
                    print(f"\tResult: {Style.BRIGHT}{die_value}")
                    print(f"\t{Style.BRIGHT}{probe_mess}")

                else:
                    # Compute new dice string
                    lst = [f"{die:02d}" for die in dice]
                    dice_str = f"[{', '.join(lst)}]"

                    # Print message
                    print(f"\tRoll: [{Style.BRIGHT}{die_10:02d}{Style.NORMAL}][{Style.BRIGHT}{die_1}{Style.NORMAL}] "
                          f"Ability: {Style.BRIGHT}{probe_value}{Style.NORMAL}")
                    print(f"\tBonus: {dice_str}")
                    print(f"\tResult: {Style.BRIGHT}{die_value}")
                    print(f"\t{Style.BRIGHT}{probe_mess}")

            elif match.group("id") and match.group("id").lower() in ["m", "malus"]:
                # Get amount of bonus dice
                malus_dice = match.group("value")
                malus_dice = int(malus_dice)

                # Compute malus
                new_die_10, dice, applied = compute_malus(die_10, die_1, malus_dice)

                # Compute die_value
                die_value = dice2value(new_die_10, die_1)

                # Probe message
                probe_mess = probe_message(probe_value, die_value)

                if applied:
                    # Compute index in dice that holds the die_10 value
                    index = dice.index(new_die_10)

                    # Compute new dice string
                    lst = [f"{Style.BRIGHT}{die:02d}{Style.NORMAL}"
                           if i == index else f"{die:02d}" for i, die in enumerate(dice)]
                    dice_str = f"[{', '.join(lst)}]"

                    # Print message
                    print(f"\tRoll: [{die_10:02d}][{Style.BRIGHT}{die_1}{Style.NORMAL}] "
                          f"Ability: {Style.BRIGHT}{probe_value}{Style.NORMAL}")
                    print(f"\tMalus: {dice_str}")
                    print(f"\tResult: {Style.BRIGHT}{die_value}")
                    print(f"\t{Style.BRIGHT}{probe_mess}")

                else:
                    # Compute new dice string
                    lst = [f"{die:02d}" for die in dice]
                    dice_str = f"[{', '.join(lst)}]"

                    # Print message
                    print(f"\tRoll: [{Style.BRIGHT}{die_10:02d}{Style.NORMAL}][{Style.BRIGHT}{die_1}{Style.NORMAL}] "
                          f"Ability: {Style.BRIGHT}{probe_value}{Style.NORMAL}")
                    print(f"\tMalus: {dice_str}")
                    print(f"\tResult: {Style.BRIGHT}{die_value}")
                    print(f"\t{Style.BRIGHT}{probe_mess}")

            else:
                # Compute die value
                die_value = dice2value(die_10, die_1)

                # Probe message
                probe_mess = probe_message(probe_value, die_value)

                # Print message
                print(f"\tRoll: [{Style.BRIGHT}{die_10:02d}{Style.NORMAL}][{Style.BRIGHT}{die_1}{Style.NORMAL}] "
                      f"Ability: {Style.BRIGHT}{probe_value}")
                print(f"\tResult: {Style.BRIGHT}{die_value}")
                print(f"\t{probe_mess}")

        else:
            print()

    def do_roll(self, message):
        match = self.__dice_regex__.search(message)

        if match:
            rng_numbers = []
            for m in self.__die_regex__.finditer(match.group("dice")):
                dice = m.group("die")
                dice = int(dice)

                value = m.group("value")
                value = int(value)

                rng_numbers.append([random.randint(1, value) for _ in range(dice)])

            rng_sum = sum([sum(rng) for rng in rng_numbers])

            # Change sum
            additions = []
            for m in self.__calculus_regex__.finditer(match.group("values")):
                group = m.groupdict()
                sign = group["sign"]

                calc_value = group["value"]
                calc_value = int(calc_value)

                if sign == "+":
                    additions.append(+calc_value)

                elif sign == "-":
                    additions.append(+calc_value)

            # Add additional values to sum
            add_sum = sum(additions)

            # Total sum
            total_sum = rng_sum + add_sum

            # Construct message
            print(f"\tRoll: {''.join([str(rng) for rng in rng_numbers])}")
            print(f"\tSum: {Style.BRIGHT}{rng_sum}")
            print(f"\tAdditions: {additions}")
            print(f"\tSum: {Style.BRIGHT}{add_sum}")
            print(f"\tResult: {Style.BRIGHT}{total_sum}")

        else:
            print()

    @staticmethod
    def postloop() -> None:
        """Appends newline character after end of the loop"""
        print("\n")

    @staticmethod
    def do_exit(_arg=None):
        """Performs the "exit" command."""
        return True

    @staticmethod
    def help_exit():
        """Shows help for the "exit" command."""
        print("Exits the application. Shorthand: x, q, or Ctrl-D.")

    do_EOF = do_exit
    help_EOF = help_exit


def main():
    CthulhuCmd().cmdloop()
