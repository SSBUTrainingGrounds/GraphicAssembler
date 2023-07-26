from PyQt6.QtWidgets import QLineEdit

from graphics.utils.Types import ThumbnailData


class RoundTextbox(QLineEdit):
    def __init__(self, data: ThumbnailData) -> None:
        super().__init__()
        self.data = data
        self.setText(data["round"])
        self.textChanged.connect(lambda: self.update())

    def update(self) -> None:
        self.data["round"] = self.text()
