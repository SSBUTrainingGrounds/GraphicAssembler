from PIL import ImageFont, ImageDraw
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


def draw_with_kerning(
        draw: ImageDraw, location: tuple[int, int], text: str, color: tuple[int, int, int], font: FreeTypeFont,
        box_size: tuple[int, int], padding: int = 0) -> None:
    total_text_width, total_text_height = draw.textsize(text, font=font)
    width_difference = box_size[0] - padding - total_text_width
    gap_width = int(width_difference / (len(text) - 1))
    x_pos = location[0] + padding / 2
    for letter in text:
        draw.text((x_pos, location[1]), letter, color, font=font)
        letter_width, letter_height = draw.textsize(letter, font=font)
        x_pos += letter_width + gap_width
