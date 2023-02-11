from PyQt6.QtWidgets import QPushButton


class CreateButton(QPushButton):
    def __init__(self):
        super().__init__()

        self.setText("Create")
        self.clicked.connect(self.button_handler)

    def button_handler(self):
        print("test")
