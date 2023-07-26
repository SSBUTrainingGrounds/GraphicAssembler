# for type hinting
from PyQt6.QtWidgets import QComboBox as Dropdown
from graphics.ui.widgets.OffsetSlider import OffsetSlider


def connect_character_dropdown(window, player_box) -> None:
    for child in player_box:
        if isinstance(child, Dropdown):
            child.currentTextChanged.connect(
                lambda: (window.timer.start(window.timer_duration))
            )


def connect_character_sliders(window, player_box) -> None:
    for child in player_box:
        if isinstance(child, OffsetSlider):
            for slider in child.all_children:
                slider.valueChanged.connect(
                    lambda: window.timer.start(window.timer_duration))
