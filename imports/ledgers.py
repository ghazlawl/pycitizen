import json
import math
import os

from datetime import datetime
from dotenv import load_dotenv
from prettytable.colortable import ColorTable, Themes

from imports.commodities import Commodities

# Load the environment vars.
load_dotenv()

# Get the console width (default to 100).
CONSOLE_WIDTH = int(os.getenv("CONSOLE_WIDTH")) or 100


class Ledger:
    data = None
    filename = "unknown.json"

    def __init__(self, filename):
        self.filename = filename

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

    def save_data(self):
        try:
            with open("files/" + self.filename, "w") as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            print(f"An error occurred: {e}")


class SalvageLedger(Ledger):
    commodities_obj = Commodities()

    # @todo Store this in the salvage.json file.
    current_station_values = [
        {"material": "Recycled Material Composite", "amount": 1.2},
        {"material": "Construction Materials", "amount": 2.3},
    ]

    def __init__(self):
        super().__init__("salvage.json")
        self.data = self.load_data()

    def add_activity(
        self,
        date: str,
        cost: int,
        what: str,
        amount_rmc: float,
        amount_cmt: float,
        cargo: str,
    ):
        # Hold the final list of cargo.
        final_cargo_list = [
            {
                "commodity": "Recycled Material Composite",
                "amount": amount_rmc,
            },
            {
                "commodity": "Construction Materials",
                "amount": amount_cmt,
            },
        ]

        # Split the input cargo into an array.
        # e.g., "2 Gold, 4 Iron" becomes a list of ['2 Gold', '4 Iron'].
        input_cargo_list = cargo.strip().split(",")

        for item in input_cargo_list:
            # Split by space to separate the quantity and the commodity.
            values = item.strip().split()

            if len(values) < 2:
                continue

            # Unpack the quantity and commodity from the values.
            quantity, commodity = values

            # Create a dictionary for each commodity.
            commodity_object = {
                "commodity": commodity.strip(),
                "amount": int(quantity.strip()),
            }

            # Add the commodity to the final cargo list.
            final_cargo_list.append(commodity_object)

        # Format the row.
        row = {
            "date": date,
            "cost": cost,
            "object": what.strip(),
            "commodities": final_cargo_list,
        }

        # Append the row and save.
        self.data["activity"].append(row)
        self.save_data()

    def set_current_station_value(self, material_to_update, new_amount):
        for item in self.current_station_values:
            if item["material"] == material_to_update:
                item["amount"] = new_amount
                return

    def get_current_station_value(self, material_to_find):
        """
        Gets the amount of the specified material that is in the filler station.

        Arguments:
            material (str) - The material ("RMC", "CMT", etc).
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

    def _get_commodity_amount(self, row, commodity):
        """
        Gets the amount of the specified commodity from the specified row.
        """
        amount = next(
            float(item["amount"])
            for item in row["commodities"]
            if item["commodity"] == commodity
        )

        return amount

    def _get_commodity_sell_price(self, commodity):
        price = next(
            float(item["price"])
            for item in self.data["optimal_sell_prices"]
            if item["commodity"] == commodity
        )

        return price

    def _get_cargo(self, row):
        data = [
            item
            for item in row["commodities"]
            if item["commodity"] != "Recycled Material Composite"
            and item["commodity"] != "Construction Materials"
        ]

        sorted_data = sorted(data, key=lambda x: x["commodity"])

        return sorted_data

    def _get_cargo_sell_price(self, cargo):
        total_price = 0

        for item in cargo:
            sell_price = self._get_commodity_sell_price(item["commodity"])

            if sell_price:
                total_price += sell_price * item["amount"]

        return total_price

    def print_activity_table(self):
        table = ColorTable(theme=Themes.LAVENDER)
        table.min_table_width = CONSOLE_WIDTH
        table.align = "l"

        table.field_names = [
            "Date",
            "Cost",
            "Object",
            "RMC",
            "RMC Profit",
            "CMT",
            "CMT Profit",
            "Cargo",
            "Cargo Profit",
            "Total Profit",
        ]

        table_rows = []

        for index, row in enumerate(self.data["activity"]):
            # Get the sell price of RMC.
            rmc_optimal_sell_price = self._get_commodity_sell_price(
                "Recycled Material Composite"
            )

            # Extract the amount of RMC and calculate the profit.
            rmc_scu = self._get_commodity_amount(row, "Recycled Material Composite")
            rmc_profit = math.floor(rmc_scu * rmc_optimal_sell_price)

            # Get the sell price of CMT.
            cmt_optimal_sell_price = self._get_commodity_sell_price(
                "Construction Materials"
            )

            # Extract the amount of CMT and calculate the profit.
            cmt_scu = self._get_commodity_amount(row, "Construction Materials")
            cmt_profit = math.floor(cmt_scu * cmt_optimal_sell_price)

            # Extract the cargo.
            # Cargo is any commodity in the row that isn't RMC or CMT.
            cargo = self._get_cargo(row)

            # Format the cargo manifest.
            cargo_manifest = [
                f"{self.commodities_obj.get_symbol_by_name(item['commodity'])} ({item['amount']})"
                for item in cargo
            ]

            # Calculate the cargo profit.
            cargo_profit = math.floor(self._get_cargo_sell_price(cargo))

            # Calculate the total profit.
            total_profit = rmc_profit + cmt_profit + cargo_profit

            # Subtract the initial cost, if any.
            if row["cost"] > 0:
                total_profit -= row["cost"]

            total_profit = math.floor(total_profit)

            table_rows.append(
                [
                    row["date"],
                    f"{row['cost']:,} UEC",
                    row["object"],
                    f"{rmc_scu:,.2f} SCU",
                    f"{rmc_profit:,} UEC",
                    f"{cmt_scu:,.2f} SCU",
                    f"{cmt_profit:,} UEC",
                    ", ".join(cargo_manifest) if len(cargo_manifest) > 0 else "-",
                    f"{cargo_profit:,} UEC",
                    f"{total_profit:,} UEC",
                ]
            )

        # Sort the table rows by date, assuming the date is in MM/DD/YY format.
        sorted_table_rows = sorted(
            table_rows, key=lambda x: datetime.strptime(x[0], "%m/%d/%y")
        )

        table.add_rows(sorted_table_rows)

        print(table)


class MiningLedger(Ledger):
    def __init__(self):
        super().__init__("mining-ledger.json")
