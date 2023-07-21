import os.path
from typing import Any, Callable

from PIL.Image import Image as ImageType
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QPushButton, QFileDialog

from graphics.utils.SettingsManager import settings_manager
from graphics.utils.Types import ThumbnailData, Top8Data


class SaveImageButton(QPushButton):
    def __init__(
            self,
            data: ThumbnailData | Top8Data,
            generate_img_fn: Callable[[Any], ImageType],
    ) -> None:
        super().__init__()
        self.data = data
        self.generate_img_fn = generate_img_fn
        self.setText("Save Image")
        self.clicked.connect(self.button_handler)

        # When we click the button, we want to change the text to "Saved!" for 1 second
        # Then we want to change it back to "Save Image"
        self.timer = QTimer()
        self.timer.timeout.connect(self.reset_button)

    def reset_button(self) -> None:
        self.setText("Save Image")

    def button_handler(self) -> None:
        output = settings_manager.get_setting_value("output_dir")
        default_name = os.path.join(output, "graphic")
        image = self.generate_img_fn(self.data)
        path = QFileDialog.getSaveFileName(self, 'Save File', default_name, "PNG (*.png)")
        image.save(path[0], format="PNG")
        self.setText("Saved!")
        self.timer.start(1000)
