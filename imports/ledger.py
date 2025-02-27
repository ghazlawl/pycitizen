import json
import os

from dotenv import load_dotenv
from prettytable.colortable import ColorTable, Themes

# Load the environment vars.
load_dotenv()

# Get the console width (default to 100).
CONSOLE_WIDTH = int(os.getenv("CONSOLE_WIDTH")) or 100


class Ledger:
    data = None

    filename = "unknown-ledger.json"

    def __init__(self, filename):
        self.filename = filename
        pass


class SalvageLedger(Ledger):
    current_station_values = [
        {"material": "Recycled Material Composite", "amount": 1.2},
        {"material": "Construction Materials", "amount": 2.3},
    ]

    def __init__(self):
        super().__init__("salvage-ledger.json")
        self.data = self.load_data()

    def load_data(self):
        try:
            with open("files/" + self.filename, "r") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f'The file "{self.filename}" does not exist.')
            return None
        except json.JSONDecodeError:
            print(f'The file "{self.filename}" is not a valid JSON file.')
            return None

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

    def print_station_values_table(self):
        table = ColorTable(theme=Themes.LAVENDER)
        table.min_table_width = CONSOLE_WIDTH
        table.align = "l"

        table.field_names = ["Material", "Amount (SCU)"]

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

    def print_activity_table(self):
        print(self.data["activity"])

        table = ColorTable(theme=Themes.LAVENDER)
        table.min_table_width = CONSOLE_WIDTH
        table.align = "l"

        table.field_names = [
            "Date",
            "Cost",
            "What",
            "RMC",
            "RMC Profit",
            "CMAT",
            "CMAT Profit",
            "Cargo",
            "Cargo Profit",
            "Total Profit",
        ]

        table_rows = []

        for index, value in enumerate(self.data["activity"]):
            # Extract the amount of RMC.
            rmc_scu = next(
                item["amount"]
                for item in value["commodities"]
                if item["commodity"] == "Recycled Material Composite"
            )

            # Extract the amount of CMAT.
            cmat_scu = next(
                item["amount"]
                for item in value["commodities"]
                if item["commodity"] == "Construction Materials"
            )

            table_rows.append(
                [
                    value["date"],
                    f"{value['cost']:,} UEC",
                    value["what"],
                    f"{rmc_scu:.2f} SCU",
                    "?",
                    f"{cmat_scu:.2f} SCU",
                    "?",
                    "?",
                    "?",
                    "?",
                ]
            )

        table.add_rows(table_rows)

        print(table)


class MiningLedger(Ledger):
    def __init__(self):
        super().__init__("mining-ledger.json")
