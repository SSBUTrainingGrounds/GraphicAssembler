import json
import os

from graphics.utils.Defaults import DEFAULT_SETTINGS


class SettingsManager:
    def __init__(self, file) -> None:
        if not os.path.exists(file):
            default_settings = json.dumps(DEFAULT_SETTINGS.copy(), indent=4)
            with open(file, "w") as json_file:
                json_file.write(default_settings)

        self.json_file = file
        self.setting_data = self.read_settings()

    def get_setting_value(self, key):
        return self.setting_data[key]

    def update_setting(self, key, value) -> None:
        self.setting_data[key] = value
        self.write_settings()

    def read_settings(self) -> dict[str, str]:
        with open(self.json_file, "r") as json_file:
            settings = json.load(json_file)

        return settings

    def write_settings(self) -> None:
        new_settings = json.dumps(self.setting_data, indent=4)
        with open(self.json_file, "w") as json_file:
            json_file.write(new_settings)


settings_manager = SettingsManager("./config.json")
