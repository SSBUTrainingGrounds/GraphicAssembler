import os
from graphics.definitions import THUMBNAIL_DIR, OUTPUT_DIR

# Import ImageDraw for Text
# Import ImageFont for Fonts
from PIL import Image

def generate_thumbnail(tournament):

    SIZE = (1920, 1080)
    canvas = Image.new('RGBA', SIZE, (0, 0, 0))

    # Paths to Template Items
    background_path = os.path.join(THUMBNAIL_DIR, "Thumbnail-Background.png")
    vs_path = os.path.join(THUMBNAIL_DIR, "Thumbnail-VS-01.png")
    tournament_path = os.path.join(THUMBNAIL_DIR, tournament)
    character_background_path = os.path.join(tournament_path, "Thumbnail-CharacterBackground.png")
    text_background_path = os.path.join(tournament_path, "Thumbnail-TextBackground.png")

    # Background
    background = Image.open(background_path, mode="r")
    canvas.paste(background)

    # Character Background
    character_background = Image.open(character_background_path, mode="r")
    canvas.paste(character_background, (0, 0), character_background)

    # Text Background
    text_background = Image.open(text_background_path, mode="r")
    canvas.paste(text_background, (0, 0), text_background)

    # VS
    vs = Image.open(vs_path, mode="r")
    canvas.paste(vs, (0, 0), vs)

    # Output Path
    output = os.path.join(OUTPUT_DIR, "test1.png")

    canvas.save(output, format="PNG")
