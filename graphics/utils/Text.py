from PIL import ImageFont


def biggest_font_size(text: str, font_path, box_size, guess) -> ImageFont:
    font = ImageFont.truetype(font_path, guess)
    while (font.getsize(text)[0] > box_size[0]) or (font.getsize(text)[1] > box_size[1]):
        guess -= 1
        font = ImageFont.truetype(font_path, guess)

    return font

