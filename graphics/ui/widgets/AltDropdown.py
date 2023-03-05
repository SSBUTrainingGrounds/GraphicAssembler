from PyQt6.QtWidgets import QComboBox

from graphics.utils.types import PlayerData


class AltDropdown(QComboBox):
    def __init__(self, player_data: PlayerData) -> None:
        super().__init__()
        self.player_data = player_data
        self.addItems(["01", "02", "03", "04", "05", "06", "07", "08"])
        self.player_data["alt"] = self.currentText()
        self.currentTextChanged.connect(self.get_selection)

    def get_selection(self, text: str) -> None:
        self.player_data["alt"] = text

    def reset(self) -> None:
        self.setCurrentText("01")
