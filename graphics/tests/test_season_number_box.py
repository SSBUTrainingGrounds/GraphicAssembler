# type: ignore

from graphics.ui.widgets.SeasonNumberTextbox import SeasonNumberBox
from graphics.utils.Types import Top8Data


def test_season_number_textbox(qtbot):
    data: Top8Data = {
        "players": [],
        "date": "2021-09-25",
        "tournament": "tos",
        "entrants": 10,
        "number": 1,
        "season": 1,
    }

    widget = SeasonNumberBox(data)

    qtbot.addWidget(widget)

    assert data["season"] == 1
    assert data["number"] == 1

    widget.season.setText("2")
    widget.number.setText("2")

    assert data["season"] == 2
    assert data["number"] == 2
