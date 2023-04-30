from PyQt6.QtWidgets import QLineEdit

from graphics.utils.Types import Top8Data


class EntrantsTextbox(QLineEdit):
    def __init__(self, data: Top8Data) -> None:
        super().__init__()
        self.data = data
        self.setText(str(data["entrants"]))
        self.textEdited.connect(lambda: self.update())

    def update(self) -> None:
        if self.text():
            self.data["entrants"] = int(self.text())
