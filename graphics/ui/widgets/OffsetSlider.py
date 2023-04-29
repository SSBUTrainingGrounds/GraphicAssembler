from typing import Optional

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QLabel, QSlider, QWidget

from graphics.utils.Types import ThumbnailPlayer, Top8Player


class OffsetSlider(QWidget):
    def __init__(
            self,
            player_data: ThumbnailPlayer | Top8Player,
            character_type: Optional[str] = None,
    ) -> None:
        super().__init__()

        self.player_data = player_data

        self.character_type = character_type

        if not self.character_type:
            self.character_type = "character"

        self.horizontal_slider = HorizontalSlider(player_data, character_type)
        self.vertical_slider = VerticalSlider(player_data, character_type)
        self.zoom_slider = ZoomSlider(player_data, character_type)

        self.all_children: list[HorizontalSlider | VerticalSlider | ZoomSlider] = [
            self.horizontal_slider,
            self.vertical_slider,
            self.zoom_slider,
        ]

        self.zoom_label = QLabel("Zoom: (100%)")
        self.offset_x_label = QLabel("Offset X: (+000)")
        self.offset_y_label = QLabel("Offset Y: (+000)")

        self.grid_layout = QGridLayout()

        self.grid_layout.addWidget(self.zoom_label, 0, 0)
        self.grid_layout.addWidget(self.zoom_slider, 1, 0)
        self.grid_layout.addWidget(self.offset_x_label, 0, 1)
        self.grid_layout.addWidget(self.horizontal_slider, 1, 1)
        self.grid_layout.addWidget(self.offset_y_label, 0, 2)
        self.grid_layout.addWidget(self.vertical_slider, 1, 2)

        self.horizontal_slider.valueChanged.connect(
            lambda: self.offset_x_label.setText(
                f"Offset X: ({player_data[f'{self.character_type}']['offset'][0]:+04d})"
            )
        )
        self.vertical_slider.valueChanged.connect(
            lambda: self.offset_y_label.setText(
                f"Offset Y: ({player_data[f'{self.character_type}']['offset'][1]:+04d})"
            )
        )
        self.zoom_slider.valueChanged.connect(
            lambda: self.zoom_label.setText(
                f"Zoom: ({player_data[f'{self.character_type}']['zoom']}%)"
            )
        )

        self.setLayout(self.grid_layout)

    def reset(self) -> None:
        for child in self.all_children:
            child.reset()


class HorizontalSlider(QSlider):
    def __init__(
            self,
            player_data: ThumbnailPlayer | Top8Player,
            character_type: Optional[str] = None,
    ) -> None:
        super().__init__()

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.player_data = player_data
        self.character_type = character_type

        if not self.character_type:
            self.character_type = "character"

        self.setOrientation(Qt.Orientation.Horizontal)
        self.setMinimum(-999)
        self.setMaximum(999)
        self.setSingleStep(1)
        self.setValue(0)
        self.valueChanged.connect(self.get_selection)

    def get_selection(self, value: int) -> None:
        self.player_data[f"{self.character_type}"]["offset"] = (
            value,
            self.player_data[f"{self.character_type}"]["offset"][1],
        )

    def reset(self):
        self.setValue(0)

    def wheelEvent(self, event) -> None:
        if self.hasFocus():
            return QSlider.wheelEvent(self, event)
        else:
            event.ignore()


class VerticalSlider(QSlider):
    def __init__(
            self,
            player_data: ThumbnailPlayer | Top8Player,
            character_type: Optional[str] = None,
    ) -> None:
        super().__init__()

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.player_data = player_data
        self.character_prefix = character_type

        if not self.character_prefix:
            self.character_prefix = "character"

        self.setOrientation(Qt.Orientation.Vertical)
        self.setMinimum(-999)
        self.setMaximum(999)
        self.setSingleStep(1)
        self.setValue(0)
        self.valueChanged.connect(self.get_selection)

    def get_selection(self, value: int) -> None:
        self.player_data[f"{self.character_prefix}"]["offset"] = (
            self.player_data[f"{self.character_prefix}"]["offset"][0],
            value,
        )

    def reset(self) -> None:
        self.setValue(0)

    def wheelEvent(self, event) -> None:
        if self.hasFocus():
            return QSlider.wheelEvent(self, event)
        else:
            event.ignore()


class ZoomSlider(QSlider):
    def __init__(
            self,
            player_data: ThumbnailPlayer | Top8Player,
            character_type: Optional[str] = None,
    ) -> None:
        super().__init__()

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.player_data = player_data
        self.character_type = character_type

        if not self.character_type:
            self.character_type = "character"

        self.setOrientation(Qt.Orientation.Horizontal)
        self.setMinimum(80)
        self.setMaximum(250)
        self.setSingleStep(1)
        self.setValue(100)
        self.valueChanged.connect(self.get_selection)

    def get_selection(self, value: int) -> None:
        self.player_data[f"{self.character_type}"]["zoom"] = value

    def reset(self) -> None:
        self.setValue(100)

    def wheelEvent(self, event) -> None:
        if self.hasFocus():
            return QSlider.wheelEvent(self, event)
        else:
            event.ignore()
