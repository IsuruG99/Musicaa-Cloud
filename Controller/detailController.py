from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
from Controller.musicReader import load_music_files

def manage_music_files(table):
    music_data = load_music_files()

    table.setColumnCount(2)
    table.setHorizontalHeaderLabels(['Music File', 'Tags'])
    table.setRowCount(len(music_data))
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