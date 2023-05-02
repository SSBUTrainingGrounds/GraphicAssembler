from PIL.ImageFont import FreeTypeFont

from graphics.utils.Text import biggest_font_size


def test_biggest_font_size():
    font = biggest_font_size("Hello", "arial.ttf", (100, 100), 100)

    assert isinstance(font, FreeTypeFont)
    assert font.size == 44

    font = biggest_font_size("Hello", "arial.ttf", (50, 50), 50)

    assert font.size == 22

    font = biggest_font_size("Hello", "arial.ttf", (100, 100), 10)

    assert font.size == 10
