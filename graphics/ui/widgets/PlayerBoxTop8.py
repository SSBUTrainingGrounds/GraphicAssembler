from enum import Enum

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QLabel, QToolButton, QPushButton, QWidget

from graphics.ui.widgets.AltDropdown import AltDropdown
from graphics.ui.widgets.CharacterDropdown import CharacterDropdown
from graphics.ui.widgets.OffsetSlider import OffsetSlider
from graphics.ui.widgets.PlayerTag import PlayerTag
from graphics.ui.widgets.PlayerTwitter import PlayerTwitter
from graphics.utils.Types import Top8Player
from graphics.utils.Defaults import DEFAULT_CHARACTER

# For type hinting
PlayerAccordionChild = (
        CharacterDropdown | AltDropdown | OffsetSlider | QLabel | PlayerTag | PlayerTwitter
)


class Character(Enum):
    MAIN = "main"
    SECONDARY = "secondary"
    POCKET = "pocket"


class PlayerAccordion(QWidget):
    def __init__(self, player_data: Top8Player, player_number: int):
        super().__init__()

        self.previous_character = None
        self.current_character = Character.MAIN
        self.next_character = Character.SECONDARY

        self.data = player_data
        self.toggle_button = QToolButton()
        self.toggle_button.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon
        )

        self.toggle_button.setText(f"Player {player_number + 1}")
        self.toggle_button.setArrowType(Qt.ArrowType.RightArrow)
        self.toggle_button.clicked.connect(self.toggle)

        self.add_character = QPushButton()
        self.add_character.setText(f"Add Secondary")
        self.add_character.clicked.connect(self.new_character)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.toggle_button, 0, 0, 1, 2)

        self.tag_label = QLabel("Tag")
        self.tag_textbox = PlayerTag(self.data)
        self.twitter_label = QLabel("Twitter")
        self.twitter_textbox = PlayerTwitter(self.data)

        self.alt_label = QLabel("Alt")

        self.grid_layout.addWidget(self.tag_label, 1, 0)
        self.grid_layout.addWidget(self.twitter_label, 1, 1)
        self.grid_layout.addWidget(self.tag_textbox, 2, 0)
        self.grid_layout.addWidget(self.twitter_textbox, 2, 1)

        self.grid_layout.addWidget(self.add_character, 3, 0, alignment=Qt.AlignmentFlag.AlignHCenter)

        [self.main_layout, self.main_boxes] = self.setup_character()
        self.grid_layout.addLayout(self.main_layout, 4, 0, 2, 0)

        # initialize these to None, Changes when Updated
        [self.secondary_layout, self.secondary_boxes] = [None, None]

        [self.pocket_layout, self.pocket_boxes] = [None, None]

        self.hide_content()

        self.setLayout(self.grid_layout)

    def get_children(
            self,
    ) -> list[PlayerAccordionChild]:
        # The children are all the items that get hidden/shown when the accordion is toggled.

        all_children: list[PlayerAccordionChild] = [
            self.tag_label,
            self.twitter_label,
            self.tag_textbox,
            self.twitter_textbox,
            self.alt_label,
            self.add_character,
        ]
        all_children.extend(self.main_boxes)
        if self.secondary_boxes:
            all_children.extend(self.secondary_boxes)
        if self.pocket_boxes:
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

    def setup_character(self) -> [QGridLayout, list[PlayerAccordionChild]]:
        character_grid = QGridLayout()
        character_boxes = self.get_character_boxes(self.current_character.value)

        character_boxes[2].setMinimumHeight(133)

        character_grid.addWidget(character_boxes[3], 0, 0)
        character_grid.addWidget(self.alt_label, 0, 1)
        character_grid.addWidget(character_boxes[0], 1, 0)
        character_grid.addWidget(character_boxes[1], 1, 1)
        character_grid.addWidget(character_boxes[2], 2, 0, 3, 2)

        return character_grid, character_boxes

    def new_character(self) -> None:
        match self.next_character:
            case Character.SECONDARY:
                self.previous_character = self.current_character
                self.current_character = self.next_character
                self.next_character = Character.POCKET

                self.data["secondary"] = DEFAULT_CHARACTER

                [self.secondary_layout, self.secondary_boxes] = self.setup_character()
                self.grid_layout.addLayout(self.secondary_layout, 6, 0, 2, 0)

                self.add_character.setText("Add Pocket")

            case Character.POCKET:
                self.previous_character = self.current_character
                self.current_character = self.next_character

                self.data["pocket"] = DEFAULT_CHARACTER

                [self.pocket_layout, self.pocket_boxes] = self.setup_character()
                self.grid_layout.addLayout(self.pocket_layout, 8, 0, 2, 0)

                self.add_character.setDisabled(True)

        self.show_content()

    # def delete_character(self) -> None:

    # TODO: Create Delete Character Buttons
