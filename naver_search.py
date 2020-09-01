import datetime
import sys

import requests
from PyQt5 import QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup

from QTdesign.Naver_Search_Form import Ui_MainWindow
from QTdesign.Save_Setting_Dialog import Ui_Save_Setting_Dialog


class TestForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_setting()
        self.init_signal()



    def init_setting(self):
        self.input_search.setFocus(True)
        # 쓰레드 작업으로 시간 계속 업데이트 필요
        self.Show_StatusMsg(str(datetime.datetime.now()))
        self.Url=None

    def init_signal(self):
        self.search_btn.clicked.connect(self.Start_Searching)
        self.input_search.returnPressed.connect(self.Start_Searching)
        self.DelHis_btn.clicked.connect(self.Delete_History)
        self.his_ext.clicked.connect(self.History_Extraction)
        self.exit_btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.search_his.itemClicked.connect(self.SetForcus_Item)
        self.search_his.itemDoubleClicked.connect(self.DoubleClick_Item)

    def Show_StatusMsg(self, msg):
        self.statusbar.showMessage(msg)

    def Start_Searching(self):
        KeyWord = self.input_search.text().strip()
        self.Url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=' + KeyWord
        if KeyWord is None or KeyWord == '' or not KeyWord:
            QMessageBox.about(self, "Error", '검색어를 입력하세요')
            self.input_search.setFocus(True)
            return None
        self.webEngineView.load(QUrl(self.Url))
        self.search_his.addItem(KeyWord)

        for i in soup.select('div._prs_nws_all dt'):
            print(i.text)

    def Delete_History(self):
        self.search_his.clear()

    def History_Extraction(self):
        #Ssd=Save_Setting_Dialog
        Ssd=Ui_Save_Setting_Dialog()
        Ssd.exec_()
        self.Check_Post=Ssd.Check_Post
        self.Check_Q=Ssd.Check_Q
        self.Check_Cafe=Ssd.Check_Cafe
        self.Check_News=Ssd.Check_News
        self.Check_Wiki=Ssd.Check_Wiki
        self.Check_Company=Ssd.Check_Company
        self.Check_Image=Ssd.Check_Image
        self.Check_Pinfo=Ssd.Check_PInfo
        self.Check_Video=Ssd.Check_Video
        self.Check_Website=Ssd.Check_Website
        self.Check_Post=Ssd.Check_Post
        self.Accept=Ssd.Accept

        if not self.Accept:
            return None

        if not self.Url:
            QMessageBox.about(self,"Error",'검색어를 입력하세요')
            return None

        req = requests.get(self.Url)
        WebData = BeautifulSoup(req.content, 'html.parser')











    def SetForcus_Item(self):
        self.input_search.setFocus(True)
        self.input_search.setText(self.search_his.currentItem().text().strip())

    def DoubleClick_Item(self):
        self.input_search.setText(self.search_his.currentItem().text().strip())
        self.Start_Searching()
        item = self.search_his.takeItem(self.search_his.count()-1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()
    app.exec_()
