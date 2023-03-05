from PIL import ImageFont
from PIL.ImageFont import FreeTypeFont


def biggest_font_size(
    text: str, font_path: str, box_size: tuple[int, int], guess: int
) -> FreeTypeFont:
    font = ImageFont.truetype(font_path, guess)
    while (font.getsize(text)[0] > box_size[0]) or (
        font.getsize(text)[1] > box_size[1]
    ):
        guess -= 1
        font = ImageFont.truetype(font_path, guess)

    return font
