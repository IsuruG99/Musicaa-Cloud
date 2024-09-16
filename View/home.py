import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSplitter, QGridLayout, QListWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt
from Controller import homeController, directoryReader

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
    def init_ui(self) -> None:
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(10,10,10,10)

        # Creating a vertical splitter to divide space between the list/buttons and future grid layout
        splitter = QSplitter(Qt.Vertical)

        # Top section - List and Buttons
        topWidget = QWidget()
        topLayout = QGridLayout()

        list = QListWidget()
        list.addItem("List Fetching Failed.")
        #set size to only display like 2 items, rest scroll
        list.setMaximumHeight(100)
        topLayout.addWidget(list, 1, 0)
        homeController.manage_dir_list(list)

        buttonLayout = QVBoxLayout()
        addButton = QPushButton("+")
        addButton.clicked.connect(lambda: homeController.button_clicked(self, "+", list))
        buttonLayout.addWidget(addButton)

        removeButton = QPushButton("-")
        removeButton.clicked.connect(lambda: homeController.button_clicked(self, "-", list))
        buttonLayout.addWidget(removeButton)

        topLayout.addLayout(buttonLayout, 1, 1)  # Buttons next to list
        topWidget.setLayout(topLayout)

        # Bottom section - Placeholder for future use
        bottomWidget = QWidget()
        bottomLayout = QVBoxLayout()

        placeholderLabel = QLabel("GRIDLAYOUT FOR FUTURE USE")
        placeholderLabel.setAlignment(Qt.AlignCenter)
        bottomLayout.addWidget(placeholderLabel)
        bottomWidget.setLayout(bottomLayout)

        # Add widgets to splitter
        splitter.addWidget(topWidget)
        splitter.addWidget(bottomWidget)

        # Set proportions (30% for top section, 70% for bottom)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 7)

        mainLayout.addWidget(splitter)
        self.setLayout(mainLayout)

