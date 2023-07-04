import sys

from PyQt6.QtWidgets import QApplication
from qt_material import apply_stylesheet  # type: ignore

from graphics.ui.views.SetupWindow import SetupWindow
from graphics.utils.SettingsManager import settings_manager
from graphics.ui.views.MainWindow import MainWindow

app = QApplication(sys.argv)

if settings_manager.get_setting_value("configured"):
    window = MainWindow()
else:
    window = SetupWindow()

window.show()

extra = {}

apply_stylesheet(
    app,
    theme="light_lightgreen.xml",
    extra=extra,
    css_file="./graphics/resources/assets/styles.css",
)

app.exec()
