import os

# Import ImageFont for Fonts
from PIL import Image, ImageDraw, ImageFont

# This is only used for type hinting
from PIL.Image import Image as ImageType

from graphics.utils.CharacterImage import generate_character_image, get_character_path
from graphics.utils.definitions import FONTS_DIR, OUTPUT_DIR, THUMBNAIL_DIR
from graphics.utils.Text import biggest_font_size
from graphics.utils.types import ThumnbailData

SIZE = (1920, 1080)
CHARACTER_BOX = (960, 800)
POSITION = [(0, 140), (960, 140)]


def draw_thumbnail_text(text: str, into: ImageType, center: tuple[int, int]) -> None:
    # multiple is added because rotating causes image to become jagged
    # sizing it down with the Image.ANTIALIAS flag smooths it out
    multiple = 3

    syncopate = biggest_font_size(
        text,
        os.path.join(FONTS_DIR, "Syncopate-Bold.ttf"),
        (930 * multiple, 120 * multiple),
        130 * multiple,
    )

    width, height = syncopate.getsize(text)
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, (255, 255, 255), syncopate)  # type: ignore
    bbox = draw.textbbox(
        (0, 0),
        text,
        ImageFont.truetype(os.path.join(FONTS_DIR, "Syncopate-Bold.ttf"), 130),
    )

    img = img.rotate(1.6, expand=True)
    width = img.size[0] // multiple
    height = img.size[1] // multiple
    img = img.resize((width, height), resample=Image.ANTIALIAS)

    into.alpha_composite(
        img, (center[0] - (width // 2), center[1] + (bbox[3] - height // 2))
    )


def generate_thumbnail(data: ThumnbailData) -> ImageType:
    player_left = data["players"][0]
    player_right = data["players"][1]
    canvas = Image.new("RGBA", SIZE)

    # TODO: This is allocating every time its run, make constant
    # Paths to Template Items
    background_path = os.path.join(THUMBNAIL_DIR, "Thumbnail-Background.png")
    vs_path = os.path.join(THUMBNAIL_DIR, "Thumbnail-VS-01.png")
    tournament_path = os.path.join(THUMBNAIL_DIR, data["tournament"])
    character_background_path = os.path.join(
        tournament_path, "Thumbnail-CharacterBackground.png"
    )
    text_background_path = os.path.join(tournament_path, "Thumbnail-TextBackground.png")
    character_paths = [
        get_character_path(
            player_left["character"]["name"], player_left["character"]["alt"]
        ),
        get_character_path(
            player_right["character"]["name"], player_right["character"]["alt"]
        ),
    ]

    # Background
    background = Image.open(background_path, mode="r")
    canvas.paste(background)

    # Character Background
    character_background = Image.open(character_background_path, mode="r")
    canvas.alpha_composite(character_background)

    # Player 1 Character
    canvas.alpha_composite(
        generate_character_image(
            character_paths[0],
            player_left["character"]["offset"],
            player_left["character"]["zoom"],
            CHARACTER_BOX,
        ),
        POSITION[0],
    )

    # Player 2 Character
    canvas.alpha_composite(
        generate_character_image(
            character_paths[1],
            player_right["character"]["offset"],
            player_right["character"]["zoom"],
            CHARACTER_BOX,
        ),
        POSITION[1],
    )

    # Text Background
    text_background = Image.open(text_background_path, mode="r")
    canvas.alpha_composite(text_background)

    # VS
    vs = Image.open(vs_path, mode="r")
    canvas.alpha_composite(vs)

    # Text
    draw_thumbnail_text(player_left["tag"], canvas, (480, 45))
    draw_thumbnail_text(player_right["tag"], canvas, (1440, 45))
    draw_thumbnail_text(data["round"], canvas, (480, 835))

    if data["tournament"] == "so":
        draw_thumbnail_text("SMASH OVERSEAS", canvas, (1440, 835))
    else:
        draw_thumbnail_text("TRIALS OF SMASH", canvas, (1440, 835))

    return canvas


def save_image(canvas: ImageType) -> None:
    # Output Path
    output = os.path.join(OUTPUT_DIR, "thumbnail.png")

    canvas.save(output, format="PNG")
