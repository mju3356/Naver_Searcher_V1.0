import sys

from PyQt5.QtWidgets import *

from QTdesign.pyqt_ui_test import Ui_mainWindow


class TestForm(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
