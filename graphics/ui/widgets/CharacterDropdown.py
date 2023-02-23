import os
from PyQt6.QtWidgets import QComboBox
from graphics.definitions import RENDERS_DIR


def get_characters() -> list[str]:
    return [f.name for f in os.scandir(RENDERS_DIR) if f.is_dir()]


class CharacterDropdown(QComboBox):
    def __init__(self):
        super().__init__()

        self.addItems(get_characters())
