import os

from PIL import Image

from graphics.utils.CharacterImage import (
    crop_character,
    get_character_path,
    resize_character,
)

from graphics.utils.SettingsManager import settings_manager


def test_get_character_path():
    renders_dir = settings_manager.get_setting_value("render_dir")

    assert get_character_path("Mario") == os.path.join(renders_dir, "Mario/01.png")
    assert get_character_path("Mario", "02") == os.path.join(
        renders_dir, "Mario/02.png"
    )
    assert get_character_path("Incineroar", "06") == os.path.join(
        renders_dir, "Incineroar/06.png"
    )
    assert get_character_path("Lucas", "22") == os.path.join(
        renders_dir, "Lucas/22.png"
    )

    assert get_character_path("Mii Brawler", "01") == os.path.join(
        renders_dir, "Mii Brawler/01.png"
    )
    assert get_character_path("Mii Brawler", "02") == os.path.join(
        renders_dir, "Mii Brawler/01.png"
    )

    assert get_character_path("None") is None

    assert get_character_path("Random") == os.path.join(
        renders_dir, "Random/Random.png"
    )
    assert get_character_path("Random") == os.path.join(
        renders_dir, "Random/Random.png"
    )


def test_crop_character():
    img = Image.new("RGBA", (100, 100), (255, 0, 0, 255))

    new_img = crop_character(img, (50, 50), (0, 0))
    assert new_img.size == (50, 50)

    new_img = crop_character(img, (50, 50), (10, 10))
    assert new_img.size == (50, 50)

    new_img = crop_character(img, (50, 50), (-10, -10))
    assert new_img.size == (50, 50)

    new_img = crop_character(img, (400, 400), (10, -10))
    assert new_img.size == (400, 400)
    assert new_img.size == (400, 400)


def test_resize_character():
    img = Image.new("RGBA", (100, 100), (255, 0, 0, 255))

    new_img = resize_character(img, 100, 100)
    assert new_img.size == (100, 100)

    new_img = resize_character(img, 50, 100)
    assert new_img.size == (100, 100)

    new_img = resize_character(img, 200, 100)
    assert new_img.size == (100, 100)

    new_img = resize_character(img, 100, 50)
    assert new_img.size == (50, 50)

    new_img = resize_character(img, 100, 200)
    assert new_img.size == (100, 100)
