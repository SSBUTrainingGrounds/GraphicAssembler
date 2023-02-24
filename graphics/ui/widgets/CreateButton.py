from PyQt6.QtWidgets import QComboBox, QPushButton

from graphics.app.generate import generate_thumbnail


class CreateButton(QPushButton):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.setText("Create")
        self.clicked.connect(self.button_handler)

    def button_handler(self):
        generate_thumbnail(self.data)
