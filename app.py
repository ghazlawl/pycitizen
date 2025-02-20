from dotenv import load_dotenv
from prettytable.colortable import ColorTable, Themes

import os
import imports.print_utils as print_utils

# Load the environment vars.
load_dotenv()

# Get the console width (default to 100).
CONSOLE_WIDTH = int(os.getenv("CONSOLE_WIDTH")) or 100

first_time_home = True
first_time_hangar = True


# Holds the current menu tree. Example values might be:
# - hangar
# - hangar/add
# - hangar/remove
# - admin
current_menu_tree = "home"

my_ships = [
    {
        "manufacturer": "DRAKE Interplanetary",
        "name": "Cutlass Black Best In Show Edition 2949",
        "crew": "1-2",
        "cargo": "46",
    },
    {
        "manufacturer": "Origin Jumpworks",
        "name": "400i",
        "crew": "1-3",
        "cargo": "42",
    },
]


def get_user_selection():
    user_input = input("Selection: ")
    return user_input


def print_my_ships_table():
    table = ColorTable(theme=Themes.LAVENDER)
    table.min_table_width = CONSOLE_WIDTH
    table.align = "l"

    table.field_names = ["ID", "Manufacturer", "Name", "Crew", "Cargo"]

    table_rows = []

    for index, ship in enumerate(my_ships):
        table_rows.append(
            [
                index + 1,
                ship["manufacturer"],
                ship["name"],
                ship["crew"],
                ship["cargo"],
            ]
        )

    table.add_rows(table_rows)

    print(table)


waiting_for_input = True

print_utils.print_logo()

while waiting_for_input:
    if current_menu_tree == "home":
        print()

        if first_time_home:
            print_utils.print_status(
                "You wake up in your hab on ARC-L4 Faint Glen Station."
            )
        else:
            print_utils.print_status("You return to your hab.")

        first_time_home = False

        print()
        print_utils.print_top_line()
        print_utils.print_line("What would you like to do?")
        print_utils.print_middle_line()
        print_utils.print_line("1: Walk to the admin office.")
        print_utils.print_line("2: Take the elevator to your hangar.")
        print_utils.print_line("3: Open your log book.")
        print_utils.print_line("q: Quit")
        print_utils.print_bottom_line()

        user_selection = get_user_selection()

        if user_selection == "q":
            waiting_for_input = False

        if user_selection == "2":
            current_menu_tree = "hangar"

    if current_menu_tree == "hangar":
        print()

        if first_time_hangar:
            print_utils.print_status("You take the elevator to your hangar.")
        else:
            print_utils.print_status("You return to your hangar.")

        first_time_hangar = False

        print()
        print_utils.print_top_line()
        print_utils.print_line("What would you like to do?")
        print_utils.print_middle_line()
        print_utils.print_line("1: View your ships in the ASOP terminal.")
        print_utils.print_line("2: Add a ship to your inventory.")
        print_utils.print_line("3: Remove a ship from your inventory.")
        print_utils.print_line("b: Back")
        print_utils.print_bottom_line()

        user_selection = get_user_selection()

        if user_selection == "b":
            current_menu_tree = "home"

        if user_selection == "1":
            print()
            print_utils.print_status(
                "You use the ASOP terminal to view your list of ships."
            )
            print()
            print_my_ships_table()

        if user_selection == "2":
            current_menu_tree = "hangar/add"

    if current_menu_tree == "hangar/add":
        print()

        ship_manufacturer = (
            input("Ship Manufacturer [DRAKE Interplanetary]: ")
            or "DRAKE Interplanetary"
        )
        ship_name = input("Ship Name [Cutter]: ") or "Cutter"
        ship_crew = input("Ship Crew [1]: ") or "1"
        ship_cargo = input("Ship Cargo (SCU) [0]: ") or "0"

        my_ships.append(
            {
                "manufacturer": ship_manufacturer,
                "name": ship_name,
                "crew": ship_crew,
                "cargo": ship_cargo,
            }
        )

        print()
        print_utils.print_success("Ship added to your inventory!")

        current_menu_tree = "hangar"
