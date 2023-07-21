from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QScrollArea, QVBoxLayout, QWidget

from graphics.ui.widgets.PlayerBoxTop8 import PlayerAccordion
from graphics.utils.Types import Top8Data


class ScrollSidebar(QScrollArea):
    def __init__(self, data: Top8Data, parent=None):
        super().__init__()

        self.data = data
        self.parent_window = parent

        widget = QWidget()
        self.setWidget(widget)

        self.all_children = []
        layout = QVBoxLayout(widget)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        player_accordions: list[PlayerAccordion] = [
            PlayerAccordion(player, i, parent=self) for i, player in enumerate(data["players"])
        ]

        for player_accordion in player_accordions:
            layout.addWidget(player_accordion)
            self.all_children.append(player_accordion)

        self.setFixedWidth(400)
        self.setWidgetResizable(True)

    def all_dropdown(self):
        dropdowns = []
        for child in self.all_children:
            dropdowns.extend(child.all_dropdown())

        return dropdowns

    def all_textbox(self):
        textboxes = []
        for child in self.all_children:
            textboxes.extend(child.all_textbox())

        return textboxes

    def all_slider(self):
        sliders = []
        for child in self.all_children:
            sliders.extend(child.all_slider())

        return sliders

    def all_button(self):
        buttons = []
        for child in self.all_children:
            buttons.extend(child.all_button())

        return buttons
