import os

from dotenv import load_dotenv

# Load the environment vars.
load_dotenv()


class Settings:
    settings = {
        "console_width": None,
        "text_color": None,
        "border_color": None,
        "border_horizontal_char": "-",
        "border_vertical_char": "|",
        "border_tl_junction_char": "+",
        "border_tr_junction_char": "+",
        "border_l_junction_char": "+",
        "border_r_junction_char": "+",
        "border_bl_junction_char": "+",
        "border_br_junction_char": "+",
    }

    def __init__(self):
        self.settings["console_width"] = int(os.getenv("CONSOLE_WIDTH")) or 100

        self.settings["text_color"] = os.getenv("TEXT_COLOR") or "WHITE"

        self.settings["border_color"] = os.getenv("BORDER_COLOR") or "WHITE"

        self.settings["border_horizontal_char"] = (
            os.getenv("BORDER_HORIZONTAL_CHAR") or "-"
        )

        self.settings["border_vertical_char"] = os.getenv("BORDER_VERTICAL_CHAR") or "|"

        self.settings["border_tl_junction_char"] = (
            os.getenv("BORDER_TL_JUNCTION_CHAR") or "+"
        )

        self.settings["border_tr_junction_char"] = (
            os.getenv("BORDER_TR_JUNCTION_CHAR") or "+"
        )

        self.settings["border_l_junction_char"] = (
            os.getenv("BORDER_L_JUNCTION_CHAR") or "+"
        )

        self.settings["border_r_junction_char"] = (
            os.getenv("BORDER_R_JUNCTION_CHAR") or "+"
        )

        self.settings["border_bl_junction_char"] = (
            os.getenv("BORDER_BL_JUNCTION_CHAR") or "+"
        )

        self.settings["border_br_junction_char"] = (
            os.getenv("BORDER_BR_JUNCTION_CHAR") or "+"
        )

    def get(self, setting):
        return self.settings.get(setting)
