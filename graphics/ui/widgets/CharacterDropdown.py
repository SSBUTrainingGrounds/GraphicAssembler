import os
from typing import Optional

from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QComboBox

from graphics.utils.SettingsManager import settings_manager
from graphics.utils.Types import ThumbnailPlayer, Top8Player


def get_characters() -> list[str]:
    renders_dir = settings_manager.get_setting_value("render_dir")
    return ["None"] + [f.name for f in os.scandir(renders_dir) if f.is_dir()]


class CharacterDropdown(QComboBox):
    def __init__(
            self,
            player_data: ThumbnailPlayer | Top8Player,
            character_type: Optional[str] = None,
    ) -> None:
        super().__init__()

        self.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)

        self.character_type = character_type

        if not self.character_type:
            self.character_type = "character"

        self.player_data = player_data
        self.currentTextChanged.connect(self.get_selection)

    def get_selection(self, text: str) -> None:
        self.player_data[f"{self.character_type}"]["name"] = text

    def wheelEvent(self, event) -> None:
        if self.hasFocus():
            return QComboBox.wheelEvent(self, event)
        else:
            event.ignore()

    def showEvent(self, e: QtGui.QShowEvent) -> None:
        self.addItems(get_characters())
        if f"{self.character_type}" in self.player_data:
            self.setCurrentText(self.player_data[f"{self.character_type}"]["name"])
