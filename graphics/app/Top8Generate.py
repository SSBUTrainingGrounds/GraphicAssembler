import os

# Import ImageFont for Fonts
from PIL import Image, ImageDraw, ImageFont

# This is only used for type hinting
from PIL.Image import Image as ImageType

from graphics.utils.CharacterImage import generate_character_image, get_character_path
from graphics.utils.Definitions import FONTS_DIR, OUTPUT_DIR, TOP8_DIR
from graphics.utils.Text import biggest_font_size
from graphics.utils.Types import Top8Data

SIZE = (1200, 800)


def generate_top8(data: Top8Data) -> ImageType:
    canvas = Image.new("RGBA", SIZE)
    draw = ImageDraw.Draw(canvas)

    tournament_path = os.path.join(TOP8_DIR, data["tournament"])
    background_path = os.path.join(tournament_path, "Top8-Background-01.png")
    footer_path = os.path.join(tournament_path, "Top8-Footer-01.png")
    header_path = os.path.join(tournament_path, "Top8-Header-01.png")

    # background
    background = Image.open(background_path, mode="r")
    canvas.paste(background)

    # footer
    footer = Image.open(footer_path, mode="r")
    canvas.alpha_composite(footer)

    # header
    header = Image.open(header_path, mode="r")
    canvas.alpha_composite(header)

    # header text
    tournament_number = f"S{data['season']} T{data['number']}"
    syncopate = ImageFont.truetype(os.path.join(FONTS_DIR, "Syncopate-Regular.ttf"), 23)

    draw.text((687, 150), tournament_number, (255, 255, 255), syncopate)
    draw.text((910, 150), data['date'], (255, 255, 255), syncopate, align="right", anchor="ra")

    entrant_number = f"{data['entrants']} ENTRANTS"
    entrant_size = biggest_font_size(entrant_number, os.path.join(FONTS_DIR, "Syncopate-Regular.ttf"), (174, 25), 23)
    draw.text((943, 150), entrant_number, (255, 255, 255), entrant_size)

    return canvas
