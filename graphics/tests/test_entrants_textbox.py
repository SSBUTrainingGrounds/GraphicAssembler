# type: ignore

from graphics.ui.widgets.EntrantsTextbox import EntrantsTextbox
from graphics.utils.Types import Top8Data


def test_entrants_textbox(qtbot):
    data: Top8Data = {
        "players": [],
        "tournament": "Test Tournament",
        "season": 1,
        "number": 1,
        "date": "2021-01-01",
        "entrants": 100,
    }

    widget = EntrantsTextbox(data)

    qtbot.addWidget(widget)

    assert widget.data["entrants"] == 100

    widget.setText("200")
    widget.update()

    assert widget.data["entrants"] == 200
