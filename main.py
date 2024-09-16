import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QTabWidget, QWidget
from PyQt5.QtCore import QFile, QTextStream
from View import home
from Controller import directoryReader

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_window()

    def init_window(self):
        self.setGeometry(550, 300, 850, 550)
        self.setWindowTitle("Musicaa")

        central_widget = QWidget()
        central_layout = QGridLayout(central_widget)
        self.setCentralWidget(central_widget)

        tabs = TabWidget()
        central_layout.addWidget(tabs)

class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.init_tabs()

    def init_tabs(self):
        self.addTab(home.HomePage(), "Home")

def main():
    app = QApplication(sys.argv)

    # Load the directory reader
    directoryReader.get_file()

    # Load the stylesheet
    file = QFile("dark-style.qss")
    if file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(file)
        app.setStyleSheet(stream.readAll())

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()