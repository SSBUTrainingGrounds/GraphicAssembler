from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QLabel, QSlider, QWidget

from graphics.utils.types import PlayerData


class OffsetSlider(QWidget):
    def __init__(self, player_data: PlayerData) -> None:
        super().__init__()
        self.player_data = player_data

        self.horizontal_slider = HorizontalSlider(player_data)
        self.vertical_slider = VerticalSlider(player_data)
        self.zoom_slider = ZoomSlider(player_data)

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
                f"Offset X: ({player_data['offset'][0]:+04d})"
            )
        )
        self.vertical_slider.valueChanged.connect(
            lambda: self.offset_y_label.setText(
                f"Offset Y: ({player_data['offset'][1]:+04d})"
            )
        )
        self.zoom_slider.valueChanged.connect(
            lambda: self.zoom_label.setText(f"Zoom: ({player_data['zoom']}%)")
        )

        self.setLayout(self.grid_layout)

    def reset(self) -> None:
        for child in self.all_children:
            child.reset()


class HorizontalSlider(QSlider):
    def __init__(self, player_data: PlayerData) -> None:
        super().__init__()
        self.player_data = player_data
        self.setOrientation(Qt.Orientation.Horizontal)
        self.setMinimum(-999)
        self.setMaximum(999)
        self.setSingleStep(1)
        self.setValue(0)
        self.valueChanged.connect(self.get_selection)

    def get_selection(self, value: int) -> None:
        self.player_data["offset"] = (value, self.player_data["offset"][1])

    def reset(self):
        self.setValue(0)


class VerticalSlider(QSlider):
    def __init__(self, player_data: PlayerData) -> None:
        super().__init__()
        self.player_data = player_data
        self.setOrientation(Qt.Orientation.Vertical)
        self.setMinimum(-999)
        self.setMaximum(999)
        self.setSingleStep(1)
        self.setValue(0)
        self.valueChanged.connect(self.get_selection)

    def get_selection(self, value: int) -> None:
        self.player_data["offset"] = (self.player_data["offset"][0], value)

    def reset(self) -> None:
        self.setValue(0)


class ZoomSlider(QSlider):
    def __init__(self, player_data: PlayerData) -> None:
        super().__init__()
        self.player_data = player_data
        self.setOrientation(Qt.Orientation.Horizontal)
        self.setMinimum(80)
        self.setMaximum(250)
        self.setSingleStep(1)
        self.setValue(100)
        self.valueChanged.connect(self.get_selection)

    def get_selection(self, value: int) -> None:
        self.player_data["zoom"] = value

    def reset(self) -> None:
        self.setValue(100)
