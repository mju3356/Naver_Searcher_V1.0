import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from QTdesign.Naver_Search_Form import Ui_MainWindow
from PyQt5.QtWidgets import *


class TestForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_setting()
        self.init_signal()

    def init_setting(self):
        self.input_search.setFocus(True)

    def init_signal(self):
        self.search_btn.clicked.connect(self.Start_Searching)
        #self.input_search.returnPressed(self.Start_Searching)
        self.DelHis_btn.clicked.connect(self.Delete_History)
        self.his_ext.clicked.connect(self.History_Extraction)
        self.exit_btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.search_his.itemClicked.connect(self.SetForcus_Item)
        self.search_his.itemDoubleClicked.connect(self.DoubleClick_Item)

    def Start_Searching(self):
        pass

    def Delete_History(self):
        pass

    def History_Extraction(self):
        pass

    def SetForcus_Item(self):
        pass

    def DoubleClick_Item(self):
        pass

        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
