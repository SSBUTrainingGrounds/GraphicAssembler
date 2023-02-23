from PyQt6.QtWidgets import QComboBox, QPushButton

from graphics.app.generate import generate_thumbnail


class CreateButton(QPushButton):
    def __init__(
        self,
        character_dropdown_one: QComboBox,
        character_dropdown_two: QComboBox,
        alt_dropdown_one: QComboBox,
        alt_dropdown_two: QComboBox,
    ):
        super().__init__()
        self.character_dropdown_one = character_dropdown_one
        self.character_dropdown_two = character_dropdown_two
        self.alt_dropdown_one = alt_dropdown_one
        self.alt_dropdown_two = alt_dropdown_two

        self.setText("Create")
        self.clicked.connect(self.button_handler)

    def button_handler(self):
        generate_thumbnail(
            "tos",
            self.character_dropdown_one.currentText(),
            self.character_dropdown_two.currentText(),
            self.alt_dropdown_one.currentText(),
            self.alt_dropdown_two.currentText(),
        )
