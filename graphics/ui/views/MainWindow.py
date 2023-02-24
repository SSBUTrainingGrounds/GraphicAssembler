from PyQt6.QtWidgets import QHBoxLayout, QMainWindow, QWidget

from graphics.ui.widgets.AltDropdown import AltDropdown
from graphics.ui.widgets.CharacterDropdown import CharacterDropdown
from graphics.ui.widgets.CreateButton import CreateButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TG Graphics")
        self.resize(400, 300)

        data = {
            "players": [{
                "tag": "",
                "character": "",
                "alt": "",
            }, {
                "tag": "",
                "character": "",
                "alt": "",
            }],
            "tournament": "tos",
            "round": "",
        }

        player_one = data["players"][0]
        player_two = data["players"][1]

        character_dropdown_one = CharacterDropdown(player_one)
        character_dropdown_two = CharacterDropdown(player_two)
        alt_dropdown_one = AltDropdown(player_one)
        alt_dropdown_two = AltDropdown(player_two)

        button = CreateButton(data)

        layout = QHBoxLayout()

        layout.addWidget(character_dropdown_one)
        layout.addWidget(alt_dropdown_one)
        layout.addWidget(character_dropdown_two)
        layout.addWidget(alt_dropdown_two)
        layout.addWidget(button)

        widget = QWidget()

        widget.setLayout(layout)

        self.setCentralWidget(widget)
