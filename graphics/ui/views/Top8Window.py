from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QWidget

from graphics.app.Top8Generate import generate_top8
from graphics.ui.widgets.DateTextbox import DateTextbox
from graphics.ui.widgets.EntrantsTextbox import EntrantsTextbox
from graphics.ui.widgets.SaveImageButton import SaveImageButton
from graphics.ui.widgets.ScrollSidebar import ScrollSidebar
from graphics.ui.widgets.SeasonNumberTextbox import SeasonNumberBox
from graphics.ui.widgets.TournamentDropdown import TournamentDropdown
from graphics.utils.Definitions import ASSET_DIR
from graphics.utils.Types import Top8Data, Top8Player
from graphics.utils.Defaults import DEFAULT_CHARACTER


class Top8Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("TG Graphics (Top 8)")
        self.resize(1200, 850)
        self.setWindowIcon(QIcon(ASSET_DIR + "/icon.png"))

        self.grid = QGridLayout()

        layout = QHBoxLayout()

        data: Top8Data = {
            "players": self.get_default_players(),
            "tournament": "tos",
            "season": 1,
            "number": 1,
            "date": "22/12/31",
            "entrants": 8,
        }

        tournament_dropdown = TournamentDropdown(data)
        season_number_box = SeasonNumberBox(data)
        date_textbox = DateTextbox(data)
        entrants_textbox = EntrantsTextbox(data)
        player_sidebar = ScrollSidebar(data)

        # Otherwise this would be a bit squished, while the other widgets take up too much space.
        tournament_dropdown.setMinimumWidth(200)

        # TODO: Replace with actual image preview
        placeholder_image = QLabel()
        placeholder_image.setPixmap(QPixmap(round(1920 / 2), round(1080 / 2)))

        button = SaveImageButton(data, generate_top8, "top8")

        # The top bar are the columns for the tournament, season, number, date, and entrants above the preview and player sidebar.
        top_bar_layout = QGridLayout()

        top_bar_layout.addWidget(
            QLabel("Tournament"), 0, 0, Qt.AlignmentFlag.AlignHCenter
        )
        top_bar_layout.addWidget(QLabel("Season"), 0, 1, Qt.AlignmentFlag.AlignHCenter)
        top_bar_layout.addWidget(QLabel("Number"), 0, 2, Qt.AlignmentFlag.AlignHCenter)
        top_bar_layout.addWidget(QLabel("Date"), 0, 3, Qt.AlignmentFlag.AlignHCenter)
        top_bar_layout.addWidget(
            QLabel("Entrants"), 0, 4, Qt.AlignmentFlag.AlignHCenter
        )

        top_bar_layout.addWidget(tournament_dropdown, 1, 0)
        top_bar_layout.addWidget(season_number_box, 1, 1, 1, 2)
        top_bar_layout.addWidget(date_textbox, 1, 3)
        top_bar_layout.addWidget(entrants_textbox, 1, 4)

        self.grid.addLayout(top_bar_layout, 0, 0, 1, 7)

        self.grid.addWidget(placeholder_image, 2, 0, 15, 4)

        self.player_label = QLabel("Players")
        self.player_label.setStyleSheet("font-size: 14px; color: #777777;")
        self.grid.addWidget(self.player_label, 2, 4, Qt.AlignmentFlag.AlignCenter)

        self.grid.addWidget(player_sidebar, 3, 4, 15, 3, Qt.AlignmentFlag.AlignHCenter)

        self.grid.addWidget(button, 18, 0, 1, 7, Qt.AlignmentFlag.AlignCenter)

        layout.addLayout(self.grid)

        self.setLayout(layout)

    def get_default_players(self) -> list[Top8Player]:
        players: list[Top8Player] = []

        for i in range(8):
            player: Top8Player = {
                "tag": f"Player {i + 1}",
                # The placements are 1, 2, 3, 4, 5, 5, 7, 7
                "placement": i if (i == 5 or i == 7) else i + 1,
                "main": DEFAULT_CHARACTER,
            }

            players.append(player)

        return players
