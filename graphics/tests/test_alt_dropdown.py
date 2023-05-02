# type: ignore

from graphics.ui.widgets.AltDropdown import AltDropdown
from graphics.utils.Types import ThumbnailPlayer, Top8Player


def test_alt_dropdown_thumbnail(qtbot):
    player_data: ThumbnailPlayer = {
        "tag": "TestPlayer",
        "character": {
            "name": "Fox",
            "alt": "01",
            "offset": (0, 0),
            "zoom": 100,
        },
    }

    widget = AltDropdown(player_data)

    qtbot.addWidget(widget)

    assert widget.player_data["character"]["alt"] == "01"

    widget.setCurrentText("02")

    assert widget.player_data["character"]["alt"] == "02"

    widget.reset()

    assert widget.player_data["character"]["alt"] == "01"

    widget.get_selection("03")

    assert widget.player_data["character"]["alt"] == "03"


def test_alt_dropdown_top8(qtbot):
    player_data: Top8Player = {
        "tag": "TestPlayer",
        "twitter": "TestPlayer",
        "placement": 1,
        "main": {
            "name": "Fox",
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

    widget = AltDropdown(player_data, "main")

    qtbot.addWidget(widget)

    assert widget.player_data["main"]["alt"] == "01"

    widget.setCurrentText("02")

    assert widget.player_data["main"]["alt"] == "02"
