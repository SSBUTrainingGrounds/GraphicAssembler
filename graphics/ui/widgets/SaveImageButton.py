from typing import Any, Callable

from PIL.Image import Image as ImageType
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QPushButton

from graphics.app.generate import save_image
from graphics.utils.types import ThumbnailData, Top8Data


class SaveImageButton(QPushButton):
    def __init__(
        self,
        data: ThumbnailData | Top8Data,
        generate_img_fn: Callable[[Any], ImageType],
        img_name: str,
    ) -> None:
        super().__init__()
        self.data = data
        self.generate_img_fn = generate_img_fn
        self.img_name = img_name
        self.setText("Save Image")
        self.clicked.connect(self.button_handler)

        # When we click the button, we want to change the text to "Saved!" for 1 second
        # Then we want to change it back to "Save Image"
        self.timer = QTimer()
        self.timer.timeout.connect(self.reset_button)

    def reset_button(self) -> None:
        self.setText("Save Image")

    def button_handler(self) -> None:
        image = self.generate_img_fn(self.data)
        save_image(image, self.img_name)
        self.setText("Saved!")
        self.timer.start(1000)
