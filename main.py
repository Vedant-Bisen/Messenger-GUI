import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from TitleBar import Titlebar


class Messenger(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.TitlebarUI()

    # Setting up the Mainwindow UI
    def initUI(self):
        self.setGeometry(200, 200, 1280, 720)  # Setting the size of the window
        self.setWindowTitle("Messenger")  # Setting the title of the window
        self.setMinimumSize(854, 480)  # Setting the minimum size of the window
        self.setMaximumSize(1920, 1080)  # Setting the maximum size of the window
        self.setStyleSheet(
            "background-color: #2c2f33;"
        )  # Setting the background color of the window

    def TitlebarUI(self):
        self.titlebar = Titlebar(self)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Messenger()
    window.show()
    sys.exit(app.exec_())
