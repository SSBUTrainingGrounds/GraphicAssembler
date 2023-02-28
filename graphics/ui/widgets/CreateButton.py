from PyQt6.QtWidgets import QPushButton

from graphics.app.generate import generate_thumbnail, save_image
from graphics.utils.types import TournamentData


class CreateButton(QPushButton):
    def __init__(self, data: TournamentData) -> None:
        super().__init__()
        self.data = data
        self.setText("Save")
        self.clicked.connect(self.button_handler)

    def button_handler(self) -> None:
        image = generate_thumbnail(self.data)
        save_image(image)
