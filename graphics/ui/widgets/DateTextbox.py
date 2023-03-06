from PyQt6.QtWidgets import QLineEdit

from graphics.utils.types import Top8Data


class DateTextbox(QLineEdit):
    def __init__(self, data: Top8Data) -> None:
        super().__init__()
        self.data = data
        self.setText(data["date"])
        self.textChanged.connect(lambda: self.update())

    def update(self) -> None:
        self.data["date"] = self.text()
