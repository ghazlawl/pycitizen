from dotenv import load_dotenv
from imports.movement import Movement

import os
import imports.printer as printer
import imports.ships as ships


# Load the environment vars.
load_dotenv()

# Get the console width (default to 100).
CONSOLE_WIDTH = int(os.getenv("CONSOLE_WIDTH")) or 100

# The movement object handles moving between locations and status messages.
movement_obj = Movement()
movement_obj.set_breadcrumb("home")
movement_obj.set_next_message("You wake up in your hab on ARC-L4 Faint Glen Station.")

# TODO: Move this to ships.py and/or a Ship class.
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

waiting_for_input = True


def get_user_selection():
    user_input = input("Selection: ")
    return user_input


printer.print_logo()

while waiting_for_input:
    if movement_obj.get_breadcrumb() == "home":
        print()
        printer.print_status(movement_obj.get_message())
        print()
        printer.print_top_line()
        printer.print_line("What would you like to do?")
        printer.print_middle_line()
        printer.print_line("1: Walk to the admin office.")
        printer.print_line("2: Take the elevator to your hangar.")
        printer.print_line("3: Open your log book.")
        printer.print_line("q: Quit")
        printer.print_bottom_line()

        user_selection = get_user_selection()

        if user_selection == "q":
            waiting_for_input = False

        if user_selection == "2":
            movement_obj.set_breadcrumb("hangar")
            movement_obj.set_next_message("You take the elevator to your hangar.")

    if movement_obj.get_breadcrumb() == "hangar":
        print()
        printer.print_status(movement_obj.get_message())
        print()
        printer.print_top_line()
        printer.print_line("What would you like to do?")
        printer.print_middle_line()
        printer.print_line("1: View your ships in the ASOP terminal.")
        printer.print_line("2: Add a ship to your inventory.")
        printer.print_line("3: Remove a ship from your inventory.")
        printer.print_line("b: Back")
        printer.print_bottom_line()

        user_selection = get_user_selection()

        if user_selection == "b":
            movement_obj.set_breadcrumb("home")
            movement_obj.set_next_message("You return to your hab.")

        if user_selection == "1":
            print()
            printer.print_status(
                "You use the ship terminal to view your list of ships."
            )
            print()
            ships.print_my_ships_table(my_ships)

            movement_obj.set_next_message(
                "You power down the ship terminal. You are still in your hangar."
            )

        if user_selection == "2":
            movement_obj.set_breadcrumb("hangar/add")

    if movement_obj.get_breadcrumb() == "hangar/add":
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
        printer.print_success("Ship added to your inventory!")

        movement_obj.set_breadcrumb("hangar")
        movement_obj.set_next_message(
            "You are done adding a ship... Update this message..."
        )
