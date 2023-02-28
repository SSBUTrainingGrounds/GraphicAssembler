import os

# Import ImageFont for Fonts
from PIL import Image, ImageDraw, ImageFont

# This is only used for type hinting
from PIL.Image import Image as ImageType

from graphics.app.types import TournamentData
from graphics.definitions import FONTS_DIR, OUTPUT_DIR, RENDERS_DIR, THUMBNAIL_DIR

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


def crop_character(
    image: ImageType, crop: tuple[int, int], offset: tuple[int, int]
) -> ImageType:
    img_width, img_height = image.size

    return image.crop(
        (
            (img_width - crop[0] + offset[0]) // 2,
            (img_height - crop[1] + offset[1]) // 2,
            (img_width + crop[0] + offset[0]) // 2,
            (img_height + crop[1] + offset[1]) // 2,
        )
    )


def resize_character(image: ImageType, zoom: int) -> ImageType:
    width_one, height_one = image.size
    if width_one > 960:
        factor = 960 / width_one
        width_one = int(width_one * factor * zoom / 100)
        height_one = int(height_one * factor * zoom / 100)
    return image.resize((width_one, height_one))


def generate_character_image(
    path: str, offset: tuple[int, int], zoom: int
) -> ImageType:
    character = Image.open(path, mode="r")
    character = character.convert("RGBA")
    character = resize_character(character, zoom)
    character = crop_character(character, CHARACTER_BOX, offset)
    return character


def biggest_font_size(text: str, font_path, box_size, guess) -> ImageFont:
    font = ImageFont.truetype(font_path, guess)
    while (font.getsize(text)[0] > box_size[0]) or (font.getsize(text)[1] > box_size[1]):
        guess -= 1
        font = ImageFont.truetype(font_path, guess)

    return font


def draw_thumbnail_text(text: str, into: ImageType, center: tuple[int, int]) -> None:

    # multiple is added because rotating causes image to become jagged
    # sizing it down with the Image.ANTIALIAS flag smooths it out
    multiple = 3

    syncopate = biggest_font_size(text, os.path.join(FONTS_DIR, 'Syncopate-Bold.ttf'), (930 * multiple, 120 * multiple),
                                  130 * multiple)

    width, height = syncopate.getsize(text)
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, (255, 255, 255), syncopate)
    bbox = draw.textbbox((0, 0), text, ImageFont.truetype(os.path.join(FONTS_DIR, 'Syncopate-Bold.ttf'), 130))

    img = img.rotate(1.6, expand=True)
    width = img.size[0] // multiple
    height = img.size[1] // multiple
    img = img.resize((width, height), resample=Image.ANTIALIAS)

    into.alpha_composite(img, (
        center[0] - (width // 2),
        center[1] + (bbox[3] - height // 2)))


def generate_thumbnail(data: TournamentData) -> ImageType:
    player_left = data["players"][0]
    player_right = data["players"][1]
    canvas = Image.new("RGBA", SIZE)

    # Output Path
    output = os.path.join(OUTPUT_DIR, "test1.png")

    # TODO: This is allocating every time its run, make constant
    # Paths to Template Items
    background_path = os.path.join(THUMBNAIL_DIR, "Thumbnail-Background.png")
    vs_path = os.path.join(THUMBNAIL_DIR, "Thumbnail-VS-01.png")
    tournament_path = os.path.join(THUMBNAIL_DIR, data["tournament"])
    character_background_path = os.path.join(
        tournament_path, "Thumbnail-CharacterBackground.png"
    )
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
    canvas.alpha_composite(
        generate_character_image(
            character_paths[0], player_left["offset"], player_left["zoom"]
        ),
        POSITION[0],
    )

    # Player 2 Character
    canvas.alpha_composite(
        generate_character_image(
            character_paths[1], player_right["offset"], player_right["zoom"]
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
    output = os.path.join(OUTPUT_DIR, "test1.png")

    canvas.save(output, format="PNG")
