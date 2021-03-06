# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_Save_Setting_Dialog(QDialog):

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.initSignal()

    def initSignal(self):
        self.Accept_btn.clicked.connect(self.Accept_btn_Click)
        self.Cancel_btn.clicked.connect(self.Cancel_btn_Click)

    def Accept_btn_Click(self):
        self.Accept=True
        self.close()

    def Cancel_btn_Click(self):
        self.Accept=False
        self.close()


    def setupUi(self):
        self.setObjectName("self")
        self.resize(192, 184)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(192)
        sizePolicy.setVerticalStretch(184)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(192, 184))
        self.setMaximumSize(QtCore.QSize(192, 184))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib/resource/setting_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 171, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(81)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(81, 16))
        self.groupBox.setObjectName("groupBox")
        self.Check_News = QtWidgets.QCheckBox(self.groupBox)
        self.Check_News.setGeometry(QtCore.QRect(10, 20, 81, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(81)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.Check_News.sizePolicy().hasHeightForWidth())
        self.Check_News.setSizePolicy(sizePolicy)
        self.Check_News.setMinimumSize(QtCore.QSize(81, 16))
        self.Check_News.setObjectName("Check_News")
        self.Check_Image = QtWidgets.QCheckBox(self.groupBox)
        self.Check_Image.setGeometry(QtCore.QRect(10, 40, 81, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(81)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.Check_Image.sizePolicy().hasHeightForWidth())
        self.Check_Image.setSizePolicy(sizePolicy)
        self.Check_Image.setMinimumSize(QtCore.QSize(81, 16))
        self.Check_Image.setObjectName("Check_Image")
        self.Check_Cafe = QtWidgets.QCheckBox(self.groupBox)
        self.Check_Cafe.setGeometry(QtCore.QRect(10, 60, 81, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(81)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.Check_Cafe.sizePolicy().hasHeightForWidth())
        self.Check_Cafe.setSizePolicy(sizePolicy)
        self.Check_Cafe.setMinimumSize(QtCore.QSize(81, 16))
        self.Check_Cafe.setObjectName("Check_Cafe")
        self.Check_Website = QtWidgets.QCheckBox(self.groupBox)
        self.Check_Website.setGeometry(QtCore.QRect(10, 80, 81, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(81)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.Check_Website.sizePolicy().hasHeightForWidth())
        self.Check_Website.setSizePolicy(sizePolicy)
        self.Check_Website.setMinimumSize(QtCore.QSize(81, 16))
        self.Check_Website.setObjectName("Check_Website")
        self.Check_Company = QtWidgets.QCheckBox(self.groupBox)
        self.Check_Company.setGeometry(QtCore.QRect(10, 100, 81, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(81)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.Check_Company.sizePolicy().hasHeightForWidth())
        self.Check_Company.setSizePolicy(sizePolicy)
        self.Check_Company.setMinimumSize(QtCore.QSize(81, 16))
        self.Check_Company.setObjectName("Check_Company")
        self.Check_Video = QtWidgets.QCheckBox(self.groupBox)
        self.Check_Video.setGeometry(QtCore.QRect(90, 20, 81, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(81)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.Check_Video.sizePolicy().hasHeightForWidth())
        self.Check_Video.setSizePolicy(sizePolicy)
        self.Check_Video.setMinimumSize(QtCore.QSize(81, 16))
        self.Check_Video.setObjectName("Check_Video")
        self.Check_Wiki = QtWidgets.QCheckBox(self.groupBox)
        self.Check_Wiki.setGeometry(QtCore.QRect(90, 40, 81, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(81)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.Check_Wiki.sizePolicy().hasHeightForWidth())
        self.Check_Wiki.setSizePolicy(sizePolicy)
        self.Check_Wiki.setMinimumSize(QtCore.QSize(81, 16))
        self.Check_Wiki.setObjectName("Check_Wiki")
        self.Check_Q = QtWidgets.QCheckBox(self.groupBox)
        self.Check_Q.setGeometry(QtCore.QRect(90, 60, 81, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(81)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.Check_Q.sizePolicy().hasHeightForWidth())
        self.Check_Q.setSizePolicy(sizePolicy)
        self.Check_Q.setMinimumSize(QtCore.QSize(81, 16))
        self.Check_Q.setObjectName("Check_Q")
        self.Check_Post = QtWidgets.QCheckBox(self.groupBox)
        self.Check_Post.setGeometry(QtCore.QRect(90, 80, 81, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(81)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.Check_Post.sizePolicy().hasHeightForWidth())
        self.Check_Post.setSizePolicy(sizePolicy)
        self.Check_Post.setMinimumSize(QtCore.QSize(81, 16))
        self.Check_Post.setObjectName("Check_Post")
        self.Check_PInfo = QtWidgets.QCheckBox(self.groupBox)
        self.Check_PInfo.setGeometry(QtCore.QRect(90, 100, 81, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(81)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.Check_PInfo.sizePolicy().hasHeightForWidth())
        self.Check_PInfo.setSizePolicy(sizePolicy)
        self.Check_PInfo.setMinimumSize(QtCore.QSize(81, 16))
        self.Check_PInfo.setMaximumSize(QtCore.QSize(81, 16))
        self.Check_PInfo.setObjectName("Check_PInfo")
        self.Cancel_btn = QtWidgets.QPushButton(self)
        self.Cancel_btn.setGeometry(QtCore.QRect(108, 150, 75, 23))
        self.Cancel_btn.setObjectName("Cancel_btn")
        self.Accept_btn = QtWidgets.QPushButton(self)
        self.Accept_btn.setGeometry(QtCore.QRect(10, 150, 81, 23))
        self.Accept_btn.setObjectName("Accept_btn")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "저장정보설정"))
        self.groupBox.setTitle(_translate("self", "추출할 정보 선택"))
        self.Check_News.setText(_translate("self", "뉴스"))
        self.Check_Image.setText(_translate("self", "이미지"))
        self.Check_Cafe.setText(_translate("self", "카페"))
        self.Check_Website.setText(_translate("self", "웹사이트"))
        self.Check_Company.setText(_translate("self", "기업정보"))
        self.Check_Video.setText(_translate("self", "동영상"))
        self.Check_Wiki.setText(_translate("self", "지식백과"))
        self.Check_Q.setText(_translate("self", "지식인"))
        self.Check_Post.setText(_translate("self", "포스트"))
        self.Check_PInfo.setText(_translate("self", "인물정보"))
        self.Cancel_btn.setText(_translate("self", "취소"))
        self.Accept_btn.setText(_translate("self", "확인"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = Ui_Save_Setting_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
