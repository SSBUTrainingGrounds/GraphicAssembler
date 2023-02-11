from PyQt6.QtWidgets import QMainWindow, QHBoxLayout

from graphics.ui.widgets.CreateButton import CreateButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TG Graphics")
        self.resize(400, 300)

        button = CreateButton()
        self.setCentralWidget(button)
