from graphics.utils.Types import Character

# When using these, make sure to add ".copy" or anything that uses the object will change
# If, for some reason, we store lists here: make a deepcopy

DEFAULT_SETTINGS = {
    "render_dir": "C:/",
    "output_dir": "C:/",
    "configured": False
}

DEFAULT_CHARACTER: Character = {
    "name": "None",
    "alt": "01",
    "offset": (0, 0),
    "zoom": 100,
}
