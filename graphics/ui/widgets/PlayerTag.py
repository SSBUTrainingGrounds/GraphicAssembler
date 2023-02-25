from PyQt6.QtWidgets import QLineEdit


class PlayerTag(QLineEdit):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.setText(player["tag"])
        self.textChanged.connect(lambda: self.update())

    def update(self):
        self.player["tag"] = self.text()
