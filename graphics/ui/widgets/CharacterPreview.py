from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel

from graphics.app.generate import get_character_path


class CharacterPreview(QLabel):
    def __init__(self, player_data):
        super().__init__()
        self.player_data = player_data
        self.setPixmap(
            QPixmap(
                get_character_path(
                    self.player_data["character"], self.player_data["alt"]
                )
            ).scaledToHeight(200, mode=Qt.TransformationMode.SmoothTransformation)
        )

    def update(self):
        self.setPixmap(
            QPixmap(
                get_character_path(
                    self.player_data["character"], self.player_data["alt"]
                )
            ).scaledToHeight(200, mode=Qt.TransformationMode.SmoothTransformation)
        )
