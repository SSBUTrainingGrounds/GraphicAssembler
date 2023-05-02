# type: ignore

from graphics.ui.widgets.PlayerTwitter import PlayerTwitter
from graphics.utils.Types import Top8Player


def test_player_twitter(qtbot):
    player_data: Top8Player = {
        "name": "Test Player",
        "twitter": "test_player",
        "placement": 1,
        "main": {
            "name": "Mario",
            "alt": "01",
            "offset": (0, 0),
            "zoom": 100,
        },
    }

    widget = PlayerTwitter(player_data)

    assert widget.text() == "test_player"

    widget.setText("test_player_2")

    assert widget.text() == "test_player_2"
