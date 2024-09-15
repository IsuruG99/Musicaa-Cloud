import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

def homepage_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Changing to Home Page")
        func(self, *args, **kwargs)
        self.show()
    return wrapper

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    @homepage_decorator
    def init_ui(self):
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(20, 20, 20, 20)
        gridLayout = QGridLayout()
        mainLayout.addLayout(gridLayout)

        label = QLabel("Hello World!")
        label.setAlignment(Qt.AlignCenter)
        gridLayout.addWidget(label, 0, 0)

        button = QPushButton("Click Me!")
        button.clicked.connect(self.button_clicked)
        gridLayout.addWidget(button, 1, 0)

        self.setLayout(mainLayout)

    def button_clicked(self):
        print("Button Clicked!")

