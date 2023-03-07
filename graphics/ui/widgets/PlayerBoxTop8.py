from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QLabel, QToolButton, QWidget

from graphics.ui.widgets.AltDropdown import AltDropdown
from graphics.ui.widgets.CharacterDropdown import CharacterDropdown
from graphics.ui.widgets.OffsetSlider import OffsetSlider
from graphics.ui.widgets.PlayerTag import PlayerTag
from graphics.ui.widgets.PlayerTwitter import PlayerTwitter
from graphics.utils.types import Top8Player

# For type hinting
PlayerAccordionChild = (
    CharacterDropdown | AltDropdown | OffsetSlider | QLabel | PlayerTag | PlayerTwitter
)


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

        self.tag_label = QLabel("Tag")
        self.tag_textbox = PlayerTag(self.data)
        self.twitter_label = QLabel("Twitter")
        self.twitter_textbox = PlayerTwitter(self.data)

        self.alt_label = QLabel("Alt")

        self.main_boxes = self.get_character_boxes("main")
        self.secondary_boxes = self.get_character_boxes("secondary")
        self.pocket_boxes = self.get_character_boxes("pocket")

        # The offset sliders.
        self.main_boxes[2].setMinimumHeight(150)
        self.secondary_boxes[2].setMinimumHeight(150)
        self.pocket_boxes[2].setMinimumHeight(150)

        self.grid_layout.addWidget(self.tag_label, 1, 0)
        self.grid_layout.addWidget(self.twitter_label, 1, 1)
        self.grid_layout.addWidget(self.tag_textbox, 2, 0)
        self.grid_layout.addWidget(self.twitter_textbox, 2, 1)
        self.grid_layout.addWidget(self.main_boxes[3], 3, 0)
        self.grid_layout.addWidget(self.alt_label, 3, 1)
        self.grid_layout.addWidget(self.main_boxes[0], 4, 0)
        self.grid_layout.addWidget(self.main_boxes[1], 4, 1)
        self.grid_layout.addWidget(self.main_boxes[2], 5, 0, 3, 2)
        self.grid_layout.addWidget(self.secondary_boxes[3], 8, 0)
        self.grid_layout.addWidget(self.alt_label, 8, 1)
        self.grid_layout.addWidget(self.secondary_boxes[0], 9, 0)
        self.grid_layout.addWidget(self.secondary_boxes[1], 9, 1)
        self.grid_layout.addWidget(self.secondary_boxes[2], 10, 0, 3, 2)
        self.grid_layout.addWidget(self.pocket_boxes[3], 13, 0)
        self.grid_layout.addWidget(self.alt_label, 13, 1)
        self.grid_layout.addWidget(self.pocket_boxes[0], 14, 0)
        self.grid_layout.addWidget(self.pocket_boxes[1], 14, 1)
        self.grid_layout.addWidget(self.pocket_boxes[2], 15, 0, 3, 2)

        self.hide_content()

        self.setLayout(self.grid_layout)

    def get_children(
        self,
    ) -> list[PlayerAccordionChild]:
        all_children: list[PlayerAccordionChild] = [
            self.tag_label,
            self.twitter_label,
            self.tag_textbox,
            self.twitter_textbox,
            self.alt_label,
        ]
        all_children.extend(self.main_boxes)
        all_children.extend(self.secondary_boxes)
        all_children.extend(self.pocket_boxes)

        return all_children

    def hide_content(self):
        for player_box in self.get_children():
            player_box.setVisible(False)

    def show_content(self):
        for player_box in self.get_children():
            player_box.setVisible(True)

    def toggle(self):
        if self.toggle_button.arrowType() == Qt.ArrowType.RightArrow:
            self.toggle_button.setArrowType(Qt.ArrowType.DownArrow)
            self.show_content()
        else:
            self.toggle_button.setArrowType(Qt.ArrowType.RightArrow)
            self.hide_content()

    def get_character_boxes(self, character_type: str) -> list[PlayerAccordionChild]:
        return [
            CharacterDropdown(self.data, character_type),
            AltDropdown(self.data, character_type),
            OffsetSlider(self.data, character_type),
            QLabel(character_type.capitalize()),
        ]
