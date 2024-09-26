import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, \
    QSlider, QLineEdit, QSpacerItem, QSizePolicy, QTableWidget, QCompleter
from PyQt5.QtCore import Qt, QSize

from Component import ScrollingLabel
from Controller import homeController
from Controller.homeController import play_music
import main


def homepage_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Changing to Home Page")
        func(self, *args, **kwargs)
        self.show()
    return wrapper

class HomePage(QWidget):
    _instance = None
    def __init__(self):
        super().__init__()
        HomePage._instance = self
        self.musicList: QTableWidget = None
        self.playPauseBtn: QPushButton = None
        self.searchText: str = None
        self.init_ui()

    @homepage_decorator
    def init_ui(self) -> None:
        image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Res', 'back.png'))
        print(f"Image found at {image_path}")
        if not os.path.exists(image_path):
            print(f"Image not found at {image_path}")
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(10, 10, 10, 10)

        # Top section - Music list with search
        topLayout = QVBoxLayout()

        searchLayout = QHBoxLayout()

        searchBox = QLineEdit()  # Search bar
        searchBtn = QPushButton("Search")
        searchBtn.clicked.connect(lambda: self.set_search_text(searchBox.text()))

        searchLayout.addWidget(searchBox, stretch=4)
        completer = QCompleter(self.getTags())
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        searchBox.setCompleter(completer)
        searchLayout.addWidget(searchBtn, stretch=1)

        self.musicList = QTableWidget()
        self.refresh_page()

        topLayout.addLayout(searchLayout)
        self.musicList.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        topLayout.addWidget(self.musicList)

        # Bottom section - Play controls (Prev, Play/Pause, Next) and bars
        controlLayout = QHBoxLayout()

        prevBtn = QPushButton()  # Previous button
        prevBtn.setIcon(QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Res', 'back.png'))))
        prevBtn.setFixedSize(70,70)
        prevBtn.setIconSize(QSize(50,50))
        prevBtn.clicked.connect(lambda: self.music_controls("prev"))
        stopBtn = QPushButton()  # Stop button\
        stopBtn.setIcon(QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Res', 'stop.png'))))
        stopBtn.setFixedSize(70,70)
        stopBtn.setIconSize(QSize(50,50))
        stopBtn.clicked.connect(lambda: self.music_controls("stop"))
        self.playPauseBtn = QPushButton()  # Play/Pause button (image will change)
        self.playPauseBtn.setIcon(QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Res', 'play.png'))))
        self.playPauseBtn.setFixedSize(70,70)
        self.playPauseBtn.setIconSize(QSize(50,50))
        self.playPauseBtn.clicked.connect(lambda: self.music_controls("play"))
        nextBtn = QPushButton()  # Next button
        nextBtn.setIcon(QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Res', 'next.png'))))
        nextBtn.setFixedSize(70,70)
        nextBtn.setIconSize(QSize(50,50))
        nextBtn.clicked.connect(lambda: lambda: self.music_controls("next"))

        # Add a blank spacer to center the play/pause button
        controlLayout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        controlLayout.addWidget(prevBtn, stretch=1)
        controlLayout.addWidget(stopBtn, stretch=1)
        controlLayout.addWidget(self.playPauseBtn, stretch=1)
        controlLayout.addWidget(nextBtn, stretch=1)
        controlLayout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Play length bar and volume controls
        barLayout = QHBoxLayout()
        nowPlayingLabel = ScrollingLabel.ScrollingLabel("Now playing: SONG NAME")
        barLayout.addWidget(nowPlayingLabel, stretch=3)

        playLengthBar = QSlider(Qt.Horizontal)
        volumeLabel = QLabel("Vol:")
        volumeSlider = QSlider(Qt.Horizontal)

        barLayout.addSpacerItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        barLayout.addWidget(playLengthBar, stretch=4)
        barLayout.addSpacerItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        barLayout.addWidget(volumeLabel, stretch=1)
        barLayout.addWidget(volumeSlider, stretch=2)

        # Adding sections to the main layout
        mainLayout.addLayout(topLayout, stretch=3)
        mainLayout.addLayout(controlLayout, stretch=5)
        mainLayout.addLayout(barLayout, stretch=2)

        self.setLayout(mainLayout)

    # Search text assignment
    def set_search_text(self, text: str) -> None:
        print(self.searchText)
        if text is not None:
            self.searchText = text
        self.refresh_page()

    @classmethod
    def music_controls(cls, action:str):
        if action not in ["play", "stop", "pause", "next", "prev"]:
            return

        if action == "play":
            play_music("play")
        elif action == "stop":
            play_music("stop")
        elif action == "pause":
            play_music("pause")
            cls._instance.playPauseBtn.setIcon(
                QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Res', 'play.png'))))
        elif action == "next":
            play_music("next")
        elif action == "prev":
            play_music("prev")

        if main.playState:
            cls._instance.playPauseBtn.setIcon(
                QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Res', 'pause.png'))))
        else:
            cls._instance.playPauseBtn.setIcon(
                QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__), '../Res', 'play.png'))))
        cls._instance.refresh_page()

    @classmethod
    def refresh_page(cls) -> None:
        if cls._instance and cls._instance.musicList is not None:
            if cls._instance.searchText is None:
                homeController.manage_table(cls._instance.musicList)
            else:
                homeController.manage_table(cls._instance.musicList, cls._instance.searchText)

    def getTags(self) -> list:
        try:
            music_list = homeController.load_music_files()
        except FileNotFoundError:
            print("No music files found.")
            music_list = []

        # Get all tags from music files as a list, no duplicates
        tags = []
        for tags_list in music_list.values():
            #add a hash to the front of each tag. etc #Jpop, #Music.
            tags.extend([f"#{tag}" for tag in tags_list])
        return list(set(tags))
