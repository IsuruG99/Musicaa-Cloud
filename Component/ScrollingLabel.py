from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QWidget, QApplication, QSlider, QPushButton, QLineEdit, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt, QTimer

class ScrollingLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedWidth(200)
        self.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.scroll_text)
        self.timer.start(100)  # Adjust the interval as needed
        self.text = text
        self.index = 0

    def scroll_text(self):
        self.index += 1
        if self.index > len(self.text):
            self.index = 0
        display_text = self.text[self.index:] + " " + self.text[:self.index]
        self.setText(display_text)