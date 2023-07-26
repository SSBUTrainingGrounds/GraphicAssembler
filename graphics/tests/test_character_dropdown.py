# type: ignore

from graphics.ui.widgets.CharacterDropdown import CharacterDropdown
from graphics.utils.Types import ThumbnailPlayer, Top8Player  # type: ignore


def test_character_dropdown_thumbnail(qtbot):
    player_data: ThumbnailPlayer = {
        "tag": "TestPlayer",
        "character": {
            "name": "Falco",
            "alt": "01",
            "offset": (0, 0),
            "zoom": 100,
        },
    }

    widget = CharacterDropdown(player_data)

    qtbot.addWidget(widget)

    assert widget.player_data["character"]["name"] == "Falco"

    widget.get_selection("Fox")

    assert widget.player_data["character"]["name"] == "Fox"

    widget.get_selection("Falco")

    assert widget.player_data["character"]["name"] == "Falco"


def test_character_dropdown_top8(qtbot):
    player_data: Top8Player = {
        "tag": "TestPlayer",
        "twitter": "TestPlayer",
        "placement": 1,
        "main": {
            "name": "Falco",
            "alt": "01",
            "offset": (0, 0),
            "zoom": 100,
        },
        "secondary": {
            "name": "Fox",
            "alt": "01",
            "offset": (0, 0),
            "zoom": 100,
        },
    }

    widget = CharacterDropdown(player_data, "main")

    qtbot.addWidget(widget)

    assert widget.player_data["main"]["name"] == "Falco"

    widget.get_selection("Fox")

    assert widget.player_data["main"]["name"] == "Fox"

    widget.get_selection("Falco")

    assert widget.player_data["main"]["name"] == "Falco"
