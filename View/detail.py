from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSplitter, QGridLayout, QTableWidget, QTableWidgetItem, QHeaderView, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

from Controller import detailController, directoryReader
from Controller.musicReader import load_music_files


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
        music_data = load_music_files()

        # Set the number of rows and columns
        table.setRowCount(len(music_data))
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(['Music File', 'Tags'])

        # Populate the table with music files and their tags
        for row, (music_file, tags) in enumerate(music_data.items()):
            music_file_item = QTableWidgetItem(music_file)
            music_file_item.setFlags(music_file_item.flags() & ~Qt.ItemIsEditable)
            music_file_item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            table.setItem(row, 0, music_file_item)

            tags_item = QTableWidgetItem(', '.join(tags))
            tags_item.setFlags(tags_item.flags() & ~Qt.ItemIsEditable)
            tags_item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            table.setItem(row, 1, tags_item)

        # Set column widths to 40% and 60%
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        table.setColumnWidth(0, int(table.width() * 0.4))
        table.setColumnWidth(1, int(table.width() * 0.6))

        # Add the table to the layout
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