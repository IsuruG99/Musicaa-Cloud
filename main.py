import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QTabWidget, QWidget
from PyQt5.QtCore import QFile, QTextStream
from View import home

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_window()

    def init_window(self):
        self.setGeometry(550, 300, 850, 550)
        self.setWindowTitle("GUI")

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
        tab1 = home.HomePage()
        self.addTab(tab1, "Home")

def main():
    app = QApplication(sys.argv)

    # Load the stylesheet
    file = QFile("src/python/dark-style.qss")
    if file.open(QFile.ReadOnly | QFile.Text):
        stream = QTextStream(file)
        app.setStyleSheet(stream.readAll())

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()