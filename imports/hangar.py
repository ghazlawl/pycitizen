import json
import os

from dotenv import load_dotenv
from prettytable.colortable import ColorTable, Themes

# Load the environment vars.
load_dotenv()

# Get the console width (default to 100).
CONSOLE_WIDTH = int(os.getenv("CONSOLE_WIDTH")) or 100


def load_my_ships():
    filename = "ships.json"

    try:
        with open("files/" + filename, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f'The file "{filename}" does not exist.')
        return None
    except json.JSONDecodeError:
        print(f'The file "{filename}" is not a valid JSON file.')
        return None


def save_my_ships(data):
    filename = "ships.json"

    try:
        with open("files/" + filename, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"An error occurred: {e}")


def print_my_ships_table(ships):
    table = ColorTable(theme=Themes.LAVENDER)
    table.min_table_width = CONSOLE_WIDTH
    table.align = "l"

    table.field_names = ["ID", "Manufacturer", "Name", "Crew", "Cargo (SCU)"]

    table_rows = []

    for index, ship in enumerate(ships):
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
