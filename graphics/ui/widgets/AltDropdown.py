from PyQt6.QtWidgets import QComboBox


class AltDropdown(QComboBox):
    def __init__(self, player_data):
        super().__init__()
        self.player_data = player_data
        self.addItems(["01", "02", "03", "04", "05", "06", "07", "08"])
        self.player_data["alt"] = self.currentText()
        self.currentTextChanged.connect(self.get_selection)

    def get_selection(self, text):
        self.player_data["alt"] = text
