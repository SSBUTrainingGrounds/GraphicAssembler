import os

# Import ImageFont for Fonts
from PIL import Image, ImageDraw, ImageFont

# This is only used for type hinting
from PIL.Image import Image as ImageType

from graphics.utils.CharacterImage import generate_character_image, get_character_path
from graphics.utils.Definitions import FONTS_DIR, OUTPUT_DIR, TOP8_DIR
from graphics.utils.Text import biggest_font_size
from graphics.utils.Types import Top8Data


def generate_top8(data: Top8Data):  # -> ImageType:
    players = data["players"]
