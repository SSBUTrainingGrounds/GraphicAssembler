# type: ignore

from graphics.ui.widgets.TournamentDropdown import TournamentDropdown
from graphics.utils.Types import ThumbnailData, Top8Data


def test_tournament_dropdown_thumbnail(qtbot):
    data: ThumbnailData = {
        "date": "2021-09-25",
        "tournament": "tos",
        "number": 1,
        "season": 1,
    }

    widget = TournamentDropdown(data)

    qtbot.addWidget(widget)

    assert data["tournament"] == "tos"

    widget.get_selection("tos2")

    assert data["tournament"] == "tos2"


def test_tournament_dropdown_top8(qtbot):
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

    widget = TournamentDropdown(data)

    qtbot.addWidget(widget)

    assert data["tournament"] == "tos"

    widget.get_selection("tos2")

    assert data["tournament"] == "tos2"
