import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Messenger(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 1280, 720)
        self.setWindowTitle('Messenger')






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Messenger()
    window.show()
    sys.exit(app.exec_())