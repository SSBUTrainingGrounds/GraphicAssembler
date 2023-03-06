from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QScrollArea, QVBoxLayout, QWidget

from graphics.ui.widgets.PlayerBoxTop8 import PlayerAccordion
from graphics.utils.types import Top8Data


class ScrollSidebar(QScrollArea):
    def __init__(self, data: Top8Data):
        super().__init__()

        self.data = data

        widget = QWidget()
        self.setWidget(widget)

        layout = QVBoxLayout(widget)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        player_accordions: list[PlayerAccordion] = []

        for i, player in enumerate(data["players"]):
            player_accordions.append(PlayerAccordion(player, i))

        for i, player_accordion in enumerate(player_accordions):
            layout.addWidget(player_accordion)

        self.setFixedWidth(400)
        self.setWidgetResizable(True)
