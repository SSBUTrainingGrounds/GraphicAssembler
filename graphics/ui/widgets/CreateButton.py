from PyQt6.QtWidgets import QPushButton

from graphics.app.generate import generate_thumbnail, save_image


class CreateButton(QPushButton):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.setText("Create")
        self.clicked.connect(self.button_handler)

    def button_handler(self):
        image = generate_thumbnail(self.data)
        save_image(image)
