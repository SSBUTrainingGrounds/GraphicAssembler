from PyQt6.QtWidgets import QLineEdit

from graphics.utils.types import PlayerData


class PlayerTag(QLineEdit):
    def __init__(self, player: PlayerData) -> None:
        super().__init__()
        self.player = player
        self.setText(player["tag"])
        self.textChanged.connect(lambda: self.update())

    def update(self) -> None:
        self.player["tag"] = self.text()
