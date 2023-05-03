from graphics.utils.Types import Character

# When using this, make sure to add ".copy" or anything that uses this object will change
# If, for some reason, we store lists here: make a deepcopy

DEFAULT_CHARACTER: Character = {
    "name": "None",
    "alt": "01",
    "offset": (0, 0),
    "zoom": 100,
}
