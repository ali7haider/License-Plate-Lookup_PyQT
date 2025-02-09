# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 686)
        MainWindow.setStyleSheet("#bg{\n"
"background-color:#FEFDFF;\n"
"    border: 2px solid #F7F7F7;\n"
"\n"
"}\n"
"#mainBar\n"
"{\n"
"background-color:#F7F7F7;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QWidget{\n"
"    color: rgb(40, 44, 52);\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"QPushButton {    \n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-right: 1px solid #DCDCDC;\n"
"    background-color:transparent;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: #DCDCDC;\n"
"    \n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"    border-radius: 5px;\n"
"    border: 1px solid gray;\n"
"    padding-left: 5px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid gray;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid gray;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border-radius: 5px;\n"
"    border: 1px solid gray;\n"
"    padding-left: 10px;\n"
"    background-color: white;\n"
"    selection-background-color: rgb(255, 121, 198);\n"
"    selection-color: white;\n"
"    height: 25px;  /* Adjust height */\n"
"}\n"
"\n"
"/* Hover Effect */\n"
"QComboBox:hover {\n"
"    border: 2px solid gray;\n"
"}")
        self.bg = QtWidgets.QWidget(MainWindow)
        self.bg.setObjectName("bg")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.bg)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_6 = QtWidgets.QFrame(self.bg)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_6.setStyleSheet("background-color:#1159A8;\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setStyleSheet("font: bold 14pt \"Arial\";\n"
"color:white;")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame_6)
        self.topBar = QtWidgets.QFrame(self.bg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topBar.sizePolicy().hasHeightForWidth())
        self.topBar.setSizePolicy(sizePolicy)
        self.topBar.setMinimumSize(QtCore.QSize(0, 40))
        self.topBar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.topBar.setStyleSheet("font: 75 11pt \"Arial\";")
        self.topBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topBar.setObjectName("topBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topBar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLicensePlate = QtWidgets.QPushButton(self.topBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLicensePlate.sizePolicy().hasHeightForWidth())
        self.btnLicensePlate.setSizePolicy(sizePolicy)
        self.btnLicensePlate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLicensePlate.setObjectName("btnLicensePlate")
        self.horizontalLayout.addWidget(self.btnLicensePlate)
        self.btnBlank1 = QtWidgets.QPushButton(self.topBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBlank1.sizePolicy().hasHeightForWidth())
        self.btnBlank1.setSizePolicy(sizePolicy)
        self.btnBlank1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBlank1.setObjectName("btnBlank1")
        self.horizontalLayout.addWidget(self.btnBlank1)
        self.btnBlank3 = QtWidgets.QPushButton(self.topBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBlank3.sizePolicy().hasHeightForWidth())
        self.btnBlank3.setSizePolicy(sizePolicy)
        self.btnBlank3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBlank3.setObjectName("btnBlank3")
        self.horizontalLayout.addWidget(self.btnBlank3)
        self.btnBlank2 = QtWidgets.QPushButton(self.topBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBlank2.sizePolicy().hasHeightForWidth())
        self.btnBlank2.setSizePolicy(sizePolicy)
        self.btnBlank2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBlank2.setObjectName("btnBlank2")
        self.horizontalLayout.addWidget(self.btnBlank2)
        self.verticalLayout.addWidget(self.topBar)
        self.frame = QtWidgets.QFrame(self.bg)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 2))
        self.frame.setStyleSheet("color: red;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.mainBar = QtWidgets.QFrame(self.bg)
        self.mainBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainBar.setObjectName("mainBar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainBar)
        self.verticalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainBar)
        self.stackedWidget.setObjectName("stackedWidget")
        self.licensePlatePage = QtWidgets.QWidget()
        self.licensePlatePage.setObjectName("licensePlatePage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.licensePlatePage)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.licensePlatePage)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setStyleSheet("font: bold 14pt \"Arial\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.licensePlatePage)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 120))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setContentsMargins(10, 0, 10, 0)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.plate_entry = QtWidgets.QLineEdit(self.frame_5)
        self.plate_entry.setMinimumSize(QtCore.QSize(0, 30))
        self.plate_entry.setStyleSheet("")
        self.plate_entry.setObjectName("plate_entry")
        self.gridLayout_3.addWidget(self.plate_entry, 1, 1, 1, 1)
        self.state_dropdown = QtWidgets.QComboBox(self.frame_5)
        self.state_dropdown.setMinimumSize(QtCore.QSize(0, 30))
        self.state_dropdown.setObjectName("state_dropdown")
        self.gridLayout_3.addWidget(self.state_dropdown, 3, 1, 1, 1)
        self.dump_label = QtWidgets.QLabel(self.frame_5)
        self.dump_label.setObjectName("dump_label")
        self.gridLayout_3.addWidget(self.dump_label, 1, 0, 1, 1)
        self.ndk_label = QtWidgets.QLabel(self.frame_5)
        self.ndk_label.setObjectName("ndk_label")
        self.gridLayout_3.addWidget(self.ndk_label, 3, 0, 1, 1)
        self.search_button = QtWidgets.QPushButton(self.frame_5)
        self.search_button.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.search_button.setFont(font)
        self.search_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_button.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#1159A8;\n"
"color:white;\n"
"border-radius:3px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:#146CD0;\n"
"}")
        self.search_button.setObjectName("search_button")
        self.gridLayout_3.addWidget(self.search_button, 4, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_2 = QtWidgets.QFrame(self.licensePlatePage)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 190))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.result_listbox = QtWidgets.QListWidget(self.frame_2)
        self.result_listbox.setStyleSheet("padding:0px;")
        self.result_listbox.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.result_listbox.setObjectName("result_listbox")
        self.verticalLayout_4.addWidget(self.result_listbox)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.licensePlatePage)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.vinTable = QtWidgets.QTableWidget(self.frame_3)
        self.vinTable.setObjectName("vinTable")
        self.vinTable.setColumnCount(0)
        self.vinTable.setRowCount(0)
        self.verticalLayout_5.addWidget(self.vinTable)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.licensePlatePage)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.mainBar)
        MainWindow.setCentralWidget(self.bg)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "License Plate Lookup"))
        self.btnLicensePlate.setText(_translate("MainWindow", "License Plate Lookup"))
        self.btnBlank1.setText(_translate("MainWindow", "Blank Page"))
        self.btnBlank3.setText(_translate("MainWindow", "Blank Page"))
        self.btnBlank2.setText(_translate("MainWindow", "Blank Page"))
        self.label.setText(_translate("MainWindow", "License Plate Lookup"))
        self.dump_label.setText(_translate("MainWindow", "Plate:"))
        self.ndk_label.setText(_translate("MainWindow", "State:"))
        self.search_button.setText(_translate("MainWindow", "Search"))
