from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSplitter, QGridLayout, QListWidget, QPushButton, QLabel, QHBoxLayout, \
    QSlider, QLineEdit, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

from Component.ScrollingLabel import ScrollingLabel


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
        mainLayout.setContentsMargins(10, 10, 10, 10)

        # Top section - Music list with search
        topLayout = QVBoxLayout()
        searchLayout = QHBoxLayout()

        searchBox = QLineEdit()  # Search bar
        searchBtn = QPushButton("Search")  # Search button

        searchLayout.addWidget(searchBox)
        searchLayout.addWidget(searchBtn)

        musicList = QListWidget()  # List of songs

        topLayout.addLayout(searchLayout)
        topLayout.addWidget(musicList)

        # Bottom section - Play controls (Prev, Play/Pause, Next) and bars
        controlLayout = QHBoxLayout()

        prevBtn = QPushButton("⏮")  # Previous button
        playPauseBtn = QPushButton("⏯")  # Play/Pause button (image will change)
        nextBtn = QPushButton("⏭")  # Next button

        controlLayout.addWidget(prevBtn)
        controlLayout.addWidget(playPauseBtn)
        controlLayout.addWidget(nextBtn)

        # Play length bar and volume controls
        barLayout = QHBoxLayout()
        nowPlayingLabel = ScrollingLabel("Now playing: SONG NAME")
        barLayout.addWidget(nowPlayingLabel)

        playLengthBar = QSlider(Qt.Horizontal)
        volumeLabel = QLabel("Vol:")
        volumeSlider = QSlider(Qt.Horizontal)

        barLayout.addSpacerItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        barLayout.addWidget(playLengthBar, stretch=5)
        barLayout.addSpacerItem(QSpacerItem(10, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        barLayout.addWidget(volumeLabel)
        barLayout.addWidget(volumeSlider, stretch=1)

        # Set fixed width for volume controls to ensure they take minimal space
        volumeLabel.setFixedWidth(50)
        volumeSlider.setFixedWidth(100)

        # Adding sections to the main layout
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(controlLayout)
        mainLayout.addLayout(barLayout)

        self.setLayout(mainLayout)

