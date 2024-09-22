from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSplitter, QGridLayout, QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

from Controller import detailController, directoryReader



class DetailPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self) -> None:
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(10, 10, 10, 10)

        splitter = QSplitter(Qt.Vertical)

        # Top section - List and Buttons
        topWidget = QWidget()
        topLayout = QGridLayout()

        table = QTableWidget()
        detailController.manage_music_files(table)
        topLayout.addWidget(table, 0, 0)

        buttonLayout = QHBoxLayout()
        addButton = QPushButton("+")
        buttonLayout.addWidget(addButton)

        removeButton = QPushButton("-")
        buttonLayout.addWidget(removeButton)

        topLayout.addLayout(buttonLayout, 1, 0)  # Buttons next to list
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
        splitter.setStretchFactor(0, 7)
        splitter.setStretchFactor(1, 1)

        mainLayout.addWidget(splitter)
        self.setLayout(mainLayout)