from dotenv import load_dotenv
from imports.movement import Movement
from imports.ledger import SalvageLedger

import os
import imports.printer as printer
import imports.hangar as hangar


# Load the environment vars.
load_dotenv()

# Get the console width (default to 100).
CONSOLE_WIDTH = int(os.getenv("CONSOLE_WIDTH")) or 100

# The movement object handles moving between locations and status messages.
movement_obj = Movement()
movement_obj.set_breadcrumb("home")
movement_obj.set_next_message("You wake up in your hab on ARC-L4 Faint Glen Station.")

# The salvage ledger object handles salvage operations.
salvage_ledger_obj = SalvageLedger()

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
        printer.print_line("3: Open your ledger.")
        printer.print_line("q: Quit")
        printer.print_bottom_line()

        user_selection = get_user_selection()

        if user_selection == "q":
            waiting_for_input = False

        if user_selection == "2":
            movement_obj.set_breadcrumb("hangar")
            movement_obj.set_next_message("You take the elevator to your hangar.")

        if user_selection == "3":
            movement_obj.set_breadcrumb("ledger")
            movement_obj.set_next_message("You open your ledger.")

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

        if user_selection == "q":
            waiting_for_input = False

        if user_selection == "b":
            movement_obj.set_breadcrumb("home")
            movement_obj.set_next_message("You return to your hab.")

        if user_selection == "1":
            print()
            printer.print_status("You use the terminal to view your list of ships.")
            print()

            my_ships = hangar.load_my_ships()
            hangar.print_my_ships_table(my_ships)

            movement_obj.set_next_message(
                "You power down the terminal. You are still in your hangar."
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
        ship_cargo = int(input("Ship Cargo (SCU) [0]: ")) or 0

        my_ships = hangar.load_my_ships()

        my_ships.append(
            {
                "manufacturer": ship_manufacturer,
                "name": ship_name,
                "crew": ship_crew,
                "cargo": ship_cargo,
            }
        )

        hangar.save_my_ships(my_ships)

        print()
        printer.print_success("Ship added to your inventory!")

        movement_obj.set_breadcrumb("hangar")
        movement_obj.set_next_message(
            "You are done adding a ship... Update this message..."
        )

    if movement_obj.get_breadcrumb() == "ledger":
        print()
        printer.print_status(movement_obj.get_message())
        print()
        printer.print_top_line()
        printer.print_line("Which ledger would you like to view?")
        printer.print_middle_line()
        printer.print_line("1: Hauling")
        printer.print_line("2: Mining")
        printer.print_line("3: Salvage")
        printer.print_line("b: Back")
        printer.print_bottom_line()

        user_selection = get_user_selection()

        if user_selection == "q":
            waiting_for_input = False

        if user_selection == "b":
            movement_obj.set_breadcrumb("home")
            movement_obj.set_next_message("You return to your hab.")

        if user_selection == "3":
            movement_obj.set_breadcrumb("ledger/salvage")
            movement_obj.set_next_message(
                "You black out and wake up on your favorite salvage ship."
            )

    if movement_obj.get_breadcrumb() == "ledger/salvage":
        print()
        printer.print_status(movement_obj.get_message())
        print()
        printer.print_top_line()
        printer.print_line("What would you like to do?")
        printer.print_middle_line()
        printer.print_line("1: Check the filler station material levels.")
        printer.print_line("b: Back")
        printer.print_bottom_line()

        user_selection = get_user_selection()

        if user_selection == "q":
            waiting_for_input = False

        if user_selection == "b":
            movement_obj.set_breadcrumb("ledger")
            movement_obj.set_next_message("You black out and wake up back in your hab.")

        if user_selection == "1":
            print()
            printer.print_status(
                "You walk over to the filler station and check the levels."
            )
            print()

            salvage_ledger_obj.print_station_values()

            movement_obj.set_next_message(
                "You leave the station. You are still on your favorite salvage ship."
            )
