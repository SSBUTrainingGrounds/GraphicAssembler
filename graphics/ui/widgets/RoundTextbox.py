from PyQt6.QtWidgets import QLineEdit

from graphics.utils.types import TournamentData


class RoundTextbox(QLineEdit):
    def __init__(self, data: TournamentData) -> None:
        super().__init__()
        self.data = data
        self.setText(data["round"])
        self.textChanged.connect(lambda: self.update())

    def update(self) -> None:
        self.data["round"] = self.text()
