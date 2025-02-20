import os

from dotenv import load_dotenv
from prettytable.colortable import ColorTable, Themes

# Load the environment vars.
load_dotenv()

# Get the console width (default to 100).
CONSOLE_WIDTH = int(os.getenv("CONSOLE_WIDTH")) or 100


def print_my_ships_table(ships):
    table = ColorTable(theme=Themes.LAVENDER)
    table.min_table_width = CONSOLE_WIDTH
    table.align = "l"

    table.field_names = ["ID", "Manufacturer", "Name", "Crew", "Cargo"]

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
