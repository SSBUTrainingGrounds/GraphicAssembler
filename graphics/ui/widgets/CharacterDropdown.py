import os

from PyQt6.QtWidgets import QComboBox

from graphics.definitions import RENDERS_DIR


def get_characters() -> list[str]:
    return [f.name for f in os.scandir(RENDERS_DIR) if f.is_dir()]


class CharacterDropdown(QComboBox):
    def __init__(self, player_data):
        super().__init__()

        self.player_data = player_data
        self.addItems(get_characters())
        self.setCurrentText(player_data["character"])
        self.currentTextChanged.connect(self.get_selection)

    def get_selection(self, text):
        self.player_data["character"] = text
