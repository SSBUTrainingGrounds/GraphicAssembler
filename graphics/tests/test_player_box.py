# type: ignore

from PyQt6.QtCore import Qt

from graphics.ui.widgets.PlayerBoxThumbnail import PlayerBox
from graphics.ui.widgets.PlayerBoxTop8 import PlayerAccordion
from graphics.utils.Types import ThumbnailPlayer, Top8Player


def test_player_box_thumbnail(qtbot):
    player_data: ThumbnailPlayer = {
        "tag": "TestPlayer",
        "character": {
            "name": "Falco",
            "alt": "01",
            "offset": (0, 0),
            "zoom": 100,
        },
    }

    widget = PlayerBox(player_data, 1)

    qtbot.addWidget(widget)

    assert len(widget.children()) == 9

    assert widget.player_data["tag"] == "TestPlayer"
    assert widget.player_data["character"]["name"] == "Falco"
    assert widget.player_data["character"]["alt"] == "01"
    assert widget.player_data["character"]["offset"] == (0, 0)
    assert widget.player_data["character"]["zoom"] == 100

    widget.offset_sliders.horizontal_slider.setValue(50)

    assert widget.player_data["character"]["offset"] == (50, 0)

    widget.reset()

    assert widget.player_data["character"]["offset"] == (0, 0)


def test_player_box_top8(qtbot):
    player_data: Top8Player = {
        "tag": "TestPlayer",
        "twitter": "TestPlayer",
        "main": {
            "name": "Falco",
            "alt": "01",
            "offset": (0, 0),
            "zoom": 100,
        },
        "secondary": {
            "name": "Falco",
            "alt": "01",
            "offset": (0, 0),
            "zoom": 100,
        },
    }

    widget = PlayerAccordion(player_data, 1)

    qtbot.addWidget(widget)

    assert len(widget.children()) == 12

    assert widget.data["tag"] == "TestPlayer"

    widget.tag_textbox.setText("NewTag")

    assert widget.data["tag"] == "NewTag"

    widget.add_character.click()

    assert len(widget.children()) == 16

    assert widget.toggle_button.arrowType() == Qt.ArrowType.RightArrow

    widget.toggle_button.click()

    assert widget.toggle_button.arrowType() == Qt.ArrowType.DownArrow
    assert widget.children()[1].isVisible() is False
