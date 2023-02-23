from PyQt6.QtWidgets import QHBoxLayout, QMainWindow, QWidget

from graphics.ui.widgets.AltDropdown import AltDropdown
from graphics.ui.widgets.CharacterDropdown import CharacterDropdown
from graphics.ui.widgets.CreateButton import CreateButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TG Graphics")
        self.resize(400, 300)

        character_dropdown_one = CharacterDropdown()
        character_dropdown_two = CharacterDropdown()
        alt_dropdown_one = AltDropdown()
        alt_dropdown_two = AltDropdown()

        button = CreateButton(
            character_dropdown_one,
            character_dropdown_two,
            alt_dropdown_one,
            alt_dropdown_two,
        )

        layout = QHBoxLayout()

        layout.addWidget(character_dropdown_one)
        layout.addWidget(alt_dropdown_one)
        layout.addWidget(character_dropdown_two)
        layout.addWidget(alt_dropdown_two)
        layout.addWidget(button)

        widget = QWidget()

        widget.setLayout(layout)

        self.setCentralWidget(widget)
