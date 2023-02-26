from PyQt6.QtWidgets import QComboBox


class TournamentDropdown(QComboBox):
    def __init__(self, data):
        super().__init__()

        self.data = data
        self.addItems(["tos", "so"])
        self.setCurrentText(data["tournament"])
        self.currentTextChanged.connect(self.get_selection)

    def get_selection(self, text):
        self.data["tournament"] = text
