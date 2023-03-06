from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QWidget

from graphics.ui.widgets.DateTextbox import DateTextbox
from graphics.ui.widgets.EntrantsTextbox import EntrantsTextbox
from graphics.ui.widgets.ScrollSidebar import ScrollSidebar
from graphics.ui.widgets.SeasonNumberTextbox import SeasonNumberBox
from graphics.ui.widgets.TournamentDropdown import TournamentDropdown
from graphics.utils.definitions import ASSET_DIR
from graphics.utils.types import Top8Data, Top8Player


class Top8Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("TG Graphics (Top 8)")
        self.resize(1200, 700)
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

        # TODO: Replace with actual image
        placeholder_image = QLabel()
        placeholder_image.setPixmap(QPixmap(round(1920 / 3), round(1080 / 3)))

        self.grid.addWidget(tournament_dropdown, 0, 0)
        self.grid.addWidget(season_number_box, 0, 1)
        self.grid.addWidget(date_textbox, 0, 2)
        self.grid.addWidget(entrants_textbox, 0, 3)
        self.grid.addWidget(placeholder_image, 1, 0, 4, 4)
        self.grid.addWidget(player_sidebar, 1, 5, 1, 4)

        layout.addLayout(self.grid)

        self.setLayout(layout)

    def get_default_players(self) -> list[Top8Player]:
        players: list[Top8Player] = []

        for i in range(8):
            player: Top8Player = {
                "tag": f"Player {i+1}",
                "twitter": f"@player{i+1}",
                # The placements are 1, 2, 3, 4, 5, 5, 7, 7
                "placement": i if (i == 5 or i == 7) else i + 1,
                "main": {
                    "name": "01-Mario",
                    "alt": f"0{i+1}",
                    "offset": (0, 0),
                    "zoom": 100,
                },
                "secondary": {
                    "name": "02-Donkey Kong",
                    "alt": f"0{i+1}",
                    "offset": (200, 200),
                    "zoom": 90,
                },
                "pocket": {
                    "name": "03-Link",
                    "alt": f"0{i+1}",
                    "offset": (200, -200),
                    "zoom": 80,
                },
            }

            players.append(player)

        return players
