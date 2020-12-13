"""Module provides hook-in for the CLI class.
"""

# Import C
import cthulhu_cmd.cli as cli


if __name__ == "__main__":
    cmd = cli.CthulhuCmd()
    cmd.cmdloop()