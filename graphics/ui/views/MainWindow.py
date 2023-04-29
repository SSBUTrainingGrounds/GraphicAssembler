from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QGridLayout, QMainWindow, QPushButton, QWidget

from graphics.ui.views.ThumbnailWindow import ThumbnailWindow
from graphics.ui.views.Top8Window import Top8Window
from graphics.utils.Definitions import ASSET_DIR


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("TG Graphics Launcher")
        self.resize(300, 200)
        self.setWindowIcon(QIcon(ASSET_DIR + "/icon.png"))

        self.grid_layout = QGridLayout()

        self.thumbnail_button = QPushButton("Thumbnail")
        self.top8_button = QPushButton("Top 8")

        self.thumbnail_button.clicked.connect(self.thumbnail_button_clicked)
        self.top8_button.clicked.connect(self.top8_button_clicked)

        self.grid_layout.addWidget(self.thumbnail_button)
        self.grid_layout.addWidget(self.top8_button)

        widget = QWidget()

        widget.setLayout(self.grid_layout)

        self.setCentralWidget(widget)

    def thumbnail_button_clicked(self) -> None:
        self.new_window = ThumbnailWindow()
        self.new_window.show()

    def top8_button_clicked(self) -> None:
        self.new_window = Top8Window()
        self.new_window.show()
