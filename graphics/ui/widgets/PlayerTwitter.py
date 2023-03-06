from PyQt6.QtWidgets import QLineEdit

from graphics.utils.types import Top8Player


class PlayerTwitter(QLineEdit):
    def __init__(self, player: Top8Player) -> None:
        super().__init__()
        self.player = player
        self.setText(player["twitter"])
        self.textChanged.connect(lambda: self.update())

    def update(self) -> None:
        self.player["twitter"] = self.text()
