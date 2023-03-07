from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QToolButton, QWidget

from graphics.ui.widgets.AltDropdown import AltDropdown
from graphics.ui.widgets.CharacterDropdown import CharacterDropdown
from graphics.ui.widgets.OffsetSlider import OffsetSlider
from graphics.ui.widgets.PlayerTag import PlayerTag
from graphics.ui.widgets.PlayerTwitter import PlayerTwitter
from graphics.utils.types import Top8Player


class PlayerAccordion(QWidget):
    def __init__(self, player_data: Top8Player, player_number: int):
        super().__init__()

        self.data = player_data
        self.toggle_button = QToolButton()
        self.toggle_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon
        )
        self.toggle_button.setText(f"Player {player_number + 1}")
        self.toggle_button.setArrowType(Qt.ArrowType.RightArrow)
        self.toggle_button.clicked.connect(self.toggle)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.toggle_button, 0, 0, 1, 2)

        self.tag_textbox = PlayerTag(self.data)
        self.twitter_textbox = PlayerTwitter(self.data)

        self.main_dropdown = CharacterDropdown(self.data, "main")
        self.main_alt_dropdown = AltDropdown(self.data, "main")
        self.main_offset_slider = OffsetSlider(self.data, "main")

        self.secondary_dropdown = CharacterDropdown(self.data, "secondary")
        self.secondary_alt_dropdown = AltDropdown(self.data, "secondary")
        self.secondary_offset_slider = OffsetSlider(self.data, "secondary")

        self.pocket_dropdown = CharacterDropdown(self.data, "pocket")
        self.pocket_alt_dropdown = AltDropdown(self.data, "pocket")
        self.pocket_offset_slider = OffsetSlider(self.data, "pocket")

        self.main_offset_slider.setMinimumHeight(150)
        self.secondary_offset_slider.setMinimumHeight(150)
        self.pocket_offset_slider.setMinimumHeight(150)

        self.grid_layout.addWidget(self.tag_textbox, 1, 0)
        self.grid_layout.addWidget(self.twitter_textbox, 1, 1)
        self.grid_layout.addWidget(self.main_dropdown, 2, 0)
        self.grid_layout.addWidget(self.main_alt_dropdown, 2, 1)
        self.grid_layout.addWidget(self.main_offset_slider, 3, 0, 3, 2)
        self.grid_layout.addWidget(self.secondary_dropdown, 6, 0)
        self.grid_layout.addWidget(self.secondary_alt_dropdown, 6, 1)
        self.grid_layout.addWidget(self.secondary_offset_slider, 7, 0, 3, 2)
        self.grid_layout.addWidget(self.pocket_dropdown, 10, 0)
        self.grid_layout.addWidget(self.pocket_alt_dropdown, 10, 1)
        self.grid_layout.addWidget(self.pocket_offset_slider, 11, 0, 3, 2)

        self.player_boxes = [
            self.tag_textbox,
            self.twitter_textbox,
            self.main_dropdown,
            self.main_alt_dropdown,
            self.main_offset_slider,
            self.secondary_dropdown,
            self.secondary_alt_dropdown,
            self.secondary_offset_slider,
            self.pocket_dropdown,
            self.pocket_alt_dropdown,
            self.pocket_offset_slider,
        ]

        for player_box in self.player_boxes:
            player_box.setVisible(False)

        self.setLayout(self.grid_layout)

    def toggle(self):
        if self.toggle_button.arrowType() == Qt.ArrowType.RightArrow:
            self.toggle_button.setArrowType(Qt.ArrowType.DownArrow)
            for player_box in self.player_boxes:
                player_box.setVisible(True)
        else:
            self.toggle_button.setArrowType(Qt.ArrowType.RightArrow)
            for player_box in self.player_boxes:
                player_box.setVisible(False)
