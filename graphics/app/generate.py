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
    # The Mii Fighters only have one alt.
    if "mii" in character.lower():
        alt = "01"

    return os.path.join(RENDERS_DIR, f"{character}/{alt}.png")


def crop_character(image: Image, crop: tuple[int, int]) -> Image:
    img_width, img_height = image.size
    # Crop from the Top of the Image to not cut off Face
    return image.crop(((img_width - crop[0]) // 2,
                       0,
                       (img_width + crop[0]) // 2,
                       crop[1]))


def resize_character(image: Image) -> Image:
    width_one, height_one = image.size
    if width_one > 960:
        factor = 960 / width_one
        width_one = int(width_one * factor)
        height_one = int(height_one * factor)
    return image.resize((width_one, height_one))


def generate_character_image(path: str) -> Image:
    character = Image.open(path, mode="r")
    character = resize_character(character)
    character = crop_character(character, CHARACTER_BOX)
    return character


def biggest_font_size(text: str, font_path, box_size, guess) -> ImageFont:
    font = ImageFont.truetype(font_path, guess)
    while (font.getsize(text)[0] > box_size[0]) or (font.getsize(text)[1] > box_size[1]):
        guess -= 1
        font = ImageFont.truetype(font_path, guess)

    return font


def draw_thumbnail_text(text: str, into: Image, center: tuple[int, int]):

    # multiple is added because rotating causes image to become jagged
    # sizing it down with the Image.ANTIALIAS flag smooths it out
    multiple = 3

    syncopate = biggest_font_size(text, os.path.join(FONTS_DIR, 'Syncopate-Bold.ttf'), (930 * multiple, 120 * multiple),
                                  130 * multiple)

    width, height = syncopate.getsize(text)
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, (255, 255, 255), syncopate)
    _, h = draw.textsize(text, font=syncopate)
    h = h // multiple

    img = img.rotate(1.6, expand=True)
    width = img.size[0] // multiple
    height = img.size[1] // multiple
    img = img.resize((width, height), resample=Image.ANTIALIAS)

    into.alpha_composite(img, (
        center[0] - width // 2,
        center[1] + (height - h) // 2))


def generate_thumbnail(data) -> Image:
    player_left = data["players"][0]
    player_right = data["players"][1]

    canvas = Image.new('RGBA', SIZE)

    # Output Path
    output = os.path.join(OUTPUT_DIR, "test1.png")

    # TODO: This is allocating every time its run, make constant
    # Paths to Template Items
    background_path = os.path.join(THUMBNAIL_DIR, "Thumbnail-Background.png")
    vs_path = os.path.join(THUMBNAIL_DIR, "Thumbnail-VS-01.png")
    tournament_path = os.path.join(THUMBNAIL_DIR, data["tournament"])
    character_background_path = os.path.join(tournament_path, "Thumbnail-CharacterBackground.png")
    text_background_path = os.path.join(tournament_path, "Thumbnail-TextBackground.png")
    character_paths = [get_character_path(player_left["character"], player_left["alt"]),
                       get_character_path(player_right["character"], player_right["alt"])]

    # Background
    background = Image.open(background_path, mode="r")
    canvas.paste(background)

    # Character Background
    character_background = Image.open(character_background_path, mode="r")
    canvas.alpha_composite(character_background)

    # Player 1 Character
    canvas.alpha_composite(generate_character_image(character_paths[0]), POSITION[0])

    # Player 2 Character
    canvas.alpha_composite(generate_character_image(character_paths[1]), POSITION[1])

    # Text Background
    text_background = Image.open(text_background_path, mode="r")
    canvas.alpha_composite(text_background)

    # VS
    vs = Image.open(vs_path, mode="r")
    canvas.alpha_composite(vs)

    # Text
    draw_thumbnail_text("STRAWBERRY", canvas, (480, 85))
    draw_thumbnail_text("PARZ", canvas, (1440, 85))
    draw_thumbnail_text("GRAND FINALS", canvas, (480, 875))
    draw_thumbnail_text("SMASH OVERSEAS", canvas, (1440, 875))

    return canvas


def save_image(canvas: Image):
    # Output Path
    output = os.path.join(OUTPUT_DIR, "test1.png")

    canvas.save(output, format="PNG")
