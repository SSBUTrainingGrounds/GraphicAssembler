import os
from typing import Optional

from PIL import Image

# This is only used for type hinting
from PIL.Image import Image as ImageType

from graphics.utils.SettingsManager import settings_manager


def get_character_path(character: str, alt: str = "01") -> Optional[str]:
    # We want an option for no character for the Top8 Graphics.
    renders_dir = settings_manager.get_setting_value("render_dir")
    if character.lower() == "none":
        return None

    if character.lower() == "random":
        return os.path.join(renders_dir, "Random/Random.png")

    # The Mii Fighters only have one alt.
    if "mii" in character.lower():
        alt = "01"

    return os.path.join(renders_dir, f"{character}/{alt}.png")


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


def resize_character(image: ImageType, zoom: int, desired_width: int) -> ImageType:
    width_one, height_one = image.size
    if width_one > desired_width:
        factor = desired_width / width_one
        width_one = int(width_one * factor * zoom / 100)
        height_one = int(height_one * factor * zoom / 100)
    return image.resize((width_one, height_one))


def generate_character_image(
        path: str, offset: tuple[int, int], zoom: int, character_box: tuple[int, int]
) -> ImageType:
    character = Image.open(path, mode="r")
    character = character.convert("RGBA")
    character = resize_character(character, zoom, character_box[0])
    character = crop_character(character, character_box, offset)
    return character
