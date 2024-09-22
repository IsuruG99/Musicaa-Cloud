from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QHBoxLayout, QPushButton, QLineEdit, QDialog, QWidget, \
    QTableWidget
from PyQt5.QtCore import Qt
from Reader.musicReader import load_music_files, add_tag


def manage_tag(name: str, tags: str) -> None:
    if not name or not tags:
        return
    dialog_box = QDialog()
    dialog_box.setWindowTitle('Add Tag')
    dialog_box.setFixedSize(600, 100)
    dialog_box.setModal(True)

    tag_input = QLineEdit()
    tag_input.setPlaceholderText('Enter a tag')
    tag_input.setFixedSize(400, 50)

    add_button = QPushButton('Add')
    add_button.setFixedSize(100, 50)
    add_button.clicked.connect(lambda: add_tag(name, tag_input.text()))

    layout = QHBoxLayout()
    layout.addWidget(tag_input)
    layout.addWidget(add_button)
    dialog_box.setLayout(layout)

    dialog_box.exec_()

def manage_music_files(table: QTableWidget) -> None:
    try:
        music_data = load_music_files()
    except FileNotFoundError:
        print("No music files found.")
        return

    table.setColumnCount(3)
    table.setHorizontalHeaderLabels(['Music File', 'Tags', ' '])
    table.setRowCount(len(music_data))
    for row, (music_file, tags) in enumerate(music_data.items()):
        music_name = music_file.split('\\')[-1]

        music_file_item = QTableWidgetItem(music_name)
        music_file_item.setFlags(music_file_item.flags() & ~Qt.ItemIsEditable)
        music_file_item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        table.setItem(row, 0, music_file_item)

        tags_item = QTableWidgetItem(', '.join(tags))
        tags_item.setFlags(tags_item.flags() & ~Qt.ItemIsEditable)
        tags_item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        table.setItem(row, 1, tags_item)

        button_widget = QWidget()
        add_button = QPushButton('+')
        add_button.setFixedWidth(30)
        add_button.clicked.connect(lambda _, mf=music_file, ti=tags: manage_tag(mf, ti))

        layout = QHBoxLayout(button_widget)
        layout.addWidget(add_button)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        button_widget.setLayout(layout)
        table.setCellWidget(row, 2, button_widget)

    table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
    table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
    table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
    table.setColumnWidth(0, int(table.width() * 0.4))
    table.setColumnWidth(1, int(table.width() * 0.5))
    table.setColumnWidth(2, int(table.width() * 0.1))