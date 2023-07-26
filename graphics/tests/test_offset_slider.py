# type: ignore

from graphics.ui.widgets.OffsetSlider import OffsetSlider
from graphics.utils.Types import ThumbnailPlayer, Top8Player


def test_offset_slider_thumbnail(qtbot):
    player_data: ThumbnailPlayer = {
        "tag": "TestPlayer",
        "character": {
            "name": "Falco",
            "alt": "01",
            "offset": (0, 0),
            "zoom": 100,
        },
    }

    widget = OffsetSlider(player_data)

    qtbot.addWidget(widget)

    assert widget.player_data["character"]["offset"] == (0, 0)

    widget.horizontal_slider.setValue(50)
    widget.vertical_slider.setValue(50)

    assert widget.player_data["character"]["offset"] == (50, 50)

    widget.zoom_slider.setValue(90)

    assert widget.player_data["character"]["zoom"] == 90

    widget.zoom_slider.setValue(50)

    assert widget.player_data["character"]["zoom"] == 80

    widget.horizontal_slider.setValue(-400)

    assert widget.player_data["character"]["offset"] == (-400, 50)

    widget.vertical_slider.setValue(-2900)

    assert widget.player_data["character"]["offset"] == (-400, -999)

    widget.reset()

    assert widget.player_data["character"]["offset"] == (0, 0)
    assert widget.player_data["character"]["zoom"] == 100


def test_offset_slider_top8(qtbot):
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

    widget = OffsetSlider(player_data, "main")

    qtbot.addWidget(widget)

    assert widget.player_data["main"]["offset"] == (0, 0)

    widget.horizontal_slider.setValue(50)
    widget.vertical_slider.setValue(50)

    assert widget.player_data["main"]["offset"] == (50, 50)

    widget.zoom_slider.setValue(90)

    assert widget.player_data["main"]["zoom"] == 90

    widget.zoom_slider.setValue(50)

    assert widget.player_data["main"]["zoom"] == 80

    widget.horizontal_slider.setValue(-400)

    assert widget.player_data["main"]["offset"] == (-400, 50)

    widget.vertical_slider.setValue(-2900)

    assert widget.player_data["main"]["offset"] == (-400, -999)

    widget.reset()

    assert widget.player_data["main"]["offset"] == (0, 0)
    assert widget.player_data["main"]["zoom"] == 100
