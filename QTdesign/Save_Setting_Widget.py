# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Save_Setting_Widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_Save_Setting_Widget(QDialog):
    def setupUi(self, Save_Setting_Widget):
        Save_Setting_Widget.setObjectName("Save_Setting_Widget")
        Save_Setting_Widget.resize(201, 151)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../lib/resource/setting_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Save_Setting_Widget.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(Save_Setting_Widget)
        self.groupBox.setGeometry(QtCore.QRect(14, 8, 171, 131))
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

        self.retranslateUi(Save_Setting_Widget)
        QtCore.QMetaObject.connectSlotsByName(Save_Setting_Widget)

    def retranslateUi(self, Save_Setting_Widget):
        _translate = QtCore.QCoreApplication.translate
        Save_Setting_Widget.setWindowTitle(_translate("Save_Setting_Widget", "추출정보설정 "))
        self.groupBox.setTitle(_translate("Save_Setting_Widget", "추출할 정보 선택"))
        self.Check_News.setText(_translate("Save_Setting_Widget", "뉴스"))
        self.Check_Image.setText(_translate("Save_Setting_Widget", "이미지"))
        self.Check_Cafe.setText(_translate("Save_Setting_Widget", "카페"))
        self.Check_Website.setText(_translate("Save_Setting_Widget", "웹사이트"))
        self.Check_Company.setText(_translate("Save_Setting_Widget", "기업정보"))
        self.Check_Video.setText(_translate("Save_Setting_Widget", "동영상"))
        self.Check_Wiki.setText(_translate("Save_Setting_Widget", "지식백과"))
        self.Check_Q.setText(_translate("Save_Setting_Widget", "지식인"))
        self.Check_Post.setText(_translate("Save_Setting_Widget", "포스트"))
        self.Check_PInfo.setText(_translate("Save_Setting_Widget", "인물정보"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Save_Setting=Ui_Save_Setting_Widget()
    Save_Setting.show()
    app.exec_()
