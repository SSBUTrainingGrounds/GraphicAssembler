from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QPushButton

from graphics.app.generate import generate_thumbnail, save_image
from graphics.utils.types import ThumnbailData


class CreateButton(QPushButton):
    def __init__(self, data: ThumnbailData) -> None:
        super().__init__()
        self.data = data
        self.setText("Save Image")
        self.clicked.connect(self.button_handler)
        self.timer = QTimer()
        self.timer.timeout.connect(self.reset_button)

    def reset_button(self) -> None:
        self.setText("Save Image")

    def button_handler(self) -> None:
        image = generate_thumbnail(self.data)
        save_image(image)
        self.setText("Saved!")
        self.timer.start(1000)
