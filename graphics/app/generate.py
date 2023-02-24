import os

# Import ImageFont for Fonts
from PIL import Image, ImageDraw, ImageFont

from graphics.definitions import (FONTS_DIR, OUTPUT_DIR, RENDERS_DIR,
                                  THUMBNAIL_DIR)

SIZE = (1920, 1080)
CHARACTER_BOX = (960, 800)
POSITION = [(0, 140), (960, 140)]


def get_character_path(character: str, alt: str = "01") -> str:
    if character.lower() == "random":
        return os.path.join(RENDERS_DIR, "Random/Random.png")

    return os.path.join(RENDERS_DIR, f"{character}/{alt}.png")


def crop_character(image, crop) -> Image:
    img_width, img_height = image.size
    return image.crop(((img_width - crop[0]) // 2,
                       (img_height - crop[1]) // 2,
                       (img_width + crop[0]) // 2,
                       (img_height + crop[1]) // 2))


def resize_character(image) -> Image:
    width_one, height_one = image.size
    if width_one > 960:
        factor = 960 / width_one
        width_one = int(width_one * factor)
        height_one = int(height_one * factor)
    return image.resize((width_one, height_one))


def draw_thumbnail_text(text: str, into, center):
    multiple = 3

    # TODO: Make function that determines max size for font based on length of input str
    syncopate = ImageFont.truetype(os.path.join(FONTS_DIR, 'Syncopate-Bold.ttf'), 120 * multiple)
    wi, hi = syncopate.getsize(text)

    img = Image.new('RGBA', (wi, hi), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((wi / 2, hi / 2), text, (255, 255, 255), syncopate, anchor="mm")

    img = img.rotate(1.58, expand=True)
    img = img.resize((wi // multiple, hi // multiple), resample=Image.ANTIALIAS)

    into.alpha_composite(img, (center[0] - (wi // multiple // 2), center[1] + (hi // multiple // 2)))


def generate_thumbnail(data):
    canvas = Image.new('RGBA', SIZE)

    # Output Path
    output = os.path.join(OUTPUT_DIR, "test1.png")

    # TODO: This is allocating every time its run, move to constants
    # Paths to Template Items
    background_path = os.path.join(THUMBNAIL_DIR, "Thumbnail-Background.png")
    vs_path = os.path.join(THUMBNAIL_DIR, "Thumbnail-VS-01.png")
    tournament_path = os.path.join(THUMBNAIL_DIR, data["tournament"])
    character_background_path = os.path.join(tournament_path, "Thumbnail-CharacterBackground.png")
    text_background_path = os.path.join(tournament_path, "Thumbnail-TextBackground.png")
    character_paths = [get_character_path(data["players"][0]["character"], data["players"][0]["alt"]),
                       get_character_path(data["players"][1]["character"], data["players"][1]["alt"])]

    # Background
    background = Image.open(background_path, mode="r")
    canvas.paste(background)

    # Character Background
    character_background = Image.open(character_background_path, mode="r")
    canvas.alpha_composite(character_background)

    # TODO: This needs to be a loop or a function
    # Player 1 Character
    character_one = Image.open(character_paths[0], mode="r")
    character_one = resize_character(character_one)
    character_one = crop_character(character_one, CHARACTER_BOX)
    canvas.alpha_composite(character_one, POSITION[0])

    # Player 2 Character
    character_two = Image.open(character_paths[1], mode="r")
    character_two = resize_character(character_two)
    character_two = crop_character(character_two, CHARACTER_BOX)
    canvas.alpha_composite(character_two, POSITION[1])

    # Text Background
    text_background = Image.open(text_background_path, mode="r")
    canvas.alpha_composite(text_background)

    # VS
    vs = Image.open(vs_path, mode="r")
    canvas.alpha_composite(vs)

    # Text
    draw_thumbnail_text("NIFARES", canvas, (480, 56))
    draw_thumbnail_text("PARZ", canvas, (1440, 56))
    draw_thumbnail_text("GRAND FINALS", canvas, (480, 850))

    canvas.save(output, format="PNG")
