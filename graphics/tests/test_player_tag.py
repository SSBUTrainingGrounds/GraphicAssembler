# type: ignore

from graphics.ui.widgets.PlayerTag import PlayerTag
from graphics.utils.Types import ThumbnailPlayer, Top8Player


def test_player_tag_thumbnail(qtbot):
    player_data: ThumbnailPlayer = {
        "tag": "TestPlayer",
        "character": {
            "name": "Falco",
            "alt": "01",
            "offset": (0, 0),
            "zoom": 100,
        },
    }

    widget = PlayerTag(player_data)

    qtbot.addWidget(widget)

    assert widget.player["tag"] == "TestPlayer"

    widget.setText("NewPlayer")

    assert widget.player["tag"] == "NewPlayer"


def test_player_tag_top8(qtbot):
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

    widget = PlayerTag(player_data)

    qtbot.addWidget(widget)

    assert widget.player["tag"] == "TestPlayer"

    widget.setText("NewPlayer")

    assert widget.player["tag"] == "NewPlayer"
