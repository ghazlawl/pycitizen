import os

from dotenv import load_dotenv

# Load the environment vars.
load_dotenv()

# Get the console width (default to 100).
CONSOLE_WIDTH = int(os.getenv("CONSOLE_WIDTH")) or 100


class bcolors:
    RED = "\33[91m"
    BLUE = "\33[94m"
    GREEN = "\033[32m"
    YELLOW = "\033[93m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[36m"
    END = "\033[0m"


def print_logo():
    """
    Prints the logo.

    See: https://patorjk.com/software/taag/#p=testall&v=0&f=ANSI%20Regular&t=PyCitizen
    """
    print()
    print(" ██▓███ ▓██   ██▓ ▄████▄   ██▓▄▄▄█████▓ ██▓▒███████▒▓█████  ███▄    █ ")
    print("▓██░  ██▒▒██  ██▒▒██▀ ▀█  ▓██▒▓  ██▒ ▓▒▓██▒▒ ▒ ▒ ▄▀░▓█   ▀  ██ ▀█   █ ")
    print("▓██░ ██▓▒ ▒██ ██░▒▓█    ▄ ▒██▒▒ ▓██░ ▒░▒██▒░ ▒ ▄▀▒░ ▒███   ▓██  ▀█ ██▒")
    print("▒██▄█▓▒ ▒ ░ ▐██▓░▒▓▓▄ ▄██▒░██░░ ▓██▓ ░ ░██░  ▄▀▒   ░▒▓█  ▄ ▓██▒  ▐▌██▒")
    print("▒██▒ ░  ░ ░ ██▒▓░▒ ▓███▀ ░░██░  ▒██▒ ░ ░██░▒███████▒░▒████▒▒██░   ▓██░")
    print("▒▓▒░ ░  ░  ██▒▒▒ ░ ░▒ ▒  ░░▓    ▒ ░░   ░▓  ░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒░   ▒ ▒ ")
    print("░▒ ░     ▓██ ░▒░   ░  ▒    ▒ ░    ░     ▒ ░░░▒ ▒ ░ ▒ ░ ░  ░░ ░░   ░ ▒░")
    print("░░       ▒ ▒ ░░  ░         ▒ ░  ░       ▒ ░░ ░ ░ ░ ░   ░      ░   ░ ░ ")
    print("         ░ ░     ░ ░       ░            ░    ░ ░       ░  ░         ░ ")
    print("         ░ ░     ░                         ░                          ")
    print()


def print_top_line():
    """
    Prints a top line.

    See: https://theasciicode.com.ar/extended-ascii-code/box-drawing-character-single-line-lower-left-corner-ascii-code-192.html
    """
    print("+" + ("-" * (CONSOLE_WIDTH - 2)) + "+")


def print_middle_line():
    """
    Prints a middle line.
    """
    print("+" + ("-" * (CONSOLE_WIDTH - 2)) + "+")


def print_bottom_line():
    """
    Prints a bottom line.
    """
    print("+" + ("-" * (CONSOLE_WIDTH - 2)) + "+")


def print_line(text):
    """
    Prints a line of text.

    Arguments:
      text - The text to print.
    """
    print(
        "|",
        "{value:{width}}".format(value=text, width=(CONSOLE_WIDTH - 4)),
        "|",
    )


def print_breadcrumbs(menu_tree):
    """
    Prints the specified menu tree in the format: "You are here: X > Y > Z". For
    example, the menu tree "ships/view" will be printed as "Ships > View".

    Arguments:
      menu_tree (str) - The menu tree. Example: ships/view
    """
    split_words = menu_tree.split("/")
    capitalized_words = [word.capitalize() for word in split_words]

    print("You are here:", " > ".join(capitalized_words))


def print_success(text):
    print(f"{bcolors.GREEN}{text}{bcolors.END}")


def print_status(text):
    print(f"{bcolors.YELLOW}{text}{bcolors.END}")
