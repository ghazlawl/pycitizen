import os

from dotenv import load_dotenv
from prettytable.colortable import ColorTable, Themes

# Load the environment vars.
load_dotenv()

# Get the console width (default to 100).
CONSOLE_WIDTH = int(os.getenv("CONSOLE_WIDTH")) or 100


class Ledger:
    filename = "unknown-ledger.json"

    def __init__(self, filename):
        self.filename = filename
        pass


class SalvageLedger(Ledger):
    current_station_values = [
        {"material": "RMC", "amount": 1.2},
        {"material": "CMAT", "amount": 2.3},
    ]

    def __init__(self):
        super().__init__("salvage-ledger.json")

    def set_current_station_value(self, material_to_update, new_amount):
        for item in self.current_station_values:
            if item["material"] == material_to_update:
                item["amount"] = new_amount
                return

    def get_current_station_value(self, material_to_find):
        """
        Gets the amount of the specified material that is in the filler station.

        Arguments:
            material (str) - The material ("RMC", "CMAT", etc).
        """
        amount = next(
            (
                item["amount"]
                for item in self.current_station_values
                if item["material"] == material_to_find
            ),
            None,
        )

        return amount

    def print_station_values(self):
        table = ColorTable(theme=Themes.LAVENDER)
        table.min_table_width = CONSOLE_WIDTH
        table.align = "l"

        table.field_names = ["Material", "Amount"]

        table_rows = []

        for index, value in enumerate(self.current_station_values):
            table_rows.append(
                [
                    value["material"],
                    value["amount"],
                ]
            )

        table.add_rows(table_rows)

        print(table)


class MiningLedger(Ledger):
    def __init__(self):
        super().__init__("mining-ledger.json")
