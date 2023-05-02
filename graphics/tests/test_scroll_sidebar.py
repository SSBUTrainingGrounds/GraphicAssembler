# type: ignore

from graphics.ui.widgets.ScrollSidebar import ScrollSidebar
from graphics.utils.Types import Top8Data


def test_scroll_sidebar(qtbot):
    data: Top8Data = {
        "players": [
            {"tag": "Player 1"},
            {"tag": "Player 2"},
            {"tag": "Player 3"},
            {"tag": "Player 4"},
            {"tag": "Player 5"},
            {"tag": "Player 6"},
            {"tag": "Player 7"},
            {"tag": "Player 8"},
        ],
        "date": "2021-09-25",
        "tournament": "tos",
        "entrants": 10,
        "number": 1,
        "season": 1,
    }

    widget = ScrollSidebar(data)

    qtbot.addWidget(widget)

    assert widget.width() == 400

    assert len(widget.children()) == 3
