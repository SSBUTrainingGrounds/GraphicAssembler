from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QLabel, QWidget

from graphics.ui.widgets.AltDropdown import AltDropdown
from graphics.ui.widgets.CharacterDropdown import CharacterDropdown
from graphics.ui.widgets.OffsetSlider import OffsetSlider
from graphics.ui.widgets.PlayerTag import PlayerTag
from graphics.utils.Types import ThumbnailPlayer


class PlayerBox(QWidget):
    def __init__(self, player_data: ThumbnailPlayer, player_number: int) -> None:
        super().__init__()
        self.player_data = player_data
        self.player_number = player_number

        self.grid_layout = QGridLayout()

        self.player_label = QLabel(f"Player {player_number}")
        self.player_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.player_label.setStyleSheet("font-size: 14px; color: #777777;")

        self.character_dropdown = CharacterDropdown(player_data)
        self.alt_dropdown = AltDropdown(player_data)
        self.player_tag = PlayerTag(player_data)
        self.offset_sliders = OffsetSlider(player_data)

        self.grid_layout.addWidget(self.player_label, 0, 0, 1, 3)
        self.grid_layout.addWidget(QLabel("Tag"), 1, 0, 1, 3)
        self.grid_layout.addWidget(QLabel("Character"), 1, 1)
        self.grid_layout.addWidget(QLabel("Alt"), 1, 2)

        self.grid_layout.addWidget(self.player_tag, 2, 0)
        self.grid_layout.addWidget(self.character_dropdown, 2, 1)
        self.grid_layout.addWidget(self.alt_dropdown, 2, 2)
        self.grid_layout.addWidget(self.offset_sliders, 3, 0, 1, 3)

        self.all_dropdowns = [self.character_dropdown, self.alt_dropdown]

        self.character_dropdown.currentTextChanged.connect(self.reset)

        self.setLayout(self.grid_layout)

    def reset(self) -> None:
        self.offset_sliders.reset()
        self.alt_dropdown.reset()
