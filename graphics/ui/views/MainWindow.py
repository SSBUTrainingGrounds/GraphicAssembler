from itertools import chain

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QMainWindow, QWidget

from graphics.ui.widgets.CreateButton import CreateButton
from graphics.ui.widgets.ImagePreview import ImagePreview
from graphics.ui.widgets.PlayerBox import PlayerBox
from graphics.ui.widgets.RoundTextbox import RoundTextbox
from graphics.ui.widgets.TournamentDropdown import TournamentDropdown
from graphics.utils.definitions import ASSET_DIR
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

        preview = ImagePreview(data)

        button = CreateButton(data)

        self.grid.addWidget(QLabel("Round"), 0, 0, 1, 3)
        self.grid.addWidget(QLabel("Tournament"), 0, 4, 1, 3)
        self.grid.addWidget(round_textbox, 1, 0, 1, 3)
        self.grid.addWidget(tournament_dropdown, 1, 4, 1, 3)

        player_box_one = PlayerBox(player_one, 1)
        player_box_two = PlayerBox(player_two, 2)

        self.grid.addWidget(player_box_one, 2, 0, 4, 3)
        self.grid.addWidget(player_box_two, 2, 4, 4, 3)

        self.grid.setColumnMinimumWidth(3, 40)

        self.grid.addWidget(preview, 8, 0, 1, 7, alignment=Qt.AlignmentFlag.AlignCenter)

        # Connect all the widgets to the timer
        for child in (
            [tournament_dropdown]
            + player_box_one.all_dropdowns
            + player_box_two.all_dropdowns
        ):
            child.currentTextChanged.connect(
                lambda: (self.timer.start(self.timer_duration))
            )

        for child in [
            round_textbox,
            player_box_one.player_tag,
            player_box_two.player_tag,
        ]:
            child.textChanged.connect(lambda: self.timer.start(self.timer_duration))

        for child in list(
            chain(
                player_box_one.offset_sliders.all_children,
                player_box_two.offset_sliders.all_children,
            )
        ):
            child.valueChanged.connect(lambda: self.timer.start(self.timer_duration))

        # Connect the timer to the preview
        self.timer.timeout.connect(preview.update)

        self.grid.addWidget(button, 9, 0, 1, 7, alignment=Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()

        widget.setLayout(layout)

        self.setCentralWidget(widget)
