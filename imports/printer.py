from imports.settings import Settings

my_bcolors = {
    "BLACK": "\033[30m",
    "RED": "\33[91m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[93m",
    "BLUE": "\33[94m",
    "PURPLE": "\033[0;35m",
    "CYAN": "\033[36m",
    "WHITE": "\033[37m",
    "END": "\033[0m",
    "GRAY": "\033[38;5;8m",
}

my_beffects = {
    "BOLD": "\033[1m",
    "UNDERLINE": "\033[4m",
    "BLINKING": "\033[5m",
    "REVERSED": "\033[7m",
    "Hidden": "\033[8m",
}

settings_obj = Settings()


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
    See: https://en.wikipedia.org/wiki/Box-drawing_characters
    """
    border_color = my_bcolors[settings_obj.get("border_color")]
    width = settings_obj.get("console_width")
    char1 = settings_obj.get("border_tl_junction_char")
    char2 = settings_obj.get("border_horizontal_char")
    char3 = settings_obj.get("border_tr_junction_char")

    print(f"{border_color}{char1}{char2 * (width - 2)}{char3}{my_bcolors['END']}")


def print_middle_line():
    """
    Prints a middle line.
    """
    border_color = my_bcolors[settings_obj.get("border_color")]
    width = settings_obj.get("console_width")
    char1 = settings_obj.get("border_l_junction_char")
    char2 = settings_obj.get("border_horizontal_char")
    char3 = settings_obj.get("border_r_junction_char")

    print(f"{border_color}{char1}{char2 * (width - 2)}{char3}{my_bcolors['END']}")


def print_bottom_line():
    """
    Prints a bottom line.
    """
    border_color = my_bcolors[settings_obj.get("border_color")]
    width = settings_obj.get("console_width")
    char1 = settings_obj.get("border_bl_junction_char")
    char2 = settings_obj.get("border_horizontal_char")
    char3 = settings_obj.get("border_br_junction_char")

    print(f"{border_color}{char1}{char2 * (width - 2)}{char3}{my_bcolors['END']}")


def print_line(text):
    """
    Prints a line of text.

    Arguments:
      text - The text to print.
    """
    border_color = my_bcolors[settings_obj.get("border_color")]
    width = settings_obj.get("console_width")
    text_color = my_bcolors[settings_obj.get("text_color")]
    char1 = settings_obj.get("border_vertical_char")

    print(
        f"{border_color}{char1}{my_bcolors['END']}",
        f"{text_color}{text:{(width - 4)}}{my_bcolors['END']}",
        f"{border_color}{char1}{my_bcolors['END']}",
    )


def print_success(text):
    print(f"{my_bcolors['GREEN']}{text}{my_bcolors['END']}")


def print_status(text):
    print(f"{my_bcolors['YELLOW']}{text}{my_bcolors['END']}")
