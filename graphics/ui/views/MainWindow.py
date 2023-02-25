from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QMainWindow, QWidget

from graphics.ui.widgets.AltDropdown import AltDropdown
from graphics.ui.widgets.CharacterDropdown import CharacterDropdown
from graphics.ui.widgets.CreateButton import CreateButton
from graphics.ui.widgets.ImagePreview import ImagePreview
from graphics.ui.widgets.OffsetSlider import OffsetSlider
from graphics.ui.widgets.PlayerTag import PlayerTag


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TG Graphics")
        self.resize(600, 450)
        self.grid = QGridLayout()

        layout = QHBoxLayout()
        layout.addLayout(self.grid)

        data = {
            "players": [
                {
                    "tag": "NIFARES",
                    "character": "01-Mario",
                    "alt": "01",
                    "offset": [0, 0],
                    "zoom": 100,
                },
                {
                    "tag": "PARZ",
                    "character": "02-Donkey Kong",
                    "alt": "01",
                    "offset": [0, 0],
                    "zoom": 100,
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

        player_tag_one = PlayerTag(player_one)
        player_tag_two = PlayerTag(player_two)

        offset_sliders_one = OffsetSlider(player_one)
        offset_sliders_two = OffsetSlider(player_two)

        preview = ImagePreview(data)

        button = CreateButton(data)

        self.grid.addWidget(player_tag_one, 0, 0)
        self.grid.addWidget(character_dropdown_one, 0, 1)
        self.grid.addWidget(alt_dropdown_one, 0, 2)
        self.grid.addWidget(offset_sliders_one, 1, 0, 2, 3)

        self.grid.addWidget(player_tag_two, 0, 3)
        self.grid.addWidget(character_dropdown_two, 0, 4)
        self.grid.addWidget(alt_dropdown_two, 0, 5)
        self.grid.addWidget(offset_sliders_two, 1, 3, 2, 3)

        self.grid.addWidget(preview, 3, 0, 1, 6)

        character_dropdown_one.currentTextChanged.connect(lambda: preview.update())
        character_dropdown_two.currentTextChanged.connect(lambda: preview.update())

        alt_dropdown_one.currentTextChanged.connect(lambda: preview.update())
        alt_dropdown_two.currentTextChanged.connect(lambda: preview.update())

        player_tag_one.textChanged.connect(lambda: preview.update())
        player_tag_two.textChanged.connect(lambda: preview.update())

        for child in offset_sliders_one.children:
            child.valueChanged.connect(lambda: preview.update())

        for child in offset_sliders_two.children:
            child.valueChanged.connect(lambda: preview.update())

        self.grid.addWidget(button, 0, 6)

        widget = QWidget()

        widget.setLayout(layout)

        self.setCentralWidget(widget)
