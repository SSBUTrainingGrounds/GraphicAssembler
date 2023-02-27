from itertools import chain

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QMainWindow, QWidget

from graphics.app.types import TournamentData
from graphics.ui.widgets.AltDropdown import AltDropdown
from graphics.ui.widgets.CharacterDropdown import CharacterDropdown
from graphics.ui.widgets.CreateButton import CreateButton
from graphics.ui.widgets.ImagePreview import ImagePreview
from graphics.ui.widgets.OffsetSlider import OffsetSlider
from graphics.ui.widgets.PlayerTag import PlayerTag
from graphics.ui.widgets.RoundTextbox import RoundTextbox
from graphics.ui.widgets.TournamentDropdown import TournamentDropdown


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("TG Graphics")
        self.resize(600, 500)
        self.grid = QGridLayout()
        self.timer_duration = 100  # Timer in milliseconds

        layout = QHBoxLayout()
        layout.addLayout(self.grid)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.setSingleShot(True)
        self.timer.start(self.timer_duration)

        data: TournamentData = {
            "players": [
                {
                    "tag": "NIFARES",
                    "character": "01-Mario",
                    "alt": "01",
                    "offset": (0, 0),
                    "zoom": 100,
                },
                {
                    "tag": "PARZ",
                    "character": "02-Donkey Kong",
                    "alt": "01",
                    "offset": (0, 0),
                    "zoom": 100,
                },
            ],
            "tournament": "tos",
            "round": "GRAND FINALS",
        }

        player_one = data["players"][0]
        player_two = data["players"][1]

        round_textbox = RoundTextbox(data)
        tournament_dropdown = TournamentDropdown(data)

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

        self.grid.addWidget(round_textbox, 0, 0, 1, 2)
        self.grid.addWidget(tournament_dropdown, 0, 2, 1, 2)

        self.grid.addWidget(player_tag_one, 1, 0)
        self.grid.addWidget(character_dropdown_one, 1, 1)
        self.grid.addWidget(alt_dropdown_one, 1, 2)
        self.grid.addWidget(offset_sliders_one, 2, 0, 2, 3)

        self.grid.addWidget(player_tag_two, 1, 3)
        self.grid.addWidget(character_dropdown_two, 1, 4)
        self.grid.addWidget(alt_dropdown_two, 1, 5)
        self.grid.addWidget(offset_sliders_two, 2, 3, 2, 3)

        self.grid.addWidget(preview, 4, 0, 1, 6)

        # Connect all the widgets to the timer
        for child in [
            tournament_dropdown,
            character_dropdown_one,
            character_dropdown_two,
            alt_dropdown_one,
            alt_dropdown_two,
        ]:
            child.currentTextChanged.connect(
                lambda: (self.timer.start(self.timer_duration))
            )

        for child in [round_textbox, player_tag_one, player_tag_two]:
            child.textChanged.connect(lambda: self.timer.start(self.timer_duration))

        for child in list(
            chain(offset_sliders_one.all_children, offset_sliders_two.all_children)
        ):
            child.valueChanged.connect(lambda: self.timer.start(self.timer_duration))

        # Connect the timer to the preview
        self.timer.timeout.connect(preview.update)

        self.grid.addWidget(button, 0, 6)

        widget = QWidget()

        widget.setLayout(layout)

        self.setCentralWidget(widget)
