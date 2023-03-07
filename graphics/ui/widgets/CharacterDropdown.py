import os
from typing import Optional

from PyQt6.QtWidgets import QComboBox

from graphics.utils.definitions import RENDERS_DIR
from graphics.utils.types import ThumbnailPlayer, Top8Player


def get_characters() -> list[str]:
    return ["None"] + [f.name for f in os.scandir(RENDERS_DIR) if f.is_dir()]


class CharacterDropdown(QComboBox):
    def __init__(
        self,
        player_data: ThumbnailPlayer | Top8Player,
        character_type: Optional[str] = None,
    ) -> None:
        super().__init__()

        self.character_type = character_type

        if not self.character_type:
            self.character_type = "character"

        self.player_data = player_data
        self.addItems(get_characters())
        self.setCurrentText(player_data[f"{self.character_type}"]["name"])  # type: ignore
        self.currentTextChanged.connect(self.get_selection)

    def get_selection(self, text: str) -> None:
        self.player_data[f"{self.character_type}"]["name"] = text
