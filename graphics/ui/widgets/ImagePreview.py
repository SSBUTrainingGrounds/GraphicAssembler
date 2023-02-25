from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel

from graphics.app.generate import generate_thumbnail


class ImagePreview(QLabel):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.setPixmap(
            QPixmap(generate_thumbnail(self.data).toqpixmap()).scaledToHeight(
                300, mode=Qt.TransformationMode.SmoothTransformation
            )
        )

    def update(self):
        self.setPixmap(
            QPixmap(generate_thumbnail(self.data).toqpixmap()).scaledToHeight(
                300, mode=Qt.TransformationMode.SmoothTransformation
            )
        )
