import os
from graphics.definitions import THUMBNAIL_DIR, RENDERS_DIR, OUTPUT_DIR

# Import ImageFont for Fonts
from PIL import Image, ImageDraw

def crop_character(image, crop):
    img_width, img_height = image.size
    return image.crop(((img_width - crop[0]) // 2,
                       (img_height - crop[1]) // 2,
                       (img_width + crop[0]) // 2,
                       (img_height + crop[1]) // 2))


def generate_thumbnail(tournament):
    SIZE = (1920, 1080)
    CHARACTER_BOX = (960, 800)

    canvas = Image.new('RGBA', SIZE, (0, 0, 0))
    draw = ImageDraw.Draw(canvas)

    # Output Path
    output = os.path.join(OUTPUT_DIR, "test1.png")

    # Paths to Template Items
    background_path = os.path.join(THUMBNAIL_DIR, "Thumbnail-Background.png")
    vs_path = os.path.join(THUMBNAIL_DIR, "Thumbnail-VS-01.png")
    tournament_path = os.path.join(THUMBNAIL_DIR, tournament)
    character_background_path = os.path.join(tournament_path, "Thumbnail-CharacterBackground.png")
    text_background_path = os.path.join(tournament_path, "Thumbnail-TextBackground.png")
    character_paths = [os.path.join(RENDERS_DIR, "02-Donkey Kong\\01.png"),
                       os.path.join(RENDERS_DIR, "01-Mario\\01.png")]

    # Background
    background = Image.open(background_path, mode="r")
    canvas.paste(background)

    # Character Background
    character_background = Image.open(character_background_path, mode="r")
    canvas.paste(character_background, (0, 0), character_background)

    # TODO: This needs to be a loop or a function
    # Player 1 Character
    character_one = Image.open(character_paths[0], mode="r")
    width_one, height_one = character_one.size
    character_one = character_one.resize((int(width_one * .75), int(height_one * .75)))
    character_one = crop_character(character_one, CHARACTER_BOX)
    canvas.paste(character_one, (0, 140), character_one)

    # Player 2 Character
    character_two = Image.open(character_paths[1], mode="r")
    width_two, height_two = character_two.size
    character_two = character_two.resize((int(width_two * .75), int(height_two * .75)))
    character_two = crop_character(character_two, CHARACTER_BOX)
    canvas.paste(character_two, (960, 140), character_two)

    # Text Background
    text_background = Image.open(text_background_path, mode="r")
    canvas.paste(text_background, (0, 0), text_background)

    # VS
    vs = Image.open(vs_path, mode="r")
    canvas.paste(vs, (0, 0), vs)

    # Text
    draw.text((100, 100), "Test")

    canvas.save(output, format="PNG")
