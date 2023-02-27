from PyQt6.QtWidgets import QLineEdit


class RoundTextbox(QLineEdit):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.setText(data["round"])
        self.textChanged.connect(lambda: self.update())

    def update(self):
        self.data["round"] = self.text()
