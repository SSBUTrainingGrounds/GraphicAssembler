import os

from PyQt6.QtWidgets import QComboBox

from graphics.utils.definitions import RENDERS_DIR
from graphics.utils.types import PlayerData


def get_characters() -> list[str]:
    return [f.name for f in os.scandir(RENDERS_DIR) if f.is_dir()]


class CharacterDropdown(QComboBox):
    def __init__(self, player_data: PlayerData) -> None:
        super().__init__()

        self.player_data = player_data
        self.addItems(get_characters())
        self.setCurrentText(player_data["character"])
        self.currentTextChanged.connect(self.get_selection)

    def get_selection(self, text: str) -> None:
        self.player_data["character"] = text
