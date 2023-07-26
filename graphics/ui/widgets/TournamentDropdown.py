import os

from PyQt6.QtWidgets import QComboBox

from graphics.utils.Definitions import TOP8_DIR
from graphics.utils.Types import ThumbnailData, Top8Data


def get_tournaments() -> list[str]:
    # TODO: This may need to get updated for Doubles and Colosseum Top 8 Graphics.
    return [f.name for f in os.scandir(TOP8_DIR) if f.is_dir()]


class TournamentDropdown(QComboBox):
    def __init__(self, data: ThumbnailData | Top8Data) -> None:
        super().__init__()

        self.data = data
        self.addItems(get_tournaments())
        self.setCurrentText(data["tournament"])
        self.currentTextChanged.connect(self.get_selection)

    def get_selection(self, text: str) -> None:
        self.data["tournament"] = text
