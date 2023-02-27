import os

from PyQt6.QtWidgets import QComboBox

from graphics.definitions import THUMBNAIL_DIR


def get_tournaments() -> list[str]:
    return [f.name for f in os.scandir(THUMBNAIL_DIR) if f.is_dir()]


class TournamentDropdown(QComboBox):
    def __init__(self, data):
        super().__init__()

        self.data = data
        self.addItems(get_tournaments())
        self.setCurrentText(data["tournament"])
        self.currentTextChanged.connect(self.get_selection)

    def get_selection(self, text):
        self.data["tournament"] = text
