from PyQt6.QtWidgets import QComboBox


class AltDropdown(QComboBox):
    def __init__(self):
        super().__init__()

        self.addItems(["01", "02", "03", "04", "05", "06", "07", "08"])
