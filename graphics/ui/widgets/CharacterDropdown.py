from PyQt6.QtWidgets import QComboBox


class CharacterDropdown(QComboBox):
    def __init__(self):
        super().__init__()

        # TODO: Actually list all characters available.
        self.addItems(["01-Mario", "07-Fox", "12-Jigglypuff", "69-Incineroar"])
