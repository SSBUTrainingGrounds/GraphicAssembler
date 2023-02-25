from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QMainWindow, QWidget

from graphics.ui.widgets.AltDropdown import AltDropdown
from graphics.ui.widgets.CharacterDropdown import CharacterDropdown
from graphics.ui.widgets.CreateButton import CreateButton
from graphics.ui.widgets.ImagePreview import ImagePreview


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TG Graphics")
        self.resize(400, 300)
        self.grid = QGridLayout()

        layout = QHBoxLayout()
        layout.addLayout(self.grid)

        data = {
            "players": [
                {
                    "tag": "",
                    "character": "",
                    "alt": "",
                },
                {
                    "tag": "",
                    "character": "",
                    "alt": "",
                },
            ],
            "tournament": "tos",
            "round": "",
        }

        player_one = data["players"][0]
        player_two = data["players"][1]

        character_dropdown_one = CharacterDropdown(player_one)
        character_dropdown_two = CharacterDropdown(player_two)

        alt_dropdown_one = AltDropdown(player_one)
        alt_dropdown_two = AltDropdown(player_two)

        preview = ImagePreview(data)

        button = CreateButton(data)

        self.grid.addWidget(character_dropdown_one, 0, 0)
        self.grid.addWidget(alt_dropdown_one, 0, 1)
        self.grid.addWidget(preview, 1, 0, 1, 4)

        self.grid.addWidget(character_dropdown_two, 0, 2)
        self.grid.addWidget(alt_dropdown_two, 0, 3)

        character_dropdown_one.currentTextChanged.connect(lambda: preview.update())
        character_dropdown_two.currentTextChanged.connect(lambda: preview.update())

        alt_dropdown_one.currentTextChanged.connect(lambda: preview.update())
        alt_dropdown_two.currentTextChanged.connect(lambda: preview.update())

        self.grid.addWidget(button, 0, 4)

        widget = QWidget()

        widget.setLayout(layout)

        self.setCentralWidget(widget)
