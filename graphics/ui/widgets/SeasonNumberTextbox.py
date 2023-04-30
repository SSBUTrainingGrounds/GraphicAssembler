from PyQt6.QtWidgets import QGridLayout, QLineEdit, QWidget

from graphics.utils.Types import Top8Data


class SeasonNumberBox(QWidget):
    def __init__(self, data: Top8Data) -> None:
        super().__init__()
        self.data = data

        self.season: SeasonTextbox = SeasonTextbox(data)
        self.number = NumberTextbox(data)

        self.grid_layout = QGridLayout()

        self.grid_layout.addWidget(self.season, 0, 0)
        self.grid_layout.addWidget(self.number, 0, 1)

        self.get_all_textbox = [self.season, self.number]

        self.setLayout(self.grid_layout)


class SeasonTextbox(QLineEdit):
    def __init__(self, data: Top8Data) -> None:
        super().__init__()
        self.data = data
        self.setText(str(data["season"]))
        self.textChanged.connect(lambda: self.update())

    def update(self) -> None:
        if self.text():
            self.data["season"] = int(self.text())


class NumberTextbox(QLineEdit):
    def __init__(self, data: Top8Data) -> None:
        super().__init__()
        self.data = data
        # This is the number of the tournament in the season.
        self.setText(str(data["number"]))
        self.textChanged.connect(lambda: self.update())

    def update(self) -> None:
        if self.text():
            self.data["number"] = int(self.text())
