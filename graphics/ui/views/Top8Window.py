from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QWidget

from graphics.utils.definitions import ASSET_DIR


class Top8Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("TG Graphics (Top 8)")
        self.resize(800, 700)
        self.setWindowIcon(QIcon(ASSET_DIR + "/icon.png"))

        self.grid = QGridLayout()

        layout = QHBoxLayout()

        self.placeholder = QLabel("Placeholder")

        layout.addWidget(self.placeholder)

        self.setLayout(layout)
