from itertools import chain

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QMainWindow, QWidget

from graphics.definitions import ASSET_DIR
from graphics.ui.widgets.AltDropdown import AltDropdown
from graphics.ui.widgets.CharacterDropdown import CharacterDropdown
from graphics.ui.widgets.CreateButton import CreateButton
from graphics.ui.widgets.ImagePreview import ImagePreview
from graphics.ui.widgets.OffsetSlider import OffsetSlider
from graphics.ui.widgets.PlayerTag import PlayerTag
from graphics.ui.widgets.RoundTextbox import RoundTextbox
from graphics.ui.widgets.TournamentDropdown import TournamentDropdown
from graphics.utils.types import TournamentData


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("TG Graphics")
        self.resize(800, 700)
        self.setWindowIcon(QIcon(ASSET_DIR + "/icon.png"))

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
                    "tag": "PLAYER 1",
                    "character": "01-Mario",
                    "alt": "01",
                    "offset": (0, 0),
                    "zoom": 100,
                },
                {
                    "tag": "PLAYER 2",
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

        self.grid.addWidget(QLabel("Round"), 0, 0, 1, 3)
        self.grid.addWidget(QLabel("Tournament"), 0, 4, 1, 3)
        self.grid.addWidget(round_textbox, 1, 0, 1, 3)
        self.grid.addWidget(tournament_dropdown, 1, 4, 1, 3)

        player_one_label = QLabel("Player 1")
        player_one_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        player_one_label.setStyleSheet(
            "font-size: 14px; color: #777777; margin-top: 10px; margin-bottom: 10px;"
        )

        player_two_label = QLabel("Player 2")
        player_two_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        player_two_label.setStyleSheet(
            "font-size: 14px; color: #777777; margin-top: 10px; margin-bottom: 10px;"
        )

        self.grid.addWidget(player_one_label, 2, 0, 1, 3)
        self.grid.addWidget(QLabel("Tag"), 3, 0, 1, 3)
        self.grid.addWidget(QLabel("Character"), 3, 1)
        self.grid.addWidget(QLabel("Alt"), 3, 2)

        self.grid.addWidget(player_tag_one, 4, 0)
        self.grid.addWidget(character_dropdown_one, 4, 1)
        self.grid.addWidget(alt_dropdown_one, 4, 2)
        self.grid.addWidget(offset_sliders_one, 5, 0, 1, 3)

        self.grid.addWidget(player_two_label, 2, 3, 1, 3)
        self.grid.addWidget(QLabel("Tag"), 3, 4, 1, 3)
        self.grid.addWidget(QLabel("Character"), 3, 5)
        self.grid.addWidget(QLabel("Alt"), 3, 6)

        self.grid.addWidget(player_tag_two, 4, 4)
        self.grid.addWidget(character_dropdown_two, 4, 5)
        self.grid.addWidget(alt_dropdown_two, 4, 6)
        self.grid.addWidget(offset_sliders_two, 5, 4, 1, 3)

        self.grid.setColumnMinimumWidth(3, 40)

        self.grid.addWidget(preview, 8, 0, 1, 7, alignment=Qt.AlignmentFlag.AlignCenter)

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

        self.grid.addWidget(button, 9, 0, 1, 7, alignment=Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()

        widget.setLayout(layout)

        self.setCentralWidget(widget)
