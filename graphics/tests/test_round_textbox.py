# type: ignore

from graphics.ui.widgets.RoundTextbox import RoundTextbox
from graphics.utils.Types import ThumbnailData


def test_round_textbox(qtbot):
    data: ThumbnailData = {
        "players": [],
        "round": "Winners Finals",
        "tournament": "tos",
    }

    widget = RoundTextbox(data)

    qtbot.addWidget(widget)

    assert widget.text() == "Winners Finals"

    widget.setText("Grand Finals")

    assert widget.text() == "Grand Finals"
