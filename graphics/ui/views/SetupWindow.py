from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QGridLayout, QLineEdit, QLabel, QPushButton, QWidget, QFileDialog

from graphics.ui.views.MainWindow import MainWindow
from graphics.utils.Definitions import ASSET_DIR
from graphics.utils.SettingsManager import settings_manager


class SetupWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("First Time Setup")
        self.resize(800, 600)
        self.setWindowIcon(QIcon(ASSET_DIR + "/icon.png"))

        self.main_window = MainWindow()

        self.grid_layout = QGridLayout()

        self.output_configured = False
        self.render_configured = False

        self.finish_button = QPushButton("Finish")
        self.finish_button.setEnabled(False)
        self.finish_button.clicked.connect(self.finish_setup)

        self.output_box = QLineEdit("Please Set Output Directory")
        self.render_box = QLineEdit("Please Set Render Directory")

        self.output_box.setReadOnly(True)
        self.render_box.setReadOnly(True)

        self.settings_label = QLabel("Setup")

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

        self.grid_layout.addWidget(self.finish_button, 5, 3)

        self.setCentralWidget(QWidget(self))

        self.centralWidget().setLayout(self.grid_layout)

    def set_output_dir(self) -> None:
        settings_manager.update_setting("output_dir",
                                        str(QFileDialog.getExistingDirectory(self, "Select Output Directory")))
        self.output_box.setText(settings_manager.get_setting_value("output_dir"))

        self.output_configured = True

        self.finish_button.setEnabled(self.output_configured and self.render_configured)

    def set_render_dir(self) -> None:
        settings_manager.update_setting("render_dir",
                                        str(QFileDialog.getExistingDirectory(self, "Select Render Directory")))
        self.render_box.setText(settings_manager.get_setting_value("render_dir"))

        self.render_configured = True

        self.finish_button.setEnabled(self.output_configured and self.render_configured)

    def finish_setup(self) -> None:
        settings_manager.update_setting("configured", True)
        self.main_window.show()
        self.close()
