from enum import Enum
from typing import Union

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton

# For type hinting
from PyQt6.QtWidgets import QComboBox as Dropdown
from PyQt6.QtWidgets import QGridLayout, QLabel
from PyQt6.QtWidgets import QLineEdit as Textbox
from PyQt6.QtWidgets import QPushButton as Button
from PyQt6.QtWidgets import QToolButton, QWidget

from graphics.ui.widgets.AltDropdown import AltDropdown
from graphics.ui.widgets.CharacterDropdown import CharacterDropdown
from graphics.ui.widgets.OffsetSlider import (
    HorizontalSlider,
    OffsetSlider,
    VerticalSlider,
    ZoomSlider,
)
from graphics.ui.widgets.PlayerTag import PlayerTag
from graphics.ui.widgets.PlayerTwitter import PlayerTwitter
from graphics.utils.TimerConnection import connect_character_dropdown, connect_character_sliders
from graphics.utils.Defaults import DEFAULT_CHARACTER
from graphics.utils.Types import Top8Player

# For type hinting
PlayerAccordionChild = Union[
    CharacterDropdown,
    AltDropdown,
    OffsetSlider,
    QLabel,
    PlayerTag,
    PlayerTwitter,
    QPushButton,
]


class Character(Enum):
    MAIN = "main"
    SECONDARY = "secondary"
    POCKET = "pocket"


class PlayerAccordion(QWidget):
    def __init__(self, player_data: Top8Player, player_number: int, parent=None):
        super().__init__()

        # HACK to make timers work
        self.parent_window = parent
        self.top_parent = self.get_top_level_parent()

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
        self.add_character.setStyleSheet(
            """
            font-size: 12px;
        """
        )
        self.add_character.setText(f"Add Character")
        self.add_character.clicked.connect(self.new_character)

        self.delete_character = QPushButton()
        self.delete_character.setText(f"Delete Character")
        self.delete_character.setStyleSheet(
            """
            font-size: 12px;
        """
        )
        self.delete_character.clicked.connect(self.remove_character)
        self.delete_character.setDisabled(True)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.toggle_button, 0, 0, 1, 2)

        self.tag_label = QLabel("Tag")
        self.tag_textbox = PlayerTag(self.data)
        self.twitter_label = QLabel("Twitter")
        self.twitter_textbox = PlayerTwitter(self.data)

        self.grid_layout.addWidget(self.tag_label, 1, 0)
        self.grid_layout.addWidget(self.twitter_label, 1, 1)
        self.grid_layout.addWidget(self.tag_textbox, 2, 0)
        self.grid_layout.addWidget(self.twitter_textbox, 2, 1)

        self.grid_layout.addWidget(
            self.add_character, 3, 0, alignment=Qt.AlignmentFlag.AlignHCenter
        )
        self.grid_layout.addWidget(
            self.delete_character, 3, 1, alignment=Qt.AlignmentFlag.AlignHCenter
        )

        [self.main_layout, self.main_boxes] = self.setup_character()
        self.grid_layout.addLayout(self.main_layout, 4, 0, 2, 0)

        # initialize these to None, Changes when Updated
        [self.secondary_layout, self.secondary_boxes] = [None, None]

        [self.pocket_layout, self.pocket_boxes] = [None, None]

        self.hide_content()

        self.setLayout(self.grid_layout)

    def get_top_level_parent(self):
        parent = self.parent_window
        return parent.parent_window

    def get_children(self) -> list[PlayerAccordionChild]:
        # The children are all the items that get hidden/shown when the accordion is toggled.

        all_children: list[PlayerAccordionChild] = [
            self.tag_label,
            self.twitter_label,
            self.tag_textbox,
            self.twitter_textbox,
            self.add_character,
            self.delete_character,
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
            QLabel("Alt"),
        ]

    def setup_character(self) -> tuple[QGridLayout, list[PlayerAccordionChild]]:
        character_grid = QGridLayout()
        character_boxes = self.get_character_boxes(self.current_character.value)

        character_boxes[2].setMinimumHeight(133)

        character_grid.addWidget(character_boxes[3], 0, 0)
        character_grid.addWidget(character_boxes[4], 0, 1)
        character_grid.addWidget(character_boxes[0], 1, 0)
        character_grid.addWidget(character_boxes[1], 1, 1)
        character_grid.addWidget(character_boxes[2], 2, 0, 3, 2)

        return character_grid, character_boxes

    def new_character(self) -> None:
        match self.current_character:
            case Character.MAIN:
                self.previous_character = self.current_character
                self.current_character = self.next_character
                self.next_character = Character.POCKET

                self.data["secondary"] = DEFAULT_CHARACTER.copy()

                [self.secondary_layout, self.secondary_boxes] = self.setup_character()
                self.grid_layout.addLayout(self.secondary_layout, 6, 0, 2, 0)

                connect_character_dropdown(self.top_parent, self.secondary_boxes)
                connect_character_sliders(self.top_parent, self.secondary_boxes)

                self.delete_character.setDisabled(False)

            case Character.SECONDARY:
                self.previous_character = self.current_character
                self.current_character = self.next_character
                self.next_character = None

                self.data["pocket"] = DEFAULT_CHARACTER.copy()

                [self.pocket_layout, self.pocket_boxes] = self.setup_character()
                self.grid_layout.addLayout(self.pocket_layout, 8, 0, 2, 0)

                connect_character_dropdown(self.top_parent, self.pocket_boxes)
                connect_character_sliders(self.top_parent, self.pocket_boxes)

                self.add_character.setDisabled(True)

            case _:
                pass

        self.show_content()

    def remove_character(self) -> None:
        match self.current_character:
            case Character.SECONDARY:
                self.next_character = self.current_character
                self.current_character = self.previous_character
                self.previous_character = None

                self.data.pop("secondary")

                if self.secondary_layout:
                    # This completely clears the layout and deletes all the widgets.
                    while self.secondary_layout.count():
                        item = self.secondary_layout.takeAt(0)
                        widget = item.widget()

                        widget.deleteLater()

                    self.secondary_layout.deleteLater()
                    self.grid_layout.removeItem(self.secondary_layout)
                    self.secondary_layout = None

                self.secondary_boxes = None

                self.delete_character.setDisabled(True)

            case Character.POCKET:
                self.next_character = self.current_character
                self.current_character = self.previous_character
                self.previous_character = Character.MAIN

                self.data.pop("pocket")

                if self.pocket_layout:
                    while self.pocket_layout.count():
                        item = self.pocket_layout.takeAt(0)
                        widget = item.widget()

                        widget.deleteLater()

                    self.pocket_layout.deleteLater()
                    self.grid_layout.removeItem(self.pocket_layout)
                    self.pocket_layout = None

                self.pocket_boxes = None

                self.add_character.setDisabled(False)

            case _:
                pass

        self.show_content()

    def all_dropdown(self) -> list[Dropdown]:
        dropdowns = []
        for player_box in self.get_children():
            if isinstance(player_box, Dropdown):
                dropdowns.append(player_box)

        return dropdowns

    def all_textbox(self) -> list[Textbox]:
        textboxes = []
        for player_box in self.get_children():
            if isinstance(player_box, Textbox):
                textboxes.append(player_box)

        return textboxes

    def all_slider(self) -> list[HorizontalSlider | VerticalSlider | ZoomSlider]:
        sliders = []
        for player_box in self.get_children():
            if isinstance(player_box, OffsetSlider):
                sliders.extend(player_box.all_children)

        return sliders

    def all_button(self) -> list[Button]:
        buttons = []
        for player_box in self.get_children():
            if isinstance(player_box, Button):
                buttons.append(player_box)

        return buttons
