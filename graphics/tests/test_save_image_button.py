# type: ignore

from graphics.app.ThumbnailGenerate import generate_thumbnail
from graphics.app.Top8Generate import generate_top8
from graphics.ui.widgets.SaveImageButton import SaveImageButton
from graphics.utils.Types import ThumbnailData, Top8Data


def test_save_image_button_thumbnail(qtbot):
    data: ThumbnailData = {
        "players": [
            {
                "name": "Player 1",
                "character": {
                    "name": "Fox",
                    "alt": "02",
                    "offset": (0, 0),
                    "zoom": 1,
                },
            },
            {
                "name": "Player 2",
                "character": {
                    "name": "Fox",
                    "alt": "01",
                    "offset": (0, 0),
                    "zoom": 1,
                },
            },
        ],
        "round": "Winners Finals",
        "tournament": "tos",
    }

    widget = SaveImageButton(data, generate_thumbnail, "thumbnail")

    qtbot.addWidget(widget)

    assert widget.text() == "Save Image"

    widget.setText("Saved!")

    assert widget.text() == "Saved!"

    widget.reset_button()

    assert widget.text() == "Save Image"

    # Not sure if it is a good idea to test actually saving the image.


def test_save_image_button_top8(qtbot):
    data: Top8Data = {
        "players": [],
        "tournament": "tos",
        "season": 1,
        "number": 1,
        "date": "2021-01-01",
        "entrants": 100,
    }

    widget = SaveImageButton(data, generate_top8, "top8")

    qtbot.addWidget(widget)

    assert widget.text() == "Save Image"

    widget.setText("Saved!")

    assert widget.text() == "Saved!"

    widget.reset_button()

    assert widget.text() == "Save Image"
