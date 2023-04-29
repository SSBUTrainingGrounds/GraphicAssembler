from typing import Optional

from PyQt6.QtWidgets import QComboBox

from graphics.utils.Types import ThumbnailPlayer, Top8Player


class AltDropdown(QComboBox):
    def __init__(
            self,
            player_data: ThumbnailPlayer | Top8Player,
            character_type: Optional[str] = None,
    ) -> None:
        super().__init__()
        self.player_data = player_data

        self.character_type = character_type

        if not self.character_type:
            self.character_type = "character"

        self.addItems(["01", "02", "03", "04", "05", "06", "07", "08"])
        if f"{self.character_type}" in player_data:
            self.setCurrentText(player_data[f"{self.character_type}"]["alt"])  # type: ignore
        self.currentTextChanged.connect(self.get_selection)

    def get_selection(self, text: str) -> None:
        self.player_data[f"{self.character_type}"]["alt"] = text

    def reset(self) -> None:
        self.setCurrentText("01")
