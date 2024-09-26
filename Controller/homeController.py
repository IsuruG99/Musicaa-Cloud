import pygame
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView

import main
from Reader.musicReader import load_music_files
from Reader.playlistReader import update_playlist, read_file


def manage_table(table: QTableWidget, query: str = "All") -> None:
    if table is None:
        return None
    music_data = query_filter(query)
    update_playlist(music_data)

    table.clear()
    table.setColumnCount(2)
    table.setHorizontalHeaderLabels(['Music File', 'Tags'])

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

    if table.rowCount() == 0:
        table.setRowCount(1)
        table.setItem(0, 0, QTableWidgetItem("No music files found."))
        table.setItem(0, 1, QTableWidgetItem(""))

    table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
    table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
    table.setColumnWidth(0, int(table.width() * 0.4))
    table.setColumnWidth(1, int(table.width() * 0.6))

    table.verticalHeader().hide()
    table.horizontalHeader().hide()

def query_filter(query: str = None) -> dict:
    try:
        music_data: dict = load_music_files()
    except FileNotFoundError:
        print("No music files found.")
        return {}

    if query is None or query == "All" or query == "":
        return music_data

    search_terms = query.split()
    filtered_music_data = {}

    for music_file, tags in music_data.items():
        music_name = music_file.split('\\')[-1]
        match = True

        for term in search_terms:
            if term.startswith('#'):
                term = term[1:]  # Remove the '#' for tag search
                if term not in tags:
                    match = False
                    break
            else:
                if term.lower() not in music_name.lower():
                    match = False
                    break

        if match:
            filtered_music_data[music_file] = tags

    return filtered_music_data

#playMusic Function, 1 argument, Play/Pause string
def play_music(action: str) -> None:
    if action not in ["play", "stop", "pause", "next", "prev"]:
        return

    # Get file uri from playlistReader as a list
    playlist: list = read_file()
    if len(playlist) == 0:
        print("No music files found.")
        return

    # Function to play the next song in the playlist
    def play_next(index: int) -> None:
        if index >= len(playlist):
            index = 0  # Loop back to the start of the playlist
        elif index < 0:
            index = len(playlist) - 1 # Loop back to the end of the playlist
        main.current_index = index
        music_file = playlist[index]
        try:
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play()
            print(f"Playing {music_file}")
            pygame.mixer.music.set_endevent(pygame.USEREVENT)
        except pygame.error as e:
            print(f"Could not load music file {music_file}: {e}")
            play_next(index + 1)  # Skip to the next file

    if action == "play":
        if not main.playState:
            play_next(main.current_index)
            main.playState = True
    elif action == "stop":
        if main.playState:
            main.playState = False
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()  # Unload the current music file
            print("Music stopped")
    elif action == "pause":
        if main.playState and pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            print("Music paused")
        else:
            pygame.mixer.music.unpause()
            print("Music resumed")
    elif action == "next":
        if main.playState:
            play_next(main.current_index + 1)
    elif action == "prev":
        if main.playState:
            play_next(main.current_index - 1 if main.current_index > 0 else len(playlist) - 1)
    print(f"Current index: {main.current_index}")




