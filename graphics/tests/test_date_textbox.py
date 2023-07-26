# type: ignore

from graphics.ui.widgets.DateTextbox import DateTextbox


def test_date_textbox(qtbot):
    data = {"date": "2021-01-01"}
    date_textbox = DateTextbox(data)

    qtbot.addWidget(date_textbox)

    assert date_textbox.text() == "2021-01-01"
    assert data["date"] == "2021-01-01"

    date_textbox.setText("2021-01-02")

    assert date_textbox.text() == "2021-01-02"
    assert data["date"] == "2021-01-02"
