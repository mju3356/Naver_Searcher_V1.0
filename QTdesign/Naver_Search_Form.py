# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Naver_Search_Form.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 550))
        MainWindow.setMaximumSize(QtCore.QSize(700, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib/resource/naver_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 411, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("lib/resource/i_1.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(589, 500, 121, 20))
        self.label_2.setObjectName("label_2")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(10, 110, 681, 211))
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(640, 50, 51, 41))
        self.search_btn.setStyleSheet("background-color: rgb(29, 219, 22);")
        self.search_btn.setObjectName("search_btn")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 330, 251, 171))
        self.groupBox.setObjectName("groupBox")
        self.search_his = QtWidgets.QListWidget(self.groupBox)
        self.search_his.setGeometry(QtCore.QRect(10, 20, 231, 141))
        self.search_his.setObjectName("search_his")
        self.DelHis_btn = QtWidgets.QPushButton(self.centralwidget)
        self.DelHis_btn.setGeometry(QtCore.QRect(270, 340, 91, 41))
        self.DelHis_btn.setObjectName("DelHis_btn")
        self.his_ext = QtWidgets.QPushButton(self.centralwidget)
        self.his_ext.setGeometry(QtCore.QRect(270, 400, 91, 41))
        self.his_ext.setObjectName("his_ext")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(270, 460, 91, 41))
        self.exit_btn.setObjectName("exit_btn")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(370, 330, 321, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.log = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.log.setGeometry(QtCore.QRect(10, 20, 301, 141))
        self.log.setObjectName("log")
        self.input_search = QtWidgets.QLineEdit(self.centralwidget)
        self.input_search.setGeometry(QtCore.QRect(412, 50, 211, 41))
        self.input_search.setObjectName("input_search")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "네이버검색기_V1.0"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">TEST Version</span></p></body></html>"))
        self.search_btn.setText(_translate("MainWindow", "검색"))
        self.groupBox.setTitle(_translate("MainWindow", "검색기록"))
        self.DelHis_btn.setText(_translate("MainWindow", "검색기록 \n"
"삭제"))
        self.his_ext.setText(_translate("MainWindow", "현재  \n"
"결과추출"))
        self.exit_btn.setText(_translate("MainWindow", "종료"))
        self.groupBox_2.setTitle(_translate("MainWindow", "log"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())