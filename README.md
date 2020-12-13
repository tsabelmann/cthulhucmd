# cthulhu_cmd
Command line tool that provides useful commands in the context of the pen and paper game **Cthulhu**.

## Installation

1. ```bash
   git clone https://github.com/tsabelmann/cthulhu_cmd
   ```
2. ```bash
   cd cthulhu_cmd
   ```
3. ```bash
   poetry install
   ```
4. ```bash
   poetry run cthulhu
   ```

## Usage
The **Cthulhu** command line tool, in form of a REPL, provides two commands: **roll** and **probe**. The **roll** command allows the throwing of dice and the subsequent summation and addition of optional values. The **probe** command allows the check of ones *ability* against **one** thrown <u>D100</u> with or without *additional* **bonus** or **malus** dice.

## Dice Syntax

A regular dice throw is specified by the *amount* of dice you want to throw and the *dice eyes*. The most common dice eyes are **100**, **20**, **12**, **10**, **8**, **6**, **4**, and **3**.

### Examples

- `1d100`
- `2D100`
- `1w20`
- `3W10`
- `1d8`
- `6D6`
- `1W4`
- `2w3`

### Disclaimer
The letters **w** and **W** can be used as a shortcut because the german word for die or dice is Würfel.

## Value Syntax

Values to be added to the final sum consists of a *sign*, and a *value* part.

### Examples

- `+2`
- `-3`

## Examples

- `roll 1d100`
- `roll 2d100 1d10 1d8 1d6 1d4 1d3`
- `roll 1d20 +3`
- `roll 1d20 +1+2+3`
- `probe 50 \\ neither bonus nor malus is applied`
- `probe 50 b 1`
- `probe 50 B 1`
- `probe 50 bonus 1`
- `probe 50 m 1`
- `probe 50 M 1`
- `probe 50 malus 1`
- `probe 50b1`
- `probe 50B1`
- `probe 50 b1`
- `probe 50B 1`
- `probe 50 BOnUs 1`
- `probe 50m1`
- `probe 50M1`
- `probe 50 m1`
- `probe 50M 1`
- `probe 50 MAlUs 1`

## Acknowledgement
The command line tool requires the installation of `Poetry`.