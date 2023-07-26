import json

from PyQt6 import QtGui
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QGridLayout, QLineEdit, QPushButton, QFileDialog, QWidget, QLabel

from graphics.utils.SettingsManager import settings_manager
from graphics.utils.Definitions import ASSET_DIR


def open_config() -> dict:
    with open("./config.json") as f:
        config = json.load(f)

    return config


class SettingsWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Settings")
        self.resize(800, 600)
        self.setWindowIcon(QIcon(ASSET_DIR + "/icon.png"))

        self.grid_layout = QGridLayout()

        self.output_box = QLineEdit()
        self.render_box = QLineEdit()

        self.output_box.setReadOnly(True)
        self.render_box.setReadOnly(True)

        self.settings_label = QLabel("Settings")

        self.output_label = QLabel("Output Directory")
        self.render_label = QLabel("Render Directory")

        self.set_output_button = QPushButton("Set Output")
        self.set_render_button = QPushButton("Set Render")

        self.set_output_button.clicked.connect(self.set_output_dir)
        self.set_render_button.clicked.connect(self.set_render_dir)

        self.settings_label.setStyleSheet("font-size: 24px")

        self.grid_layout.addWidget(self.settings_label, 0, 0)

        self.grid_layout.addWidget(self.output_label, 1, 0)
        self.grid_layout.addWidget(self.output_box, 2, 0)
        self.grid_layout.addWidget(self.set_output_button, 2, 1)

        self.grid_layout.addWidget(self.render_label, 3, 0)
        self.grid_layout.addWidget(self.render_box, 4, 0)
        self.grid_layout.addWidget(self.set_render_button, 4, 1)

        self.setCentralWidget(QWidget(self))

        self.centralWidget().setLayout(self.grid_layout)

    def set_output_dir(self) -> None:
        settings_manager.update_setting("output_dir",
                                        str(QFileDialog.getExistingDirectory(self, "Select Output Directory", "C:/")))
        self.output_box.setText(settings_manager.get_setting_value("output_dir"))

    def set_render_dir(self) -> None:
        existing_setting = settings_manager.get_setting_value("render_dir")
        settings_manager.update_setting("render_dir",
                                        str(QFileDialog.getExistingDirectory(self, "Select Render Directory",
                                                                             existing_setting)))
        self.render_box.setText(settings_manager.get_setting_value("render_dir"))

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.output_box.setText(settings_manager.get_setting_value("output_dir"))
        self.render_box.setText(settings_manager.get_setting_value("render_dir"))
