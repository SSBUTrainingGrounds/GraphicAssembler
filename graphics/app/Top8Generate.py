import os
from enum import Enum

# Import ImageFont for Fonts
from PIL import Image, ImageDraw, ImageFont

# This is only used for type hinting
from PIL.Image import Image as ImageType

from graphics.utils.CharacterImage import generate_character_image, get_character_path
from graphics.utils.Definitions import FONTS_DIR, TOP8_DIR
from graphics.utils.Text import biggest_font_size
from graphics.utils.Types import Top8Data, Top8Player

SIZE = (1200, 800)
CARD_SIZE = (238, 238)

# Default Locations for Characters based on how many per player
# (x, y)
# M: Centered
# M + S: Main Bottom Right, Secondary Top Left
# M + S + P: Main Bottom Right, Secondary Top Left, Pocket Bottom Left
DEFAULT_CHAR_PLACING = [
    [(0, 0)],
    [(-60, -60), (80, 80)],
    [(-100, -60), (80, 80), (80, -80)]]

DEFAULT_CHAR_SIZING = [
    [1],
    [1, .70],
    [1, .70, .70]
]

PLAYER_CARD_PLACING = [
    (25, 210),
    (288, 210),
    (556, 210),
    (824, 210),
    (148, 473),
    (411, 473),
    (674, 473),
    (937, 473)
]


def generate_player_card(placing: int, tournament: str, player_data: Top8Player) -> ImageType:
    canvas = Image.new("RGBA", CARD_SIZE)
    draw = ImageDraw.Draw(canvas, "RGBA")
    syncopate_number = ImageFont.truetype(os.path.join(FONTS_DIR, "Syncopate-Bold.ttf"), 48)
    syncopate_bold = biggest_font_size(player_data["tag"], os.path.join(FONTS_DIR, "Syncopate-Bold.ttf"), (238, 50), 22)

    character_paths = [
        get_character_path(
            player_data["main"]["name"], player_data["main"]["alt"]
        )
    ]
    if "secondary" in player_data:
        character_paths.append(get_character_path(player_data["secondary"]["name"], player_data["secondary"]["alt"]))
    if "pocket" in player_data:
        character_paths.append(get_character_path(player_data["pocket"]["name"], player_data["pocket"]["alt"]))

    char_number = len(character_paths)
    character_type = None

    for i in range(char_number)[::-1]:
        match i:
            case 0:
                character_type = player_data["main"]
            case 1:
                character_type = player_data["secondary"]
            case 2:
                character_type = player_data["pocket"]
        if character_paths[i]:
            # noinspection PyTypeChecker
            canvas.alpha_composite(
                generate_character_image(
                    character_paths[i],
                    # Add offset to default placing (type checker does not like this ¯\_(ツ)_/¯)
                    # [a, aa] + [b, bb] = [a+b, aa+bb]
                    tuple(map(sum, zip(DEFAULT_CHAR_PLACING[char_number - 1][i], character_type["offset"]))),
                    character_type["zoom"] * DEFAULT_CHAR_SIZING[char_number - 1][i],
                    CARD_SIZE)
            )

    draw.text((15, 15), str(placing), (255, 255, 255), syncopate_number)

    # Annoying, but this is the only way to draw a semi-transparent rectangle
    overlay = Image.new('RGBA', SIZE, (0, 0, 0, 0))
    draw_tag = ImageDraw.Draw(overlay)
    draw_tag.rounded_rectangle((0, 188, 238, 238), fill=(0, 0, 0, int(225 * .96)), radius=10)
    canvas.alpha_composite(overlay)

    draw.rounded_rectangle((0, 0, 238, 238), outline="white", width=3, radius=10)

    tag_text_location = (119, 213)

    if "twitter" in player_data:
        if player_data["twitter"]:
            tag_text_location = (119, 206)
            syncopate_reg = biggest_font_size("@" + player_data["twitter"],
                                              os.path.join(FONTS_DIR, "Syncopate-Regular.ttf"),
                                              (238, 50), 13)
            draw.text((119, 224), "@" + player_data["twitter"].upper(), (255, 255, 255), syncopate_reg, anchor="mm",
                      align="center")

    draw.text(tag_text_location, player_data["tag"].upper(), (255, 255, 255), syncopate_bold, anchor="mm",
              align="center")

    return canvas


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

    for i in range(8):
        player_card = generate_player_card(data["players"][i]["placement"], data["tournament"], data["players"][i])
        canvas.alpha_composite(player_card, PLAYER_CARD_PLACING[i])

    return canvas
