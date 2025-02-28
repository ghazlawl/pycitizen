import json


class Commodities:
    data = []
    filename = "commodities.json"

    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(f"files/{self.filename}", "r") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f'The file "{self.filename}" does not exist.')
            return None
        except json.JSONDecodeError:
            print(f'The file "{self.filename}" is not a valid JSON file.')
            return None

    def _get_x_by_y(self, x, y, value):
        if x != "symbol" and x != "name":
            return False

        results = [item[x] for item in self.data if item[y] == value]

        if len(results) > 0:
            return results[0]

        return False

    def get_symbol_by_name(self, name):
        return self._get_x_by_y("symbol", "name", name)

    def get_name_by_symbol(self, symbol):
        return self._get_x_by_y("name", "symbol", symbol)
