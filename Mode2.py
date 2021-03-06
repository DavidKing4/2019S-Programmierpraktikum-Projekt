from Board import *
from Words import *
import copy
import Mode1 as m1
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
from OutFunc import *
from operator import add
from threading import Thread
from PyQt5.QtWidgets import *






class Ui_Formiki(object):
    def setupUi(self, Formiki):
        self.Formiki = Formiki
        Formiki.setObjectName("Formiki")
        Formiki.resize(700, 521)
        Formiki.setStyleSheet("background: #f2f1ef")

        
        
        self.gridLayout_2 = QtWidgets.QGridLayout(Formiki)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(Formiki)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(" color: #303030;\n"
"\n"
"background:#f2f1ef ;\n"
"\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_33 = QtWidgets.QPushButton(Formiki)
        self.pushButton_33.setEnabled(True)
        self.pushButton_33.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_33.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_33.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_33.setAutoFillBackground(False)
        self.pushButton_33.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_33.setAutoDefault(False)
        self.pushButton_33.setDefault(False)
        self.pushButton_33.setFlat(True)
        self.pushButton_33.setObjectName("pushButton_33")
        self.gridLayout.addWidget(self.pushButton_33, 3, 3, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(Formiki)
        self.pushButton_30.setEnabled(True)
        self.pushButton_30.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_30.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_30.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_30.setAutoFillBackground(False)
        self.pushButton_30.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_30.setAutoDefault(False)
        self.pushButton_30.setDefault(False)
        self.pushButton_30.setFlat(True)
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout.addWidget(self.pushButton_30, 3, 0, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(Formiki)
        self.pushButton_31.setEnabled(True)
        self.pushButton_31.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_31.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_31.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_31.setAutoFillBackground(False)
        self.pushButton_31.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_31.setAutoDefault(False)
        self.pushButton_31.setDefault(False)
        self.pushButton_31.setFlat(True)
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout.addWidget(self.pushButton_31, 3, 1, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(Formiki)
        self.pushButton_32.setEnabled(True)
        self.pushButton_32.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_32.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_32.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_32.setAutoFillBackground(False)
        self.pushButton_32.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_32.setAutoDefault(False)
        self.pushButton_32.setDefault(False)
        self.pushButton_32.setFlat(True)
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout.addWidget(self.pushButton_32, 3, 2, 1, 1)
        self.pushButton_01 = QtWidgets.QPushButton(Formiki)
        self.pushButton_01.setEnabled(True)
        self.pushButton_01.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_01.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_01.setFont(font)
        self.pushButton_01.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_01.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_01.setAutoFillBackground(False)
        self.pushButton_01.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_01.setAutoDefault(False)
        self.pushButton_01.setDefault(False)
        self.pushButton_01.setFlat(True)
        self.pushButton_01.setObjectName("pushButton_01")
        self.gridLayout.addWidget(self.pushButton_01, 0, 1, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(Formiki)
        self.pushButton_20.setEnabled(True)
        self.pushButton_20.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_20.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_20.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_20.setAutoFillBackground(False)
        self.pushButton_20.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_20.setAutoDefault(False)
        self.pushButton_20.setDefault(False)
        self.pushButton_20.setFlat(True)
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_20, 2, 0, 1, 1)
        self.pushButton_03 = QtWidgets.QPushButton(Formiki)
        self.pushButton_03.setEnabled(True)
        self.pushButton_03.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_03.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_03.setFont(font)
        self.pushButton_03.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_03.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_03.setAutoFillBackground(False)
        self.pushButton_03.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_03.setAutoDefault(False)
        self.pushButton_03.setDefault(False)
        self.pushButton_03.setFlat(True)
        self.pushButton_03.setObjectName("pushButton_03")
        self.gridLayout.addWidget(self.pushButton_03, 0, 3, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(Formiki)
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_10.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_10.setAutoDefault(False)
        self.pushButton_10.setDefault(False)
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 1, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(Formiki)
        self.pushButton_12.setEnabled(True)
        self.pushButton_12.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_12.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_12.setAutoFillBackground(False)
        self.pushButton_12.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_12.setAutoDefault(False)
        self.pushButton_12.setDefault(False)
        self.pushButton_12.setFlat(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 1, 2, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(Formiki)
        self.pushButton_11.setEnabled(True)
        self.pushButton_11.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_11.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_11.setAutoFillBackground(False)
        self.pushButton_11.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_11.setAutoDefault(False)
        self.pushButton_11.setDefault(False)
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 1, 1, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(Formiki)
        self.pushButton_13.setEnabled(True)
        self.pushButton_13.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_13.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_13.setAutoFillBackground(False)
        self.pushButton_13.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_13.setAutoDefault(False)
        self.pushButton_13.setDefault(False)
        self.pushButton_13.setFlat(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 1, 3, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(Formiki)
        self.pushButton_21.setEnabled(True)
        self.pushButton_21.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_21.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_21.setAutoFillBackground(False)
        self.pushButton_21.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_21.setAutoDefault(False)
        self.pushButton_21.setDefault(False)
        self.pushButton_21.setFlat(True)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout.addWidget(self.pushButton_21, 2, 1, 1, 1)
        self.pushButton_02 = QtWidgets.QPushButton(Formiki)
        self.pushButton_02.setEnabled(True)
        self.pushButton_02.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_02.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_02.setFont(font)
        self.pushButton_02.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_02.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_02.setAutoFillBackground(False)
        self.pushButton_02.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_02.setAutoDefault(False)
        self.pushButton_02.setDefault(False)
        self.pushButton_02.setFlat(True)
        self.pushButton_02.setObjectName("pushButton_02")
        self.gridLayout.addWidget(self.pushButton_02, 0, 2, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(Formiki)
        self.pushButton_22.setEnabled(True)
        self.pushButton_22.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_22.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_22.setAutoFillBackground(False)
        self.pushButton_22.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_22.setAutoDefault(False)
        self.pushButton_22.setDefault(False)
        self.pushButton_22.setFlat(True)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_22, 2, 2, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(Formiki)
        self.pushButton_23.setEnabled(True)
        self.pushButton_23.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_23.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_23.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_23.setAutoFillBackground(False)
        self.pushButton_23.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_23.setAutoDefault(False)
        self.pushButton_23.setDefault(False)
        self.pushButton_23.setFlat(True)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout.addWidget(self.pushButton_23, 2, 3, 1, 1)
        self.pushButton_00 = QtWidgets.QPushButton(Formiki)




        self.pushButton_00.setEnabled(True)
        self.pushButton_00.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_00.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_00.setFont(font)
        self.pushButton_00.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_00.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_00.setAutoFillBackground(False)
        self.pushButton_00.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"\n"
"border: 2px solid  #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_00.setAutoDefault(False)
        self.pushButton_00.setDefault(False)
        self.pushButton_00.setFlat(True)
        self.pushButton_00.setObjectName("pushButton_00")
        self.gridLayout.addWidget(self.pushButton_00, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 2, 1)
        self.AItextEdit_2 = QtWidgets.QTextEdit(Formiki)
        self.AItextEdit_2.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.AItextEdit_2.setFont(font)
        self.AItextEdit_2.setStyleSheet(" color: #303030;\n"
"\n"
"background:#f2f1ef ;\n"
"\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.AItextEdit_2.setLineWidth(-2)
        self.AItextEdit_2.setObjectName("AItextEdit_2")
        self.gridLayout_2.addWidget(self.AItextEdit_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Formiki)
        self.label.setMaximumSize(QtCore.QSize(150, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Formiki)
        self.lcdNumber_2.setMaximumSize(QtCore.QSize(70, 28))
        self.lcdNumber_2.setStyleSheet(" color: #303030;\n"
"\n"
"background:#f2f1ef ;\n"
"\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_2.addWidget(self.lcdNumber_2)
        self.label_2 = QtWidgets.QLabel(Formiki)
        self.label_2.setMaximumSize(QtCore.QSize(150, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(Formiki)
        self.lcdNumber_3.setMaximumSize(QtCore.QSize(70, 28))
        self.lcdNumber_3.setStyleSheet(" color: #303030;\n"
"\n"
"background:#f2f1ef ;\n"
"\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.horizontalLayout_2.addWidget(self.lcdNumber_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(Formiki)
        self.label_3.setMaximumSize(QtCore.QSize(150, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lcdNumber = QtWidgets.QLCDNumber(Formiki)
        self.lcdNumber.setMinimumSize(QtCore.QSize(70, 0))
        self.lcdNumber.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lcdNumber.setStyleSheet(" color: #303030;\n"
"\n"
"background:#f2f1ef ;\n"
"\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_2.addWidget(self.lcdNumber)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(Formiki)
        self.pushButton_3.setMinimumSize(QtCore.QSize(70, 28))
        self.pushButton_3.setMaximumSize(QtCore.QSize(70, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(" color: #303030;\n"
"\n"
"background: #a29bfe;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(Formiki)
        self.pushButton_2.setMinimumSize(QtCore.QSize(70, 28))
        self.pushButton_2.setMaximumSize(QtCore.QSize(70, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(" color: #303030;\n"
"\n"
"background: #fd79a8;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.label_4 = QtWidgets.QLabel(Formiki)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(26)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.pushButton_4 = QtWidgets.QPushButton(Formiki)
        self.pushButton_4.setMinimumSize(QtCore.QSize(70, 28))
        self.pushButton_4.setMaximumSize(QtCore.QSize(70, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(" color: #303030;\n"
"\n"
"background: #00b894 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(Formiki)
        self.pushButton_5.setMinimumSize(QtCore.QSize(70, 28))
        self.pushButton_5.setMaximumSize(QtCore.QSize(70, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(" color: #303030;\n"
"\n"
"background: #fdcb6e ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.hide()
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton = QtWidgets.QPushButton(Formiki)
        self.pushButton.setMinimumSize(QtCore.QSize(70, 28))
        self.pushButton.setMaximumSize(QtCore.QSize(70, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(" color: #303030;\n"
"\n"
"background:#d63031 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)



        """ NEW BUTTONS ||| WILL IT WORK???"""

        ##################################################### 5x5 ######################################################
        self.pushButton_04 = QtWidgets.QPushButton(Formiki)
        self.pushButton_04.setEnabled(True)
        self.pushButton_04.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_04.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_04.setFont(font)
        self.pushButton_04.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_04.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_04.setAutoFillBackground(False)
        self.pushButton_04.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_04.setAutoDefault(False)
        self.pushButton_04.setDefault(False)
        self.pushButton_04.setFlat(True)
        self.pushButton_04.setObjectName("pushButton_04")
        self.pushButton_04.hide()
        self.gridLayout.addWidget(self.pushButton_04, 0, 4, 1, 1)

        self.pushButton_05 = QtWidgets.QPushButton(Formiki)
        self.pushButton_05.setEnabled(True)
        self.pushButton_05.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_05.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_05.setFont(font)
        self.pushButton_05.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_05.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_05.setAutoFillBackground(False)
        self.pushButton_05.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_05.setAutoDefault(False)
        self.pushButton_05.setDefault(False)
        self.pushButton_05.setFlat(True)
        self.pushButton_05.setObjectName("pushButton_05")
        self.pushButton_05.hide()
        self.gridLayout.addWidget(self.pushButton_05, 0, 5, 1, 1)

        self.pushButton_06 = QtWidgets.QPushButton(Formiki)
        self.pushButton_06.setEnabled(True)
        self.pushButton_06.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_06.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_06.setFont(font)
        self.pushButton_06.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_06.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_06.setAutoFillBackground(False)
        self.pushButton_06.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_06.setAutoDefault(False)
        self.pushButton_06.setDefault(False)
        self.pushButton_06.setFlat(True)
        self.pushButton_06.setObjectName("pushButton_06")
        self.pushButton_06.hide()
        self.gridLayout.addWidget(self.pushButton_06, 0, 6, 1, 1)

        self.pushButton_07 = QtWidgets.QPushButton(Formiki)
        self.pushButton_07.setEnabled(True)
        self.pushButton_07.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_07.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_07.setFont(font)
        self.pushButton_07.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_07.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_07.setAutoFillBackground(False)
        self.pushButton_07.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_07.setAutoDefault(False)
        self.pushButton_07.setDefault(False)
        self.pushButton_07.setFlat(True)
        self.pushButton_07.setObjectName("pushButton_07")
        self.pushButton_07.hide()
        self.gridLayout.addWidget(self.pushButton_07, 0, 7, 1, 1)

        self.pushButton_08 = QtWidgets.QPushButton(Formiki)
        self.pushButton_08.setEnabled(True)
        self.pushButton_08.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_08.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_08.setFont(font)
        self.pushButton_08.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_08.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_08.setAutoFillBackground(False)
        self.pushButton_08.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_08.setAutoDefault(False)
        self.pushButton_08.setDefault(False)
        self.pushButton_08.setFlat(True)
        self.pushButton_08.setObjectName("pushButton_08")
        self.pushButton_08.hide()
        self.gridLayout.addWidget(self.pushButton_08, 0, 8, 1, 1)

        self.pushButton_09 = QtWidgets.QPushButton(Formiki)
        self.pushButton_09.setEnabled(True)
        self.pushButton_09.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_09.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_09.setFont(font)
        self.pushButton_09.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_09.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_09.setAutoFillBackground(False)
        self.pushButton_09.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_09.setAutoDefault(False)
        self.pushButton_09.setDefault(False)
        self.pushButton_09.setFlat(True)
        self.pushButton_09.setObjectName("pushButton_09")
        self.pushButton_09.hide()
        self.gridLayout.addWidget(self.pushButton_09, 0, 9, 1, 1)

        self.pushButton_010 = QtWidgets.QPushButton(Formiki)
        self.pushButton_010.setEnabled(True)
        self.pushButton_010.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_010.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_010.setFont(font)
        self.pushButton_010.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_010.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_010.setAutoFillBackground(False)
        self.pushButton_010.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_010.setAutoDefault(False)
        self.pushButton_010.setDefault(False)
        self.pushButton_010.setFlat(True)
        self.pushButton_010.setObjectName("pushButton_010")
        self.pushButton_010.hide()
        self.gridLayout.addWidget(self.pushButton_010, 0, 10, 1, 1)

        self.pushButton_011 = QtWidgets.QPushButton(Formiki)
        self.pushButton_011.setEnabled(True)
        self.pushButton_011.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_011.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_011.setFont(font)
        self.pushButton_011.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_011.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_011.setAutoFillBackground(False)
        self.pushButton_011.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_011.setAutoDefault(False)
        self.pushButton_011.setDefault(False)
        self.pushButton_011.setFlat(True)
        self.pushButton_011.setObjectName("pushButton_011")
        self.pushButton_011.hide()
        self.gridLayout.addWidget(self.pushButton_011, 0, 11, 1, 1)
















        self.pushButton_14 = QtWidgets.QPushButton(Formiki)
        self.pushButton_14.setEnabled(True)
        self.pushButton_14.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_14.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_14.setAutoFillBackground(False)
        self.pushButton_14.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_14.setAutoDefault(False)
        self.pushButton_14.setDefault(False)
        self.pushButton_14.setFlat(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.hide()
        self.gridLayout.addWidget(self.pushButton_14, 1, 4, 1, 1)

        self.pushButton_15 = QtWidgets.QPushButton(Formiki)
        self.pushButton_15.setEnabled(True)
        self.pushButton_15.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_15.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_15.setAutoFillBackground(False)
        self.pushButton_15.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_15.setAutoDefault(False)
        self.pushButton_15.setDefault(False)
        self.pushButton_15.setFlat(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.hide()
        self.gridLayout.addWidget(self.pushButton_15, 1, 5, 1, 1)

        self.pushButton_16 = QtWidgets.QPushButton(Formiki)
        self.pushButton_16.setEnabled(True)
        self.pushButton_16.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_16.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_16.setAutoFillBackground(False)
        self.pushButton_16.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_16.setAutoDefault(False)
        self.pushButton_16.setDefault(False)
        self.pushButton_16.setFlat(True)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.hide()
        self.gridLayout.addWidget(self.pushButton_16, 1, 6, 1, 1)

        self.pushButton_17 = QtWidgets.QPushButton(Formiki)
        self.pushButton_17.setEnabled(True)
        self.pushButton_17.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_17.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_17.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_17.setAutoFillBackground(False)
        self.pushButton_17.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_17.setAutoDefault(False)
        self.pushButton_17.setDefault(False)
        self.pushButton_17.setFlat(True)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.hide()
        self.gridLayout.addWidget(self.pushButton_17, 1, 7, 1, 1)

        self.pushButton_18 = QtWidgets.QPushButton(Formiki)
        self.pushButton_18.setEnabled(True)
        self.pushButton_18.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_18.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_18.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_18.setAutoFillBackground(False)
        self.pushButton_18.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_18.setAutoDefault(False)
        self.pushButton_18.setDefault(False)
        self.pushButton_18.setFlat(True)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.hide()
        self.gridLayout.addWidget(self.pushButton_18, 1, 8, 1, 1)

        self.pushButton_19 = QtWidgets.QPushButton(Formiki)
        self.pushButton_19.setEnabled(True)
        self.pushButton_19.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_19.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_19.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_19.setAutoFillBackground(False)
        self.pushButton_19.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_19.setAutoDefault(False)
        self.pushButton_19.setDefault(False)
        self.pushButton_19.setFlat(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.hide()
        self.gridLayout.addWidget(self.pushButton_19, 1, 9, 1, 1)

        self.pushButton_110 = QtWidgets.QPushButton(Formiki)
        self.pushButton_110.setEnabled(True)
        self.pushButton_110.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_110.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_110.setFont(font)
        self.pushButton_110.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_110.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_110.setAutoFillBackground(False)
        self.pushButton_110.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_110.setAutoDefault(False)
        self.pushButton_110.setDefault(False)
        self.pushButton_110.setFlat(True)
        self.pushButton_110.setObjectName("pushButton_110")
        self.pushButton_110.hide()
        self.gridLayout.addWidget(self.pushButton_110, 1, 10, 1, 1)

        self.pushButton_111 = QtWidgets.QPushButton(Formiki)
        self.pushButton_111.setEnabled(True)
        self.pushButton_111.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_111.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_111.setFont(font)
        self.pushButton_111.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_111.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_111.setAutoFillBackground(False)
        self.pushButton_111.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_111.setAutoDefault(False)
        self.pushButton_111.setDefault(False)
        self.pushButton_111.setFlat(True)
        self.pushButton_111.setObjectName("pushButton_111")
        self.pushButton_111.hide()
        self.gridLayout.addWidget(self.pushButton_111, 1, 11, 1, 1)

        self.pushButton_24 = QtWidgets.QPushButton(Formiki)
        self.pushButton_24.setEnabled(True)
        self.pushButton_24.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_24.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_24.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_24.setAutoFillBackground(False)
        self.pushButton_24.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_24.setAutoDefault(False)
        self.pushButton_24.setDefault(False)
        self.pushButton_24.setFlat(True)
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_24.hide()
        self.gridLayout.addWidget(self.pushButton_24, 2, 4, 1, 1)

        self.pushButton_25 = QtWidgets.QPushButton(Formiki)
        self.pushButton_25.setEnabled(True)
        self.pushButton_25.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_25.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_25.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_25.setAutoFillBackground(False)
        self.pushButton_25.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_25.setAutoDefault(False)
        self.pushButton_25.setDefault(False)
        self.pushButton_25.setFlat(True)
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_25.hide()
        self.gridLayout.addWidget(self.pushButton_25, 2, 5, 1, 1)

        self.pushButton_26 = QtWidgets.QPushButton(Formiki)
        self.pushButton_26.setEnabled(True)
        self.pushButton_26.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_26.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_26.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_26.setAutoFillBackground(False)
        self.pushButton_26.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_26.setAutoDefault(False)
        self.pushButton_26.setDefault(False)
        self.pushButton_26.setFlat(True)
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_26.hide()
        self.gridLayout.addWidget(self.pushButton_26, 2, 6, 1, 1)

        self.pushButton_27 = QtWidgets.QPushButton(Formiki)
        self.pushButton_27.setEnabled(True)
        self.pushButton_27.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_27.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_27.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_27.setAutoFillBackground(False)
        self.pushButton_27.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_27.setAutoDefault(False)
        self.pushButton_27.setDefault(False)
        self.pushButton_27.setFlat(True)
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_27.hide()
        self.gridLayout.addWidget(self.pushButton_27, 2, 7, 1, 1)

        self.pushButton_28 = QtWidgets.QPushButton(Formiki)
        self.pushButton_28.setEnabled(True)
        self.pushButton_28.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_28.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_28.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_28.setAutoFillBackground(False)
        self.pushButton_28.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_28.setAutoDefault(False)
        self.pushButton_28.setDefault(False)
        self.pushButton_28.setFlat(True)
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_28.hide()
        self.gridLayout.addWidget(self.pushButton_28, 2, 8, 1, 1)

        self.pushButton_29 = QtWidgets.QPushButton(Formiki)
        self.pushButton_29.setEnabled(True)
        self.pushButton_29.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_29.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_29.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_29.setAutoFillBackground(False)
        self.pushButton_29.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_29.setAutoDefault(False)
        self.pushButton_29.setDefault(False)
        self.pushButton_29.setFlat(True)
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_29.hide()
        self.gridLayout.addWidget(self.pushButton_29, 2, 9, 1, 1)

        self.pushButton_210 = QtWidgets.QPushButton(Formiki)
        self.pushButton_210.setEnabled(True)
        self.pushButton_210.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_210.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_210.setFont(font)
        self.pushButton_210.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_210.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_210.setAutoFillBackground(False)
        self.pushButton_210.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_210.setAutoDefault(False)
        self.pushButton_210.setDefault(False)
        self.pushButton_210.setFlat(True)
        self.pushButton_210.setObjectName("pushButton_210")
        self.pushButton_210.hide()
        self.gridLayout.addWidget(self.pushButton_210, 2, 10, 1, 1)

        self.pushButton_211 = QtWidgets.QPushButton(Formiki)
        self.pushButton_211.setEnabled(True)
        self.pushButton_211.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_211.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_211.setFont(font)
        self.pushButton_211.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_211.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_211.setAutoFillBackground(False)
        self.pushButton_211.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_211.setAutoDefault(False)
        self.pushButton_211.setDefault(False)
        self.pushButton_211.setFlat(True)
        self.pushButton_211.setObjectName("pushButton_211")
        self.pushButton_211.hide()
        self.gridLayout.addWidget(self.pushButton_211, 2, 11, 1, 1)

        self.pushButton_34 = QtWidgets.QPushButton(Formiki)
        self.pushButton_34.setEnabled(True)
        self.pushButton_34.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_34.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_34.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_34.setAutoFillBackground(False)
        self.pushButton_34.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_34.setAutoDefault(False)
        self.pushButton_34.setDefault(False)
        self.pushButton_34.setFlat(True)
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_34.hide()
        self.gridLayout.addWidget(self.pushButton_34, 3, 4, 1, 1)

        self.pushButton_35 = QtWidgets.QPushButton(Formiki)
        self.pushButton_35.setEnabled(True)
        self.pushButton_35.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_35.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_35.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_35.setAutoFillBackground(False)
        self.pushButton_35.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_35.setAutoDefault(False)
        self.pushButton_35.setDefault(False)
        self.pushButton_35.setFlat(True)
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_35.hide()
        self.gridLayout.addWidget(self.pushButton_35, 3, 5, 1, 1)

        self.pushButton_36 = QtWidgets.QPushButton(Formiki)
        self.pushButton_36.setEnabled(True)
        self.pushButton_36.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_36.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_36.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_36.setAutoFillBackground(False)
        self.pushButton_36.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_36.setAutoDefault(False)
        self.pushButton_36.setDefault(False)
        self.pushButton_36.setFlat(True)
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_36.hide()
        self.gridLayout.addWidget(self.pushButton_36, 3, 6, 1, 1)

        self.pushButton_37 = QtWidgets.QPushButton(Formiki)
        self.pushButton_37.setEnabled(True)
        self.pushButton_37.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_37.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_37.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_37.setAutoFillBackground(False)
        self.pushButton_37.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_37.setAutoDefault(False)
        self.pushButton_37.setDefault(False)
        self.pushButton_37.setFlat(True)
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_37.hide()
        self.gridLayout.addWidget(self.pushButton_37, 3, 7, 1, 1)

        self.pushButton_38 = QtWidgets.QPushButton(Formiki)
        self.pushButton_38.setEnabled(True)
        self.pushButton_38.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_38.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_38.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_38.setAutoFillBackground(False)
        self.pushButton_38.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_38.setAutoDefault(False)
        self.pushButton_38.setDefault(False)
        self.pushButton_38.setFlat(True)
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_38.hide()
        self.gridLayout.addWidget(self.pushButton_38, 3, 8, 1, 1)

        self.pushButton_39 = QtWidgets.QPushButton(Formiki)
        self.pushButton_39.setEnabled(True)
        self.pushButton_39.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_39.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_39.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_39.setAutoFillBackground(False)
        self.pushButton_39.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_39.setAutoDefault(False)
        self.pushButton_39.setDefault(False)
        self.pushButton_39.setFlat(True)
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_39.hide()
        self.gridLayout.addWidget(self.pushButton_39, 3, 9, 1, 1)

        self.pushButton_310 = QtWidgets.QPushButton(Formiki)
        self.pushButton_310.setEnabled(True)
        self.pushButton_310.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_310.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_310.setFont(font)
        self.pushButton_310.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_310.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_310.setAutoFillBackground(False)
        self.pushButton_310.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_310.setAutoDefault(False)
        self.pushButton_310.setDefault(False)
        self.pushButton_310.setFlat(True)
        self.pushButton_310.setObjectName("pushButton_310")
        self.pushButton_310.hide()
        self.gridLayout.addWidget(self.pushButton_310, 3, 10, 1, 1)

        self.pushButton_311 = QtWidgets.QPushButton(Formiki)
        self.pushButton_311.setEnabled(True)
        self.pushButton_311.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_311.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_311.setFont(font)
        self.pushButton_311.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_311.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_311.setAutoFillBackground(False)
        self.pushButton_311.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_311.setAutoDefault(False)
        self.pushButton_311.setDefault(False)
        self.pushButton_311.setFlat(True)
        self.pushButton_311.setObjectName("pushButton_311")
        self.pushButton_311.hide()
        self.gridLayout.addWidget(self.pushButton_311, 3, 11, 1, 1)

        self.pushButton_40 = QtWidgets.QPushButton(Formiki)
        self.pushButton_40.setEnabled(True)
        self.pushButton_40.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_40.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_40.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_40.setAutoFillBackground(False)
        self.pushButton_40.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_40.setAutoDefault(False)
        self.pushButton_40.setDefault(False)
        self.pushButton_40.setFlat(True)
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_40.hide()
        self.gridLayout.addWidget(self.pushButton_40, 4, 0, 1, 1)

        self.pushButton_41 = QtWidgets.QPushButton(Formiki)
        self.pushButton_41.setEnabled(True)
        self.pushButton_41.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_41.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_41.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_41.setAutoFillBackground(False)
        self.pushButton_41.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_41.setAutoDefault(False)
        self.pushButton_41.setDefault(False)
        self.pushButton_41.setFlat(True)
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_41.hide()
        self.gridLayout.addWidget(self.pushButton_41, 4, 1, 1, 1)

        self.pushButton_42 = QtWidgets.QPushButton(Formiki)
        self.pushButton_42.setEnabled(True)
        self.pushButton_42.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_42.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_42.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_42.setAutoFillBackground(False)
        self.pushButton_42.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_42.setAutoDefault(False)
        self.pushButton_42.setDefault(False)
        self.pushButton_42.setFlat(True)
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_42.hide()
        self.gridLayout.addWidget(self.pushButton_42, 4, 2, 1, 1)

        self.pushButton_43 = QtWidgets.QPushButton(Formiki)
        self.pushButton_43.setEnabled(True)
        self.pushButton_43.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_43.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_43.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_43.setAutoFillBackground(False)
        self.pushButton_43.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_43.setAutoDefault(False)
        self.pushButton_43.setDefault(False)
        self.pushButton_43.setFlat(True)
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_43.hide()
        self.gridLayout.addWidget(self.pushButton_43, 4, 3, 1, 1)

        self.pushButton_44 = QtWidgets.QPushButton(Formiki)
        self.pushButton_44.setEnabled(True)
        self.pushButton_44.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_44.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_44.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_44.setAutoFillBackground(False)
        self.pushButton_44.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_44.setAutoDefault(False)
        self.pushButton_44.setDefault(False)
        self.pushButton_44.setFlat(True)
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_44.hide()
        self.gridLayout.addWidget(self.pushButton_44, 4, 4, 1, 1)

        self.pushButton_45 = QtWidgets.QPushButton(Formiki)
        self.pushButton_45.setEnabled(True)
        self.pushButton_45.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_45.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_45.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_45.setAutoFillBackground(False)
        self.pushButton_45.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_45.setAutoDefault(False)
        self.pushButton_45.setDefault(False)
        self.pushButton_45.setFlat(True)
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_45.hide()
        self.gridLayout.addWidget(self.pushButton_45, 4, 5, 1, 1)

        self.pushButton_46 = QtWidgets.QPushButton(Formiki)
        self.pushButton_46.setEnabled(True)
        self.pushButton_46.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_46.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_46.setFont(font)
        self.pushButton_46.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_46.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_46.setAutoFillBackground(False)
        self.pushButton_46.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_46.setAutoDefault(False)
        self.pushButton_46.setDefault(False)
        self.pushButton_46.setFlat(True)
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_46.hide()
        self.gridLayout.addWidget(self.pushButton_46, 4, 6, 1, 1)

        self.pushButton_47 = QtWidgets.QPushButton(Formiki)
        self.pushButton_47.setEnabled(True)
        self.pushButton_47.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_47.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_47.setFont(font)
        self.pushButton_47.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_47.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_47.setAutoFillBackground(False)
        self.pushButton_47.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_47.setAutoDefault(False)
        self.pushButton_47.setDefault(False)
        self.pushButton_47.setFlat(True)
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_47.hide()
        self.gridLayout.addWidget(self.pushButton_47, 4, 7, 1, 1)

        self.pushButton_48 = QtWidgets.QPushButton(Formiki)
        self.pushButton_48.setEnabled(True)
        self.pushButton_48.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_48.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_48.setFont(font)
        self.pushButton_48.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_48.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_48.setAutoFillBackground(False)
        self.pushButton_48.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_48.setAutoDefault(False)
        self.pushButton_48.setDefault(False)
        self.pushButton_48.setFlat(True)
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_48.hide()
        self.gridLayout.addWidget(self.pushButton_48, 4, 8, 1, 1)

        self.pushButton_49 = QtWidgets.QPushButton(Formiki)
        self.pushButton_49.setEnabled(True)
        self.pushButton_49.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_49.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_49.setFont(font)
        self.pushButton_49.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_49.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_49.setAutoFillBackground(False)
        self.pushButton_49.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_49.setAutoDefault(False)
        self.pushButton_49.setDefault(False)
        self.pushButton_49.setFlat(True)
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_49.hide()
        self.gridLayout.addWidget(self.pushButton_49, 4, 9, 1, 1)

        self.pushButton_410 = QtWidgets.QPushButton(Formiki)
        self.pushButton_410.setEnabled(True)
        self.pushButton_410.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_410.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_410.setFont(font)
        self.pushButton_410.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_410.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_410.setAutoFillBackground(False)
        self.pushButton_410.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_410.setAutoDefault(False)
        self.pushButton_410.setDefault(False)
        self.pushButton_410.setFlat(True)
        self.pushButton_410.setObjectName("pushButton_410")
        self.pushButton_410.hide()
        self.gridLayout.addWidget(self.pushButton_410, 4, 10, 1, 1)

        self.pushButton_411 = QtWidgets.QPushButton(Formiki)
        self.pushButton_411.setEnabled(True)
        self.pushButton_411.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_411.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_411.setFont(font)
        self.pushButton_411.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_411.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_411.setAutoFillBackground(False)
        self.pushButton_411.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_411.setAutoDefault(False)
        self.pushButton_411.setDefault(False)
        self.pushButton_411.setFlat(True)
        self.pushButton_411.setObjectName("pushButton_411")
        self.pushButton_411.hide()
        self.gridLayout.addWidget(self.pushButton_411, 4, 11, 1, 1)


        self.pushButton_50 = QtWidgets.QPushButton(Formiki)
        self.pushButton_50.setEnabled(True)
        self.pushButton_50.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_50.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_50.setFont(font)
        self.pushButton_50.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_50.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_50.setAutoFillBackground(False)
        self.pushButton_50.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87561 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_50.setAutoDefault(False)
        self.pushButton_50.setDefault(False)
        self.pushButton_50.setFlat(True)
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_50.hide()
        self.gridLayout.addWidget(self.pushButton_50, 5, 0, 1, 1)

        self.pushButton_51 = QtWidgets.QPushButton(Formiki)
        self.pushButton_51.setEnabled(True)
        self.pushButton_51.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_51.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_51.setFont(font)
        self.pushButton_51.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_51.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_51.setAutoFillBackground(False)
        self.pushButton_51.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87561 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_51.setAutoDefault(False)
        self.pushButton_51.setDefault(False)
        self.pushButton_51.setFlat(True)
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_51.hide()
        self.gridLayout.addWidget(self.pushButton_51, 5, 1, 1, 1)

        self.pushButton_52 = QtWidgets.QPushButton(Formiki)
        self.pushButton_52.setEnabled(True)
        self.pushButton_52.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_52.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_52.setFont(font)
        self.pushButton_52.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_52.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_52.setAutoFillBackground(False)
        self.pushButton_52.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87561 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_52.setAutoDefault(False)
        self.pushButton_52.setDefault(False)
        self.pushButton_52.setFlat(True)
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_52.hide()
        self.gridLayout.addWidget(self.pushButton_52, 5, 2, 1, 1)

        self.pushButton_53 = QtWidgets.QPushButton(Formiki)
        self.pushButton_53.setEnabled(True)
        self.pushButton_53.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_53.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_53.setFont(font)
        self.pushButton_53.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_53.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_53.setAutoFillBackground(False)
        self.pushButton_53.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87561 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_53.setAutoDefault(False)
        self.pushButton_53.setDefault(False)
        self.pushButton_53.setFlat(True)
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_53.hide()
        self.gridLayout.addWidget(self.pushButton_53, 5, 3, 1, 1)

        self.pushButton_54 = QtWidgets.QPushButton(Formiki)
        self.pushButton_54.setEnabled(True)
        self.pushButton_54.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_54.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_54.setFont(font)
        self.pushButton_54.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_54.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_54.setAutoFillBackground(False)
        self.pushButton_54.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87561 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_54.setAutoDefault(False)
        self.pushButton_54.setDefault(False)
        self.pushButton_54.setFlat(True)
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_54.hide()
        self.gridLayout.addWidget(self.pushButton_54, 5, 4, 1, 1)

        self.pushButton_55 = QtWidgets.QPushButton(Formiki)
        self.pushButton_55.setEnabled(True)
        self.pushButton_55.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_55.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_55.setFont(font)
        self.pushButton_55.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_55.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_55.setAutoFillBackground(False)
        self.pushButton_55.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87561 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_55.setAutoDefault(False)
        self.pushButton_55.setDefault(False)
        self.pushButton_55.setFlat(True)
        self.pushButton_55.setObjectName("pushButton_55")
        self.pushButton_55.hide()
        self.gridLayout.addWidget(self.pushButton_55, 5, 5, 1, 1)

        self.pushButton_56 = QtWidgets.QPushButton(Formiki)
        self.pushButton_56.setEnabled(True)
        self.pushButton_56.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_56.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_56.setFont(font)
        self.pushButton_56.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_56.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_56.setAutoFillBackground(False)
        self.pushButton_56.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87561 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_56.setAutoDefault(False)
        self.pushButton_56.setDefault(False)
        self.pushButton_56.setFlat(True)
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_56.hide()
        self.gridLayout.addWidget(self.pushButton_56, 5, 6, 1, 1)

        self.pushButton_57 = QtWidgets.QPushButton(Formiki)
        self.pushButton_57.setEnabled(True)
        self.pushButton_57.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_57.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_57.setFont(font)
        self.pushButton_57.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_57.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_57.setAutoFillBackground(False)
        self.pushButton_57.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87561 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_57.setAutoDefault(False)
        self.pushButton_57.setDefault(False)
        self.pushButton_57.setFlat(True)
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_57.hide()
        self.gridLayout.addWidget(self.pushButton_57, 5, 7, 1, 1)

        self.pushButton_58 = QtWidgets.QPushButton(Formiki)
        self.pushButton_58.setEnabled(True)
        self.pushButton_58.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_58.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_58.setFont(font)
        self.pushButton_58.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_58.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_58.setAutoFillBackground(False)
        self.pushButton_58.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87561 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_58.setAutoDefault(False)
        self.pushButton_58.setDefault(False)
        self.pushButton_58.setFlat(True)
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_58.hide()
        self.gridLayout.addWidget(self.pushButton_58, 5, 8, 1, 1)

        self.pushButton_59 = QtWidgets.QPushButton(Formiki)
        self.pushButton_59.setEnabled(True)
        self.pushButton_59.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_59.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_59.setFont(font)
        self.pushButton_59.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_59.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_59.setAutoFillBackground(False)
        self.pushButton_59.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87561 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_59.setAutoDefault(False)
        self.pushButton_59.setDefault(False)
        self.pushButton_59.setFlat(True)
        self.pushButton_59.setObjectName("pushButton_59")
        self.pushButton_59.hide()
        self.gridLayout.addWidget(self.pushButton_59, 5, 9, 1, 1)

        self.pushButton_510 = QtWidgets.QPushButton(Formiki)
        self.pushButton_510.setEnabled(True)
        self.pushButton_510.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_510.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_510.setFont(font)
        self.pushButton_510.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_510.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_510.setAutoFillBackground(False)
        self.pushButton_510.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87561 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_510.setAutoDefault(False)
        self.pushButton_510.setDefault(False)
        self.pushButton_510.setFlat(True)
        self.pushButton_510.setObjectName("pushButton_510")
        self.pushButton_510.hide()
        self.gridLayout.addWidget(self.pushButton_510, 5, 10, 1, 1)

        self.pushButton_511 = QtWidgets.QPushButton(Formiki)
        self.pushButton_511.setEnabled(True)
        self.pushButton_511.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_511.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_511.setFont(font)
        self.pushButton_511.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_511.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_511.setAutoFillBackground(False)
        self.pushButton_511.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87561 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_511.setAutoDefault(False)
        self.pushButton_511.setDefault(False)
        self.pushButton_511.setFlat(True)
        self.pushButton_511.setObjectName("pushButton_511")
        self.pushButton_511.hide()
        self.gridLayout.addWidget(self.pushButton_511, 5, 11, 1, 1)

        self.pushButton_60 = QtWidgets.QPushButton(Formiki)
        self.pushButton_60.setEnabled(True)
        self.pushButton_60.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_60.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_60.setFont(font)
        self.pushButton_60.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_60.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_60.setAutoFillBackground(False)
        self.pushButton_60.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_60.setAutoDefault(False)
        self.pushButton_60.setDefault(False)
        self.pushButton_60.setFlat(True)
        self.pushButton_60.setObjectName("pushButton_60")
        self.pushButton_60.hide()
        self.gridLayout.addWidget(self.pushButton_60, 6, 0, 1, 1)

        self.pushButton_61 = QtWidgets.QPushButton(Formiki)
        self.pushButton_61.setEnabled(True)
        self.pushButton_61.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_61.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_61.setFont(font)
        self.pushButton_61.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_61.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_61.setAutoFillBackground(False)
        self.pushButton_61.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_61.setAutoDefault(False)
        self.pushButton_61.setDefault(False)
        self.pushButton_61.setFlat(True)
        self.pushButton_61.setObjectName("pushButton_61")
        self.pushButton_61.hide()
        self.gridLayout.addWidget(self.pushButton_61, 6, 1, 1, 1)

        self.pushButton_62 = QtWidgets.QPushButton(Formiki)
        self.pushButton_62.setEnabled(True)
        self.pushButton_62.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_62.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_62.setFont(font)
        self.pushButton_62.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_62.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_62.setAutoFillBackground(False)
        self.pushButton_62.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_62.setAutoDefault(False)
        self.pushButton_62.setDefault(False)
        self.pushButton_62.setFlat(True)
        self.pushButton_62.setObjectName("pushButton_62")
        self.pushButton_62.hide()
        self.gridLayout.addWidget(self.pushButton_62, 6, 2, 1, 1)

        self.pushButton_63 = QtWidgets.QPushButton(Formiki)
        self.pushButton_63.setEnabled(True)
        self.pushButton_63.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_63.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_63.setFont(font)
        self.pushButton_63.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_63.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_63.setAutoFillBackground(False)
        self.pushButton_63.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_63.setAutoDefault(False)
        self.pushButton_63.setDefault(False)
        self.pushButton_63.setFlat(True)
        self.pushButton_63.setObjectName("pushButton_63")
        self.pushButton_63.hide()
        self.gridLayout.addWidget(self.pushButton_63, 6, 3, 1, 1)

        self.pushButton_64 = QtWidgets.QPushButton(Formiki)
        self.pushButton_64.setEnabled(True)
        self.pushButton_64.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_64.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_64.setFont(font)
        self.pushButton_64.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_64.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_64.setAutoFillBackground(False)
        self.pushButton_64.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_64.setAutoDefault(False)
        self.pushButton_64.setDefault(False)
        self.pushButton_64.setFlat(True)
        self.pushButton_64.setObjectName("pushButton_64")
        self.pushButton_64.hide()
        self.gridLayout.addWidget(self.pushButton_64, 6, 4, 1, 1)

        self.pushButton_65 = QtWidgets.QPushButton(Formiki)
        self.pushButton_65.setEnabled(True)
        self.pushButton_65.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_65.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_65.setFont(font)
        self.pushButton_65.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_65.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_65.setAutoFillBackground(False)
        self.pushButton_65.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_65.setAutoDefault(False)
        self.pushButton_65.setDefault(False)
        self.pushButton_65.setFlat(True)
        self.pushButton_65.setObjectName("pushButton_65")
        self.pushButton_65.hide()
        self.gridLayout.addWidget(self.pushButton_65, 6, 5, 1, 1)

        self.pushButton_66 = QtWidgets.QPushButton(Formiki)
        self.pushButton_66.setEnabled(True)
        self.pushButton_66.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_66.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_66.setFont(font)
        self.pushButton_66.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_66.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_66.setAutoFillBackground(False)
        self.pushButton_66.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_66.setAutoDefault(False)
        self.pushButton_66.setDefault(False)
        self.pushButton_66.setFlat(True)
        self.pushButton_66.setObjectName("pushButton_66")
        self.pushButton_66.hide()
        self.gridLayout.addWidget(self.pushButton_66, 6, 6, 1, 1)

        self.pushButton_67 = QtWidgets.QPushButton(Formiki)
        self.pushButton_67.setEnabled(True)
        self.pushButton_67.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_67.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_67.setFont(font)
        self.pushButton_67.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_67.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_67.setAutoFillBackground(False)
        self.pushButton_67.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_67.setAutoDefault(False)
        self.pushButton_67.setDefault(False)
        self.pushButton_67.setFlat(True)
        self.pushButton_67.setObjectName("pushButton_67")
        self.pushButton_67.hide()
        self.gridLayout.addWidget(self.pushButton_67, 6, 7, 1, 1)

        self.pushButton_68 = QtWidgets.QPushButton(Formiki)
        self.pushButton_68.setEnabled(True)
        self.pushButton_68.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_68.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_68.setFont(font)
        self.pushButton_68.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_68.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_68.setAutoFillBackground(False)
        self.pushButton_68.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_68.setAutoDefault(False)
        self.pushButton_68.setDefault(False)
        self.pushButton_68.setFlat(True)
        self.pushButton_68.setObjectName("pushButton_68")
        self.pushButton_68.hide()
        self.gridLayout.addWidget(self.pushButton_68, 6, 8, 1, 1)

        self.pushButton_69 = QtWidgets.QPushButton(Formiki)
        self.pushButton_69.setEnabled(True)
        self.pushButton_69.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_69.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_69.setFont(font)
        self.pushButton_69.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_69.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_69.setAutoFillBackground(False)
        self.pushButton_69.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_69.setAutoDefault(False)
        self.pushButton_69.setDefault(False)
        self.pushButton_69.setFlat(True)
        self.pushButton_69.setObjectName("pushButton_69")
        self.pushButton_69.hide()
        self.gridLayout.addWidget(self.pushButton_69, 6, 9, 1, 1)

        self.pushButton_610 = QtWidgets.QPushButton(Formiki)
        self.pushButton_610.setEnabled(True)
        self.pushButton_610.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_610.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_610.setFont(font)
        self.pushButton_610.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_610.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_610.setAutoFillBackground(False)
        self.pushButton_610.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_610.setAutoDefault(False)
        self.pushButton_610.setDefault(False)
        self.pushButton_610.setFlat(True)
        self.pushButton_610.setObjectName("pushButton_610")
        self.pushButton_610.hide()
        self.gridLayout.addWidget(self.pushButton_610, 6, 10, 1, 1)

        self.pushButton_611 = QtWidgets.QPushButton(Formiki)
        self.pushButton_611.setEnabled(True)
        self.pushButton_611.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_611.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_611.setFont(font)
        self.pushButton_611.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_611.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_611.setAutoFillBackground(False)
        self.pushButton_611.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_611.setAutoDefault(False)
        self.pushButton_611.setDefault(False)
        self.pushButton_611.setFlat(True)
        self.pushButton_611.setObjectName("pushButton_611")
        self.pushButton_611.hide()
        self.gridLayout.addWidget(self.pushButton_611, 6, 11, 1, 1)

        self.pushButton_70 = QtWidgets.QPushButton(Formiki)
        self.pushButton_70.setEnabled(True)
        self.pushButton_70.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_70.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_70.setFont(font)
        self.pushButton_70.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_70.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_70.setAutoFillBackground(False)
        self.pushButton_70.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_70.setAutoDefault(False)
        self.pushButton_70.setDefault(False)
        self.pushButton_70.setFlat(True)
        self.pushButton_70.setObjectName("pushButton_70")
        self.pushButton_70.hide()
        self.gridLayout.addWidget(self.pushButton_70, 7, 0, 1, 1)

        self.pushButton_71 = QtWidgets.QPushButton(Formiki)
        self.pushButton_71.setEnabled(True)
        self.pushButton_71.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_71.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_71.setFont(font)
        self.pushButton_71.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_71.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_71.setAutoFillBackground(False)
        self.pushButton_71.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_71.setAutoDefault(False)
        self.pushButton_71.setDefault(False)
        self.pushButton_71.setFlat(True)
        self.pushButton_71.setObjectName("pushButton_71")
        self.pushButton_71.hide()
        self.gridLayout.addWidget(self.pushButton_71, 7, 1, 1, 1)

        self.pushButton_72 = QtWidgets.QPushButton(Formiki)
        self.pushButton_72.setEnabled(True)
        self.pushButton_72.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_72.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_72.setFont(font)
        self.pushButton_72.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_72.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_72.setAutoFillBackground(False)
        self.pushButton_72.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_72.setAutoDefault(False)
        self.pushButton_72.setDefault(False)
        self.pushButton_72.setFlat(True)
        self.pushButton_72.setObjectName("pushButton_72")
        self.pushButton_72.hide()
        self.gridLayout.addWidget(self.pushButton_72, 7, 2, 1, 1)

        self.pushButton_73 = QtWidgets.QPushButton(Formiki)
        self.pushButton_73.setEnabled(True)
        self.pushButton_73.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_73.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_73.setFont(font)
        self.pushButton_73.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_73.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_73.setAutoFillBackground(False)
        self.pushButton_73.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_73.setAutoDefault(False)
        self.pushButton_73.setDefault(False)
        self.pushButton_73.setFlat(True)
        self.pushButton_73.setObjectName("pushButton_73")
        self.pushButton_73.hide()
        self.gridLayout.addWidget(self.pushButton_73, 7, 3, 1, 1)

        self.pushButton_74 = QtWidgets.QPushButton(Formiki)
        self.pushButton_74.setEnabled(True)
        self.pushButton_74.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_74.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_74.setFont(font)
        self.pushButton_74.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_74.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_74.setAutoFillBackground(False)
        self.pushButton_74.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_74.setAutoDefault(False)
        self.pushButton_74.setDefault(False)
        self.pushButton_74.setFlat(True)
        self.pushButton_74.setObjectName("pushButton_74")
        self.pushButton_74.hide()
        self.gridLayout.addWidget(self.pushButton_74, 7, 4, 1, 1)

        self.pushButton_75 = QtWidgets.QPushButton(Formiki)
        self.pushButton_75.setEnabled(True)
        self.pushButton_75.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_75.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_75.setFont(font)
        self.pushButton_75.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_75.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_75.setAutoFillBackground(False)
        self.pushButton_75.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_75.setAutoDefault(False)
        self.pushButton_75.setDefault(False)
        self.pushButton_75.setFlat(True)
        self.pushButton_75.setObjectName("pushButton_75")
        self.pushButton_75.hide()
        self.gridLayout.addWidget(self.pushButton_75, 7, 5, 1, 1)

        self.pushButton_76 = QtWidgets.QPushButton(Formiki)
        self.pushButton_76.setEnabled(True)
        self.pushButton_76.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_76.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_76.setFont(font)
        self.pushButton_76.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_76.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_76.setAutoFillBackground(False)
        self.pushButton_76.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_76.setAutoDefault(False)
        self.pushButton_76.setDefault(False)
        self.pushButton_76.setFlat(True)
        self.pushButton_76.setObjectName("pushButton_76")
        self.pushButton_76.hide()
        self.gridLayout.addWidget(self.pushButton_76, 7, 6, 1, 1)

        self.pushButton_77 = QtWidgets.QPushButton(Formiki)
        self.pushButton_77.setEnabled(True)
        self.pushButton_77.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_77.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_77.setFont(font)
        self.pushButton_77.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_77.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_77.setAutoFillBackground(False)
        self.pushButton_77.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_77.setAutoDefault(False)
        self.pushButton_77.setDefault(False)
        self.pushButton_77.setFlat(True)
        self.pushButton_77.setObjectName("pushButton_77")
        self.pushButton_77.hide()
        self.gridLayout.addWidget(self.pushButton_77, 7, 7, 1, 1)

        self.pushButton_78 = QtWidgets.QPushButton(Formiki)
        self.pushButton_78.setEnabled(True)
        self.pushButton_78.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_78.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_78.setFont(font)
        self.pushButton_78.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_78.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_78.setAutoFillBackground(False)
        self.pushButton_78.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_78.setAutoDefault(False)
        self.pushButton_78.setDefault(False)
        self.pushButton_78.setFlat(True)
        self.pushButton_78.setObjectName("pushButton_78")
        self.pushButton_78.hide()
        self.gridLayout.addWidget(self.pushButton_78, 7, 8, 1, 1)

        self.pushButton_79 = QtWidgets.QPushButton(Formiki)
        self.pushButton_79.setEnabled(True)
        self.pushButton_79.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_79.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_79.setFont(font)
        self.pushButton_79.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_79.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_79.setAutoFillBackground(False)
        self.pushButton_79.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_79.setAutoDefault(False)
        self.pushButton_79.setDefault(False)
        self.pushButton_79.setFlat(True)
        self.pushButton_79.setObjectName("pushButton_79")
        self.pushButton_79.hide()
        self.gridLayout.addWidget(self.pushButton_79, 7, 9, 1, 1)

        self.pushButton_710 = QtWidgets.QPushButton(Formiki)
        self.pushButton_710.setEnabled(True)
        self.pushButton_710.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_710.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_710.setFont(font)
        self.pushButton_710.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_710.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_710.setAutoFillBackground(False)
        self.pushButton_710.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_710.setAutoDefault(False)
        self.pushButton_710.setDefault(False)
        self.pushButton_710.setFlat(True)
        self.pushButton_710.setObjectName("pushButton_710")
        self.pushButton_710.hide()
        self.gridLayout.addWidget(self.pushButton_710, 7, 10, 1, 1)

        self.pushButton_711 = QtWidgets.QPushButton(Formiki)
        self.pushButton_711.setEnabled(True)
        self.pushButton_711.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_711.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_711.setFont(font)
        self.pushButton_711.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_711.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_711.setAutoFillBackground(False)
        self.pushButton_711.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_711.setAutoDefault(False)
        self.pushButton_711.setDefault(False)
        self.pushButton_711.setFlat(True)
        self.pushButton_711.setObjectName("pushButton_711")
        self.pushButton_711.hide()
        self.gridLayout.addWidget(self.pushButton_711, 7, 11, 1, 1)

        self.pushButton_80 = QtWidgets.QPushButton(Formiki)
        self.pushButton_80.setEnabled(True)
        self.pushButton_80.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_80.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_80.setFont(font)
        self.pushButton_80.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_80.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_80.setAutoFillBackground(False)
        self.pushButton_80.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_80.setAutoDefault(False)
        self.pushButton_80.setDefault(False)
        self.pushButton_80.setFlat(True)
        self.pushButton_80.setObjectName("pushButton_80")
        self.pushButton_80.hide()
        self.gridLayout.addWidget(self.pushButton_80, 8, 0, 1, 1)

        self.pushButton_81 = QtWidgets.QPushButton(Formiki)
        self.pushButton_81.setEnabled(True)
        self.pushButton_81.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_81.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_81.setFont(font)
        self.pushButton_81.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_81.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_81.setAutoFillBackground(False)
        self.pushButton_81.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_81.setAutoDefault(False)
        self.pushButton_81.setDefault(False)
        self.pushButton_81.setFlat(True)
        self.pushButton_81.setObjectName("pushButton_81")
        self.pushButton_81.hide()
        self.gridLayout.addWidget(self.pushButton_81, 8, 1, 1, 1)

        self.pushButton_82 = QtWidgets.QPushButton(Formiki)
        self.pushButton_82.setEnabled(True)
        self.pushButton_82.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_82.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_82.setFont(font)
        self.pushButton_82.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_82.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_82.setAutoFillBackground(False)
        self.pushButton_82.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_82.setAutoDefault(False)
        self.pushButton_82.setDefault(False)
        self.pushButton_82.setFlat(True)
        self.pushButton_82.setObjectName("pushButton_82")
        self.pushButton_82.hide()
        self.gridLayout.addWidget(self.pushButton_82, 8, 2, 1, 1)

        self.pushButton_83 = QtWidgets.QPushButton(Formiki)
        self.pushButton_83.setEnabled(True)
        self.pushButton_83.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_83.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_83.setFont(font)
        self.pushButton_83.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_83.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_83.setAutoFillBackground(False)
        self.pushButton_83.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_83.setAutoDefault(False)
        self.pushButton_83.setDefault(False)
        self.pushButton_83.setFlat(True)
        self.pushButton_83.setObjectName("pushButton_83")
        self.pushButton_83.hide()
        self.gridLayout.addWidget(self.pushButton_83, 8, 3, 1, 1)

        self.pushButton_84 = QtWidgets.QPushButton(Formiki)
        self.pushButton_84.setEnabled(True)
        self.pushButton_84.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_84.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_84.setFont(font)
        self.pushButton_84.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_84.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_84.setAutoFillBackground(False)
        self.pushButton_84.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_84.setAutoDefault(False)
        self.pushButton_84.setDefault(False)
        self.pushButton_84.setFlat(True)
        self.pushButton_84.setObjectName("pushButton_84")
        self.pushButton_84.hide()
        self.gridLayout.addWidget(self.pushButton_84, 8, 4, 1, 1)

        self.pushButton_85 = QtWidgets.QPushButton(Formiki)
        self.pushButton_85.setEnabled(True)
        self.pushButton_85.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_85.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_85.setFont(font)
        self.pushButton_85.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_85.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_85.setAutoFillBackground(False)
        self.pushButton_85.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_85.setAutoDefault(False)
        self.pushButton_85.setDefault(False)
        self.pushButton_85.setFlat(True)
        self.pushButton_85.setObjectName("pushButton_85")
        self.pushButton_85.hide()
        self.gridLayout.addWidget(self.pushButton_85, 8, 5, 1, 1)

        self.pushButton_86 = QtWidgets.QPushButton(Formiki)
        self.pushButton_86.setEnabled(True)
        self.pushButton_86.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_86.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_86.setFont(font)
        self.pushButton_86.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_86.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_86.setAutoFillBackground(False)
        self.pushButton_86.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_86.setAutoDefault(False)
        self.pushButton_86.setDefault(False)
        self.pushButton_86.setFlat(True)
        self.pushButton_86.setObjectName("pushButton_86")
        self.pushButton_86.hide()
        self.gridLayout.addWidget(self.pushButton_86, 8, 6, 1, 1)

        self.pushButton_87 = QtWidgets.QPushButton(Formiki)
        self.pushButton_87.setEnabled(True)
        self.pushButton_87.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_87.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_87.setFont(font)
        self.pushButton_87.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_87.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_87.setAutoFillBackground(False)
        self.pushButton_87.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_87.setAutoDefault(False)
        self.pushButton_87.setDefault(False)
        self.pushButton_87.setFlat(True)
        self.pushButton_87.setObjectName("pushButton_87")
        self.pushButton_87.hide()
        self.gridLayout.addWidget(self.pushButton_87, 8, 7, 1, 1)

        self.pushButton_88 = QtWidgets.QPushButton(Formiki)
        self.pushButton_88.setEnabled(True)
        self.pushButton_88.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_88.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_88.setFont(font)
        self.pushButton_88.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_88.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_88.setAutoFillBackground(False)
        self.pushButton_88.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_88.setAutoDefault(False)
        self.pushButton_88.setDefault(False)
        self.pushButton_88.setFlat(True)
        self.pushButton_88.setObjectName("pushButton_88")
        self.pushButton_88.hide()
        self.gridLayout.addWidget(self.pushButton_88, 8, 8, 1, 1)

        self.pushButton_89 = QtWidgets.QPushButton(Formiki)
        self.pushButton_89.setEnabled(True)
        self.pushButton_89.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_89.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_89.setFont(font)
        self.pushButton_89.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_89.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_89.setAutoFillBackground(False)
        self.pushButton_89.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_89.setAutoDefault(False)
        self.pushButton_89.setDefault(False)
        self.pushButton_89.setFlat(True)
        self.pushButton_89.setObjectName("pushButton_89")
        self.pushButton_89.hide()
        self.gridLayout.addWidget(self.pushButton_89, 8, 9, 1, 1)

        self.pushButton_810 = QtWidgets.QPushButton(Formiki)
        self.pushButton_810.setEnabled(True)
        self.pushButton_810.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_810.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_810.setFont(font)
        self.pushButton_810.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_810.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_810.setAutoFillBackground(False)
        self.pushButton_810.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_810.setAutoDefault(False)
        self.pushButton_810.setDefault(False)
        self.pushButton_810.setFlat(True)
        self.pushButton_810.setObjectName("pushButton_810")
        self.pushButton_810.hide()
        self.gridLayout.addWidget(self.pushButton_810, 8, 10, 1, 1)

        self.pushButton_811 = QtWidgets.QPushButton(Formiki)
        self.pushButton_811.setEnabled(True)
        self.pushButton_811.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_811.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_811.setFont(font)
        self.pushButton_811.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_811.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_811.setAutoFillBackground(False)
        self.pushButton_811.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_811.setAutoDefault(False)
        self.pushButton_811.setDefault(False)
        self.pushButton_811.setFlat(True)
        self.pushButton_811.setObjectName("pushButton_811")
        self.pushButton_811.hide()
        self.gridLayout.addWidget(self.pushButton_811, 8, 11, 1, 1)

        self.pushButton_90 = QtWidgets.QPushButton(Formiki)
        self.pushButton_90.setEnabled(True)
        self.pushButton_90.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_90.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_90.setFont(font)
        self.pushButton_90.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_90.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_90.setAutoFillBackground(False)
        self.pushButton_90.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_90.setAutoDefault(False)
        self.pushButton_90.setDefault(False)
        self.pushButton_90.setFlat(True)
        self.pushButton_90.setObjectName("pushButton_90")
        self.pushButton_90.hide()
        self.gridLayout.addWidget(self.pushButton_90, 9, 0, 1, 1)

        self.pushButton_91 = QtWidgets.QPushButton(Formiki)
        self.pushButton_91.setEnabled(True)
        self.pushButton_91.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_91.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_91.setFont(font)
        self.pushButton_91.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_91.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_91.setAutoFillBackground(False)
        self.pushButton_91.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_91.setAutoDefault(False)
        self.pushButton_91.setDefault(False)
        self.pushButton_91.setFlat(True)
        self.pushButton_91.setObjectName("pushButton_91")
        self.pushButton_91.hide()
        self.gridLayout.addWidget(self.pushButton_91, 9, 1, 1, 1)

        self.pushButton_92 = QtWidgets.QPushButton(Formiki)
        self.pushButton_92.setEnabled(True)
        self.pushButton_92.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_92.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_92.setFont(font)
        self.pushButton_92.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_92.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_92.setAutoFillBackground(False)
        self.pushButton_92.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_92.setAutoDefault(False)
        self.pushButton_92.setDefault(False)
        self.pushButton_92.setFlat(True)
        self.pushButton_92.setObjectName("pushButton_92")
        self.pushButton_92.hide()
        self.gridLayout.addWidget(self.pushButton_92, 9, 2, 1, 1)

        self.pushButton_93 = QtWidgets.QPushButton(Formiki)
        self.pushButton_93.setEnabled(True)
        self.pushButton_93.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_93.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_93.setFont(font)
        self.pushButton_93.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_93.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_93.setAutoFillBackground(False)
        self.pushButton_93.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_93.setAutoDefault(False)
        self.pushButton_93.setDefault(False)
        self.pushButton_93.setFlat(True)
        self.pushButton_93.setObjectName("pushButton_93")
        self.pushButton_93.hide()
        self.gridLayout.addWidget(self.pushButton_93, 9, 3, 1, 1)

        self.pushButton_94 = QtWidgets.QPushButton(Formiki)
        self.pushButton_94.setEnabled(True)
        self.pushButton_94.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_94.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_94.setFont(font)
        self.pushButton_94.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_94.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_94.setAutoFillBackground(False)
        self.pushButton_94.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_94.setAutoDefault(False)
        self.pushButton_94.setDefault(False)
        self.pushButton_94.setFlat(True)
        self.pushButton_94.setObjectName("pushButton_94")
        self.pushButton_94.hide()
        self.gridLayout.addWidget(self.pushButton_94, 9, 4, 1, 1)

        self.pushButton_95 = QtWidgets.QPushButton(Formiki)
        self.pushButton_95.setEnabled(True)
        self.pushButton_95.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_95.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_95.setFont(font)
        self.pushButton_95.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_95.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_95.setAutoFillBackground(False)
        self.pushButton_95.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_95.setAutoDefault(False)
        self.pushButton_95.setDefault(False)
        self.pushButton_95.setFlat(True)
        self.pushButton_95.setObjectName("pushButton_95")
        self.pushButton_95.hide()
        self.gridLayout.addWidget(self.pushButton_95, 9, 5, 1, 1)

        self.pushButton_96 = QtWidgets.QPushButton(Formiki)
        self.pushButton_96.setEnabled(True)
        self.pushButton_96.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_96.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_96.setFont(font)
        self.pushButton_96.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_96.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_96.setAutoFillBackground(False)
        self.pushButton_96.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_96.setAutoDefault(False)
        self.pushButton_96.setDefault(False)
        self.pushButton_96.setFlat(True)
        self.pushButton_96.setObjectName("pushButton_96")
        self.pushButton_96.hide()
        self.gridLayout.addWidget(self.pushButton_96, 9, 6, 1, 1)

        self.pushButton_97 = QtWidgets.QPushButton(Formiki)
        self.pushButton_97.setEnabled(True)
        self.pushButton_97.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_97.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_97.setFont(font)
        self.pushButton_97.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_97.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_97.setAutoFillBackground(False)
        self.pushButton_97.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_97.setAutoDefault(False)
        self.pushButton_97.setDefault(False)
        self.pushButton_97.setFlat(True)
        self.pushButton_97.setObjectName("pushButton_97")
        self.pushButton_97.hide()
        self.gridLayout.addWidget(self.pushButton_97, 9, 7, 1, 1)

        self.pushButton_98 = QtWidgets.QPushButton(Formiki)
        self.pushButton_98.setEnabled(True)
        self.pushButton_98.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_98.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_98.setFont(font)
        self.pushButton_98.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_98.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_98.setAutoFillBackground(False)
        self.pushButton_98.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_98.setAutoDefault(False)
        self.pushButton_98.setDefault(False)
        self.pushButton_98.setFlat(True)
        self.pushButton_98.setObjectName("pushButton_98")
        self.pushButton_98.hide()
        self.gridLayout.addWidget(self.pushButton_98, 9, 8, 1, 1)

        self.pushButton_99 = QtWidgets.QPushButton(Formiki)
        self.pushButton_99.setEnabled(True)
        self.pushButton_99.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_99.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_99.setFont(font)
        self.pushButton_99.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_99.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_99.setAutoFillBackground(False)
        self.pushButton_99.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_99.setAutoDefault(False)
        self.pushButton_99.setDefault(False)
        self.pushButton_99.setFlat(True)
        self.pushButton_99.setObjectName("pushButton_99")
        self.pushButton_99.hide()
        self.gridLayout.addWidget(self.pushButton_99, 9, 9, 1, 1)

        self.pushButton_910 = QtWidgets.QPushButton(Formiki)
        self.pushButton_910.setEnabled(True)
        self.pushButton_910.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_910.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_910.setFont(font)
        self.pushButton_910.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_910.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_910.setAutoFillBackground(False)
        self.pushButton_910.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_910.setAutoDefault(False)
        self.pushButton_910.setDefault(False)
        self.pushButton_910.setFlat(True)
        self.pushButton_910.setObjectName("pushButton_910")
        self.pushButton_910.hide()
        self.gridLayout.addWidget(self.pushButton_910, 9, 10, 1, 1)

        self.pushButton_911 = QtWidgets.QPushButton(Formiki)
        self.pushButton_911.setEnabled(True)
        self.pushButton_911.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_911.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_911.setFont(font)
        self.pushButton_911.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_911.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_911.setAutoFillBackground(False)
        self.pushButton_911.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_911.setAutoDefault(False)
        self.pushButton_911.setDefault(False)
        self.pushButton_911.setFlat(True)
        self.pushButton_911.setObjectName("pushButton_911")
        self.pushButton_911.hide()
        self.gridLayout.addWidget(self.pushButton_911, 9, 11, 1, 1)

        self.pushButton_100 = QtWidgets.QPushButton(Formiki)
        self.pushButton_100.setEnabled(True)
        self.pushButton_100.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_100.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_100.setFont(font)
        self.pushButton_100.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_100.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_100.setAutoFillBackground(False)
        self.pushButton_100.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_100.setAutoDefault(False)
        self.pushButton_100.setDefault(False)
        self.pushButton_100.setFlat(True)
        self.pushButton_100.setObjectName("pushButton_100")
        self.pushButton_100.hide()
        self.gridLayout.addWidget(self.pushButton_100, 10, 0, 1, 1)

        self.pushButton_101 = QtWidgets.QPushButton(Formiki)
        self.pushButton_101.setEnabled(True)
        self.pushButton_101.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_101.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_101.setFont(font)
        self.pushButton_101.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_101.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_101.setAutoFillBackground(False)
        self.pushButton_101.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_101.setAutoDefault(False)
        self.pushButton_101.setDefault(False)
        self.pushButton_101.setFlat(True)
        self.pushButton_101.setObjectName("pushButton_101")
        self.pushButton_101.hide()
        self.gridLayout.addWidget(self.pushButton_101, 10, 1, 1, 1)

        self.pushButton_102 = QtWidgets.QPushButton(Formiki)
        self.pushButton_102.setEnabled(True)
        self.pushButton_102.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_102.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_102.setFont(font)
        self.pushButton_102.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_102.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_102.setAutoFillBackground(False)
        self.pushButton_102.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_102.setAutoDefault(False)
        self.pushButton_102.setDefault(False)
        self.pushButton_102.setFlat(True)
        self.pushButton_102.setObjectName("pushButton_102")
        self.pushButton_102.hide()
        self.gridLayout.addWidget(self.pushButton_102, 10, 2, 1, 1)

        self.pushButton_103 = QtWidgets.QPushButton(Formiki)
        self.pushButton_103.setEnabled(True)
        self.pushButton_103.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_103.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_103.setFont(font)
        self.pushButton_103.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_103.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_103.setAutoFillBackground(False)
        self.pushButton_103.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_103.setAutoDefault(False)
        self.pushButton_103.setDefault(False)
        self.pushButton_103.setFlat(True)
        self.pushButton_103.setObjectName("pushButton_103")
        self.pushButton_103.hide()
        self.gridLayout.addWidget(self.pushButton_103, 10, 3, 1, 1)

        self.pushButton_104 = QtWidgets.QPushButton(Formiki)
        self.pushButton_104.setEnabled(True)
        self.pushButton_104.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_104.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_104.setFont(font)
        self.pushButton_104.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_104.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_104.setAutoFillBackground(False)
        self.pushButton_104.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_104.setAutoDefault(False)
        self.pushButton_104.setDefault(False)
        self.pushButton_104.setFlat(True)
        self.pushButton_104.setObjectName("pushButton_104")
        self.pushButton_104.hide()
        self.gridLayout.addWidget(self.pushButton_104, 10, 4, 1, 1)

        self.pushButton_105 = QtWidgets.QPushButton(Formiki)
        self.pushButton_105.setEnabled(True)
        self.pushButton_105.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_105.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_105.setFont(font)
        self.pushButton_105.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_105.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_105.setAutoFillBackground(False)
        self.pushButton_105.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_105.setAutoDefault(False)
        self.pushButton_105.setDefault(False)
        self.pushButton_105.setFlat(True)
        self.pushButton_105.setObjectName("pushButton_105")
        self.pushButton_105.hide()
        self.gridLayout.addWidget(self.pushButton_105, 10, 5, 1, 1)

        self.pushButton_106 = QtWidgets.QPushButton(Formiki)
        self.pushButton_106.setEnabled(True)
        self.pushButton_106.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_106.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_106.setFont(font)
        self.pushButton_106.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_106.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_106.setAutoFillBackground(False)
        self.pushButton_106.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_106.setAutoDefault(False)
        self.pushButton_106.setDefault(False)
        self.pushButton_106.setFlat(True)
        self.pushButton_106.setObjectName("pushButton_106")
        self.pushButton_106.hide()
        self.gridLayout.addWidget(self.pushButton_106, 10, 6, 1, 1)

        self.pushButton_107 = QtWidgets.QPushButton(Formiki)
        self.pushButton_107.setEnabled(True)
        self.pushButton_107.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_107.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_107.setFont(font)
        self.pushButton_107.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_107.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_107.setAutoFillBackground(False)
        self.pushButton_107.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_107.setAutoDefault(False)
        self.pushButton_107.setDefault(False)
        self.pushButton_107.setFlat(True)
        self.pushButton_107.setObjectName("pushButton_107")
        self.pushButton_107.hide()
        self.gridLayout.addWidget(self.pushButton_107, 10, 7, 1, 1)

        self.pushButton_108 = QtWidgets.QPushButton(Formiki)
        self.pushButton_108.setEnabled(True)
        self.pushButton_108.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_108.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_108.setFont(font)
        self.pushButton_108.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_108.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_108.setAutoFillBackground(False)
        self.pushButton_108.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_108.setAutoDefault(False)
        self.pushButton_108.setDefault(False)
        self.pushButton_108.setFlat(True)
        self.pushButton_108.setObjectName("pushButton_108")
        self.pushButton_108.hide()
        self.gridLayout.addWidget(self.pushButton_108, 10, 8, 1, 1)

        self.pushButton_109 = QtWidgets.QPushButton(Formiki)
        self.pushButton_109.setEnabled(True)
        self.pushButton_109.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_109.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_109.setFont(font)
        self.pushButton_109.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_109.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_109.setAutoFillBackground(False)
        self.pushButton_109.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_109.setAutoDefault(False)
        self.pushButton_109.setDefault(False)
        self.pushButton_109.setFlat(True)
        self.pushButton_109.setObjectName("pushButton_109")
        self.pushButton_109.hide()
        self.gridLayout.addWidget(self.pushButton_109, 10, 9, 1, 1)

        self.pushButton_1010 = QtWidgets.QPushButton(Formiki)
        self.pushButton_1010.setEnabled(True)
        self.pushButton_1010.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_1010.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_1010.setFont(font)
        self.pushButton_1010.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1010.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_1010.setAutoFillBackground(False)
        self.pushButton_1010.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_1010.setAutoDefault(False)
        self.pushButton_1010.setDefault(False)
        self.pushButton_1010.setFlat(True)
        self.pushButton_1010.setObjectName("pushButton_1010")
        self.pushButton_1010.hide()
        self.gridLayout.addWidget(self.pushButton_1010, 10, 10, 1, 1)

        self.pushButton_1011 = QtWidgets.QPushButton(Formiki)
        self.pushButton_1011.setEnabled(True)
        self.pushButton_1011.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_1011.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_1011.setFont(font)
        self.pushButton_1011.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1011.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_1011.setAutoFillBackground(False)
        self.pushButton_1011.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_1011.setAutoDefault(False)
        self.pushButton_1011.setDefault(False)
        self.pushButton_1011.setFlat(True)
        self.pushButton_1011.setObjectName("pushButton_1011")
        self.pushButton_1011.hide()
        self.gridLayout.addWidget(self.pushButton_1011, 10, 11, 1, 1)

        self.pushButton_1100 = QtWidgets.QPushButton(Formiki)
        self.pushButton_1100.setEnabled(True)
        self.pushButton_1100.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_1100.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_1100.setFont(font)
        self.pushButton_1100.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1100.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_1100.setAutoFillBackground(False)
        self.pushButton_1100.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_1100.setAutoDefault(False)
        self.pushButton_1100.setDefault(False)
        self.pushButton_1100.setFlat(True)
        self.pushButton_1100.setObjectName("pushButton_1100")
        self.pushButton_1100.hide()
        self.gridLayout.addWidget(self.pushButton_1100, 11, 0, 1, 1)

        self.pushButton_1111 = QtWidgets.QPushButton(Formiki)
        self.pushButton_1111.setEnabled(True)
        self.pushButton_1111.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_1111.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_1111.setFont(font)
        self.pushButton_1111.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1111.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_1111.setAutoFillBackground(False)
        self.pushButton_1111.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_1111.setAutoDefault(False)
        self.pushButton_1111.setDefault(False)
        self.pushButton_1111.setFlat(True)
        self.pushButton_1111.setObjectName("pushButton_1111")
        self.pushButton_1111.hide()
        self.gridLayout.addWidget(self.pushButton_1111, 11, 1, 1, 1)

        self.pushButton_112 = QtWidgets.QPushButton(Formiki)
        self.pushButton_112.setEnabled(True)
        self.pushButton_112.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_112.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_112.setFont(font)
        self.pushButton_112.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_112.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_112.setAutoFillBackground(False)
        self.pushButton_112.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_112.setAutoDefault(False)
        self.pushButton_112.setDefault(False)
        self.pushButton_112.setFlat(True)
        self.pushButton_112.setObjectName("pushButton_112")
        self.pushButton_112.hide()
        self.gridLayout.addWidget(self.pushButton_112, 11, 2, 1, 1)

        self.pushButton_113 = QtWidgets.QPushButton(Formiki)
        self.pushButton_113.setEnabled(True)
        self.pushButton_113.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_113.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_113.setFont(font)
        self.pushButton_113.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_113.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_113.setAutoFillBackground(False)
        self.pushButton_113.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_113.setAutoDefault(False)
        self.pushButton_113.setDefault(False)
        self.pushButton_113.setFlat(True)
        self.pushButton_113.setObjectName("pushButton_113")
        self.pushButton_113.hide()
        self.gridLayout.addWidget(self.pushButton_113, 11, 3, 1, 1)

        self.pushButton_114 = QtWidgets.QPushButton(Formiki)
        self.pushButton_114.setEnabled(True)
        self.pushButton_114.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_114.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_114.setFont(font)
        self.pushButton_114.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_114.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_114.setAutoFillBackground(False)
        self.pushButton_114.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_114.setAutoDefault(False)
        self.pushButton_114.setDefault(False)
        self.pushButton_114.setFlat(True)
        self.pushButton_114.setObjectName("pushButton_114")
        self.pushButton_114.hide()
        self.gridLayout.addWidget(self.pushButton_114, 11, 4, 1, 1)

        self.pushButton_115 = QtWidgets.QPushButton(Formiki)
        self.pushButton_115.setEnabled(True)
        self.pushButton_115.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_115.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_115.setFont(font)
        self.pushButton_115.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_115.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_115.setAutoFillBackground(False)
        self.pushButton_115.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_115.setAutoDefault(False)
        self.pushButton_115.setDefault(False)
        self.pushButton_115.setFlat(True)
        self.pushButton_115.setObjectName("pushButton_115")
        self.pushButton_115.hide()
        self.gridLayout.addWidget(self.pushButton_115, 11, 5, 1, 1)

        self.pushButton_116 = QtWidgets.QPushButton(Formiki)
        self.pushButton_116.setEnabled(True)
        self.pushButton_116.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_116.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_116.setFont(font)
        self.pushButton_116.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_116.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_116.setAutoFillBackground(False)
        self.pushButton_116.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_116.setAutoDefault(False)
        self.pushButton_116.setDefault(False)
        self.pushButton_116.setFlat(True)
        self.pushButton_116.setObjectName("pushButton_116")
        self.pushButton_116.hide()
        self.gridLayout.addWidget(self.pushButton_116, 11, 6, 1, 1)

        self.pushButton_117 = QtWidgets.QPushButton(Formiki)
        self.pushButton_117.setEnabled(True)
        self.pushButton_117.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_117.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_117.setFont(font)
        self.pushButton_117.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_117.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_117.setAutoFillBackground(False)
        self.pushButton_117.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_117.setAutoDefault(False)
        self.pushButton_117.setDefault(False)
        self.pushButton_117.setFlat(True)
        self.pushButton_117.setObjectName("pushButton_117")
        self.pushButton_117.hide()
        self.gridLayout.addWidget(self.pushButton_117, 11, 7, 1, 1)

        self.pushButton_118 = QtWidgets.QPushButton(Formiki)
        self.pushButton_118.setEnabled(True)
        self.pushButton_118.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_118.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_118.setFont(font)
        self.pushButton_118.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_118.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_118.setAutoFillBackground(False)
        self.pushButton_118.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_118.setAutoDefault(False)
        self.pushButton_118.setDefault(False)
        self.pushButton_118.setFlat(True)
        self.pushButton_118.setObjectName("pushButton_118")
        self.pushButton_118.hide()
        self.gridLayout.addWidget(self.pushButton_118, 11, 8, 1, 1)

        self.pushButton_119 = QtWidgets.QPushButton(Formiki)
        self.pushButton_119.setEnabled(True)
        self.pushButton_119.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_119.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_119.setFont(font)
        self.pushButton_119.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_119.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_119.setAutoFillBackground(False)
        self.pushButton_119.setStyleSheet(" color: #303030;\n"
                                         "\n"
                                         "background: #e87461 ;\n"
                                         "border: 2px solid #303030;\n"
                                         "    border-radius: 20px;\n"
                                         "    border-style: outset;\n"
                                         "\n"
                                         "Text-align:center")
        self.pushButton_119.setAutoDefault(False)
        self.pushButton_119.setDefault(False)
        self.pushButton_119.setFlat(True)
        self.pushButton_119.setObjectName("pushButton_119")
        self.pushButton_119.hide()
        self.gridLayout.addWidget(self.pushButton_119, 11, 9, 1, 1)

        self.pushButton_11110 = QtWidgets.QPushButton(Formiki)
        self.pushButton_11110.setEnabled(True)
        self.pushButton_11110.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_11110.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_11110.setFont(font)
        self.pushButton_11110.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11110.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_11110.setAutoFillBackground(False)
        self.pushButton_11110.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_11110.setAutoDefault(False)
        self.pushButton_11110.setDefault(False)
        self.pushButton_11110.setFlat(True)
        self.pushButton_11110.setObjectName("pushButton_11110")
        self.pushButton_11110.hide()
        self.gridLayout.addWidget(self.pushButton_11110, 11, 10, 1, 1)

        self.pushButton_11111 = QtWidgets.QPushButton(Formiki)
        self.pushButton_11111.setEnabled(True)
        self.pushButton_11111.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_11111.setMaximumSize(QtCore.QSize(300, 300))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_11111.setFont(font)
        self.pushButton_11111.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11111.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_11111.setAutoFillBackground(False)
        self.pushButton_11111.setStyleSheet(" color: #303030;\n"
                                          "\n"
                                          "background: #e87461 ;\n"
                                          "border: 2px solid #303030;\n"
                                          "    border-radius: 20px;\n"
                                          "    border-style: outset;\n"
                                          "\n"
                                          "Text-align:center")
        self.pushButton_11111.setAutoDefault(False)
        self.pushButton_11111.setDefault(False)
        self.pushButton_11111.setFlat(True)
        self.pushButton_11111.setObjectName("pushButton_11111")
        self.pushButton_11111.hide()
        self.gridLayout.addWidget(self.pushButton_11111, 11, 11, 1, 1)


        """TOGGLES"""
        self.pushButton_00.setCheckable(True)
        self.pushButton_01.setCheckable(True)
        self.pushButton_02.setCheckable(True)
        self.pushButton_03.setCheckable(True)
        self.pushButton_04.setCheckable(True)
        self.pushButton_05.setCheckable(True)
        self.pushButton_06.setCheckable(True)
        self.pushButton_07.setCheckable(True)
        self.pushButton_08.setCheckable(True)
        self.pushButton_09.setCheckable(True)
        self.pushButton_010.setCheckable(True)
        self.pushButton_011.setCheckable(True)

        self.pushButton_10.setCheckable(True)
        self.pushButton_11.setCheckable(True)
        self.pushButton_12.setCheckable(True)
        self.pushButton_13.setCheckable(True)
        self.pushButton_14.setCheckable(True)
        self.pushButton_15.setCheckable(True)
        self.pushButton_16.setCheckable(True)
        self.pushButton_17.setCheckable(True)
        self.pushButton_18.setCheckable(True)
        self.pushButton_19.setCheckable(True)
        self.pushButton_110.setCheckable(True)
        self.pushButton_111.setCheckable(True)

        self.pushButton_20.setCheckable(True)
        self.pushButton_21.setCheckable(True)
        self.pushButton_22.setCheckable(True)
        self.pushButton_23.setCheckable(True)
        self.pushButton_24.setCheckable(True)
        self.pushButton_25.setCheckable(True)
        self.pushButton_26.setCheckable(True)
        self.pushButton_27.setCheckable(True)
        self.pushButton_28.setCheckable(True)
        self.pushButton_29.setCheckable(True)
        self.pushButton_210.setCheckable(True)
        self.pushButton_211.setCheckable(True)

        self.pushButton_30.setCheckable(True)
        self.pushButton_31.setCheckable(True)
        self.pushButton_32.setCheckable(True)
        self.pushButton_33.setCheckable(True)
        self.pushButton_34.setCheckable(True)
        self.pushButton_35.setCheckable(True)
        self.pushButton_36.setCheckable(True)
        self.pushButton_37.setCheckable(True)
        self.pushButton_38.setCheckable(True)
        self.pushButton_39.setCheckable(True)
        self.pushButton_310.setCheckable(True)
        self.pushButton_311.setCheckable(True)

        self.pushButton_40.setCheckable(True)
        self.pushButton_41.setCheckable(True)
        self.pushButton_42.setCheckable(True)
        self.pushButton_43.setCheckable(True)
        self.pushButton_44.setCheckable(True)
        self.pushButton_45.setCheckable(True)
        self.pushButton_46.setCheckable(True)
        self.pushButton_47.setCheckable(True)
        self.pushButton_48.setCheckable(True)
        self.pushButton_49.setCheckable(True)
        self.pushButton_410.setCheckable(True)
        self.pushButton_411.setCheckable(True)

        self.pushButton_50.setCheckable(True)
        self.pushButton_51.setCheckable(True)
        self.pushButton_52.setCheckable(True)
        self.pushButton_53.setCheckable(True)
        self.pushButton_54.setCheckable(True)
        self.pushButton_55.setCheckable(True)
        self.pushButton_56.setCheckable(True)
        self.pushButton_57.setCheckable(True)
        self.pushButton_58.setCheckable(True)
        self.pushButton_59.setCheckable(True)
        self.pushButton_510.setCheckable(True)
        self.pushButton_511.setCheckable(True)

        self.pushButton_60.setCheckable(True)
        self.pushButton_61.setCheckable(True)
        self.pushButton_62.setCheckable(True)
        self.pushButton_63.setCheckable(True)
        self.pushButton_64.setCheckable(True)
        self.pushButton_65.setCheckable(True)
        self.pushButton_66.setCheckable(True)
        self.pushButton_67.setCheckable(True)
        self.pushButton_68.setCheckable(True)
        self.pushButton_69.setCheckable(True)
        self.pushButton_610.setCheckable(True)
        self.pushButton_611.setCheckable(True)

        self.pushButton_70.setCheckable(True)
        self.pushButton_71.setCheckable(True)
        self.pushButton_72.setCheckable(True)
        self.pushButton_73.setCheckable(True)
        self.pushButton_74.setCheckable(True)
        self.pushButton_75.setCheckable(True)
        self.pushButton_76.setCheckable(True)
        self.pushButton_77.setCheckable(True)
        self.pushButton_78.setCheckable(True)
        self.pushButton_79.setCheckable(True)
        self.pushButton_710.setCheckable(True)
        self.pushButton_711.setCheckable(True)

        self.pushButton_80.setCheckable(True)
        self.pushButton_81.setCheckable(True)
        self.pushButton_82.setCheckable(True)
        self.pushButton_83.setCheckable(True)
        self.pushButton_84.setCheckable(True)
        self.pushButton_85.setCheckable(True)
        self.pushButton_86.setCheckable(True)
        self.pushButton_87.setCheckable(True)
        self.pushButton_88.setCheckable(True)
        self.pushButton_89.setCheckable(True)
        self.pushButton_810.setCheckable(True)
        self.pushButton_811.setCheckable(True)

        self.pushButton_90.setCheckable(True)
        self.pushButton_91.setCheckable(True)
        self.pushButton_92.setCheckable(True)
        self.pushButton_93.setCheckable(True)
        self.pushButton_94.setCheckable(True)
        self.pushButton_95.setCheckable(True)
        self.pushButton_96.setCheckable(True)
        self.pushButton_97.setCheckable(True)
        self.pushButton_98.setCheckable(True)
        self.pushButton_99.setCheckable(True)
        self.pushButton_910.setCheckable(True)
        self.pushButton_911.setCheckable(True)

        self.pushButton_100.setCheckable(True)
        self.pushButton_101.setCheckable(True)
        self.pushButton_102.setCheckable(True)
        self.pushButton_103.setCheckable(True)
        self.pushButton_104.setCheckable(True)
        self.pushButton_105.setCheckable(True)
        self.pushButton_106.setCheckable(True)
        self.pushButton_107.setCheckable(True)
        self.pushButton_108.setCheckable(True)
        self.pushButton_109.setCheckable(True)
        self.pushButton_1010.setCheckable(True)
        self.pushButton_1011.setCheckable(True)

        self.pushButton_1100.setCheckable(True)
        self.pushButton_1111.setCheckable(True)
        self.pushButton_112.setCheckable(True)
        self.pushButton_113.setCheckable(True)
        self.pushButton_114.setCheckable(True)
        self.pushButton_115.setCheckable(True)
        self.pushButton_116.setCheckable(True)
        self.pushButton_117.setCheckable(True)
        self.pushButton_118.setCheckable(True)
        self.pushButton_119.setCheckable(True)
        self.pushButton_11110.setCheckable(True)
        self.pushButton_11111.setCheckable(True)


        self.retranslateUi(Formiki)
        QtCore.QMetaObject.connectSlotsByName(Formiki)

    """ BOARD SETTINGS """

    def __init__(self, Formiki, board=None, size=6, trie=None, words=None, seconds=120):
        self.n = size
        self.w = ""
        self.wordlist = []
        self.chain = []
        self.directions = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]
        self.paths = []
        self.ctd = seconds
        self.sec = None
        self.dfsed = False

        self.t1 = Thread(target=self.countdown, args=(self.ctd,))

        self.font = QtGui.QFont()
        self.font.setPointSize(12)
        self.font.setFamily("Cambria")
        



        """ COLORS """
        self.blue = " color: #303030;\n""\n""background: #74b9ff ;\n""border: 2px solid #303030;\n""    border-radius: 20px;\n""    border-style: outset;\n""\n""Text-align:center;"

        self.defa = " color: #303030;\n""\n""background: #e87461 ;\n""border: 2px solid #303030;\n""border-radius: 20px;\n""border-style: outset;\n" "\n""Text-align:center"

        self.green = " color: #303030;\n""\n""background: #55efc4 ;\n""border: 2px solid #303030;\n""    border-radius: 20px;\n""    border-style: outset;\n""\n""Text-align:center;"

        self.red = " color: #303030;\n""\n""background: #d63031 ;\n""border: 2px solid #303030;\n""    border-radius: 20px;\n""    border-style: outset;\n""\n""Text-align:center;"
        self.darkblue = " color: #303030;\n""\n""background: #0984e3 ;\n""border: 2px solid #303030;\n""    border-radius: 20px;\n""    border-style: outset;\n""\n""Text-align:center;"
        
        """ SHORTCUT-KEY BINDINGS """
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape), Formiki)
        
        
        self
        if board is None:
            self.board = Board(n=self.n)
        else:
            self.board = board

        if words is None:
            self.words = Words()
        else:
            self.words = words

        if trie is None:
            self.trie = self.words.trie()
        else:
            self.trie = trie

        if self.n > 4:
            a= 700
            b=515
            Formiki.resize(a + self.n*(2*9), b+self.n*(2*16))

        # for i in range(self.n):
        #     for j in range(self.n):
        #         startChar = self.board.letters[i][j]
        #         temp = copy.deepcopy(self.board.letters)
        #         temp[i][j] = '-'
        #         Board.dfs(self.board, temp, self.trie, (i,j), startChar, False, None, False, None, [(i,j)], delay=0)

    def retranslateUi(self, Formiki):
        _translate = QtCore.QCoreApplication.translate
        Formiki.setWindowTitle(_translate("Formiki", "Formiki"))
        self.lineEdit.setPlaceholderText(_translate("Formiki", "Enter:"))
        self.pushButton_00.setText(_translate("Formiki", self.board.letters[0][0]))
        self.pushButton_01.setText(_translate("Formiki", self.board.letters[0][1]))
        self.pushButton_02.setText(_translate("Formiki", self.board.letters[0][2]))
        self.pushButton_03.setText(_translate("Formiki", self.board.letters[0][3]))
        try:
            self.pushButton_04.setText(_translate("Formiki", self.board.letters[0][4]))
            self.pushButton_05.setText(_translate("Formiki", self.board.letters[0][5]))
            self.pushButton_06.setText(_translate("Formiki", self.board.letters[0][6]))
            self.pushButton_07.setText(_translate("Formiki", self.board.letters[0][7]))
            self.pushButton_08.setText(_translate("Formiki", self.board.letters[0][8]))
            self.pushButton_09.setText(_translate("Formiki", self.board.letters[0][9]))
            self.pushButton_010.setText(_translate("Formiki", self.board.letters[0][10]))
            self.pushButton_011.setText(_translate("Formiki", self.board.letters[0][11]))
        except:
            pass

        self.pushButton_10.setText(_translate("Formiki", self.board.letters[1][0]))
        self.pushButton_11.setText(_translate("Formiki", self.board.letters[1][1]))
        self.pushButton_12.setText(_translate("Formiki", self.board.letters[1][2]))
        self.pushButton_13.setText(_translate("Formiki", self.board.letters[1][3]))
        try:
            self.pushButton_14.setText(_translate("Formiki", self.board.letters[1][4]))
            self.pushButton_15.setText(_translate("Formiki", self.board.letters[1][5]))
            self.pushButton_16.setText(_translate("Formiki", self.board.letters[1][6]))
            self.pushButton_17.setText(_translate("Formiki", self.board.letters[1][7]))
            self.pushButton_18.setText(_translate("Formiki", self.board.letters[1][8]))
            self.pushButton_19.setText(_translate("Formiki", self.board.letters[1][9]))
            self.pushButton_110.setText(_translate("Formiki", self.board.letters[1][10]))
            self.pushButton_111.setText(_translate("Formiki", self.board.letters[1][11]))
        except:
            pass

        self.pushButton_20.setText(_translate("Formiki", self.board.letters[2][0]))
        self.pushButton_21.setText(_translate("Formiki", self.board.letters[2][1]))
        self.pushButton_22.setText(_translate("Formiki", self.board.letters[2][2]))
        self.pushButton_23.setText(_translate("Formiki", self.board.letters[2][3]))
        try:
            self.pushButton_24.setText(_translate("Formiki", self.board.letters[2][4]))
            self.pushButton_25.setText(_translate("Formiki", self.board.letters[2][5]))
            self.pushButton_26.setText(_translate("Formiki", self.board.letters[2][6]))
            self.pushButton_27.setText(_translate("Formiki", self.board.letters[2][7]))
            self.pushButton_28.setText(_translate("Formiki", self.board.letters[2][8]))
            self.pushButton_29.setText(_translate("Formiki", self.board.letters[2][9]))
            self.pushButton_210.setText(_translate("Formiki", self.board.letters[2][10]))
            self.pushButton_211.setText(_translate("Formiki", self.board.letters[2][11]))
        except:
            pass

        self.pushButton_30.setText(_translate("Formiki", self.board.letters[3][0]))
        self.pushButton_31.setText(_translate("Formiki", self.board.letters[3][1]))
        self.pushButton_32.setText(_translate("Formiki", self.board.letters[3][2]))
        self.pushButton_33.setText(_translate("Formiki", self.board.letters[3][3]))
        try:
            self.pushButton_34.setText(_translate("Formiki", self.board.letters[3][4]))
            self.pushButton_35.setText(_translate("Formiki", self.board.letters[3][5]))
            self.pushButton_36.setText(_translate("Formiki", self.board.letters[3][6]))
            self.pushButton_37.setText(_translate("Formiki", self.board.letters[3][7]))
            self.pushButton_38.setText(_translate("Formiki", self.board.letters[3][8]))
            self.pushButton_39.setText(_translate("Formiki", self.board.letters[3][9]))
            self.pushButton_310.setText(_translate("Formiki", self.board.letters[3][10]))
            self.pushButton_311.setText(_translate("Formiki", self.board.letters[3][11]))
        except:
            pass
        try:
            self.pushButton_40.setText(_translate("Formiki", self.board.letters[4][0]))
            self.pushButton_41.setText(_translate("Formiki", self.board.letters[4][1]))
            self.pushButton_42.setText(_translate("Formiki", self.board.letters[4][2]))
            self.pushButton_43.setText(_translate("Formiki", self.board.letters[4][3]))
            self.pushButton_44.setText(_translate("Formiki", self.board.letters[4][4]))
            self.pushButton_45.setText(_translate("Formiki", self.board.letters[4][5]))
            self.pushButton_46.setText(_translate("Formiki", self.board.letters[4][6]))
            self.pushButton_47.setText(_translate("Formiki", self.board.letters[4][7]))
            self.pushButton_48.setText(_translate("Formiki", self.board.letters[4][8]))
            self.pushButton_49.setText(_translate("Formiki", self.board.letters[4][9]))
            self.pushButton_410.setText(_translate("Formiki", self.board.letters[4][10]))
            self.pushButton_411.setText(_translate("Formiki", self.board.letters[4][11]))
        except:
            pass

        try:
            self.pushButton_50.setText(_translate("Formiki", self.board.letters[5][0]))
            self.pushButton_51.setText(_translate("Formiki", self.board.letters[5][1]))
            self.pushButton_52.setText(_translate("Formiki", self.board.letters[5][2]))
            self.pushButton_53.setText(_translate("Formiki", self.board.letters[5][3]))
            self.pushButton_54.setText(_translate("Formiki", self.board.letters[5][4]))
            self.pushButton_55.setText(_translate("Formiki", self.board.letters[5][5]))
            self.pushButton_56.setText(_translate("Formiki", self.board.letters[5][6]))
            self.pushButton_57.setText(_translate("Formiki", self.board.letters[5][7]))
            self.pushButton_58.setText(_translate("Formiki", self.board.letters[5][8]))
            self.pushButton_59.setText(_translate("Formiki", self.board.letters[5][9]))
            self.pushButton_510.setText(_translate("Formiki", self.board.letters[5][10]))
            self.pushButton_511.setText(_translate("Formiki", self.board.letters[5][11]))
        except:
            pass

        try:
            self.pushButton_60.setText(_translate("Formiki", self.board.letters[6][0]))
            self.pushButton_61.setText(_translate("Formiki", self.board.letters[6][1]))
            self.pushButton_62.setText(_translate("Formiki", self.board.letters[6][2]))
            self.pushButton_63.setText(_translate("Formiki", self.board.letters[6][3]))
            self.pushButton_64.setText(_translate("Formiki", self.board.letters[6][4]))
            self.pushButton_65.setText(_translate("Formiki", self.board.letters[6][5]))
            self.pushButton_66.setText(_translate("Formiki", self.board.letters[6][6]))
            self.pushButton_67.setText(_translate("Formiki", self.board.letters[6][7]))
            self.pushButton_68.setText(_translate("Formiki", self.board.letters[6][8]))
            self.pushButton_69.setText(_translate("Formiki", self.board.letters[6][9]))
            self.pushButton_610.setText(_translate("Formiki", self.board.letters[6][10]))
            self.pushButton_611.setText(_translate("Formiki", self.board.letters[6][11]))
        except:
            pass

        try:
            self.pushButton_70.setText(_translate("Formiki", self.board.letters[7][0]))
            self.pushButton_71.setText(_translate("Formiki", self.board.letters[7][1]))
            self.pushButton_72.setText(_translate("Formiki", self.board.letters[7][2]))
            self.pushButton_73.setText(_translate("Formiki", self.board.letters[7][3]))
            self.pushButton_74.setText(_translate("Formiki", self.board.letters[7][4]))
            self.pushButton_75.setText(_translate("Formiki", self.board.letters[7][5]))
            self.pushButton_76.setText(_translate("Formiki", self.board.letters[7][6]))
            self.pushButton_77.setText(_translate("Formiki", self.board.letters[7][7]))
            self.pushButton_78.setText(_translate("Formiki", self.board.letters[7][8]))
            self.pushButton_79.setText(_translate("Formiki", self.board.letters[7][9]))
            self.pushButton_710.setText(_translate("Formiki", self.board.letters[7][10]))
            self.pushButton_711.setText(_translate("Formiki", self.board.letters[7][11]))
        except:
            pass

        try:
            self.pushButton_80.setText(_translate("Formiki", self.board.letters[8][0]))
            self.pushButton_81.setText(_translate("Formiki", self.board.letters[8][1]))
            self.pushButton_82.setText(_translate("Formiki", self.board.letters[8][2]))
            self.pushButton_83.setText(_translate("Formiki", self.board.letters[8][3]))
            self.pushButton_84.setText(_translate("Formiki", self.board.letters[8][4]))
            self.pushButton_85.setText(_translate("Formiki", self.board.letters[8][5]))
            self.pushButton_86.setText(_translate("Formiki", self.board.letters[8][6]))
            self.pushButton_87.setText(_translate("Formiki", self.board.letters[8][7]))
            self.pushButton_88.setText(_translate("Formiki", self.board.letters[8][8]))
            self.pushButton_89.setText(_translate("Formiki", self.board.letters[8][9]))
            self.pushButton_810.setText(_translate("Formiki", self.board.letters[8][10]))
            self.pushButton_811.setText(_translate("Formiki", self.board.letters[8][11]))
        except:
            pass

        try:
            self.pushButton_90.setText(_translate("Formiki", self.board.letters[9][0]))
            self.pushButton_91.setText(_translate("Formiki", self.board.letters[9][1]))
            self.pushButton_92.setText(_translate("Formiki", self.board.letters[9][2]))
            self.pushButton_93.setText(_translate("Formiki", self.board.letters[9][3]))
            self.pushButton_94.setText(_translate("Formiki", self.board.letters[9][4]))
            self.pushButton_95.setText(_translate("Formiki", self.board.letters[9][5]))
            self.pushButton_96.setText(_translate("Formiki", self.board.letters[9][6]))
            self.pushButton_97.setText(_translate("Formiki", self.board.letters[9][7]))
            self.pushButton_98.setText(_translate("Formiki", self.board.letters[9][8]))
            self.pushButton_99.setText(_translate("Formiki", self.board.letters[9][9]))
            self.pushButton_910.setText(_translate("Formiki", self.board.letters[9][10]))
            self.pushButton_911.setText(_translate("Formiki", self.board.letters[9][11]))

        except:
            pass

        try:
            self.pushButton_100.setText(_translate("Formiki", self.board.letters[10][0]))
            self.pushButton_101.setText(_translate("Formiki", self.board.letters[10][1]))
            self.pushButton_102.setText(_translate("Formiki", self.board.letters[10][2]))
            self.pushButton_103.setText(_translate("Formiki", self.board.letters[10][3]))
            self.pushButton_104.setText(_translate("Formiki", self.board.letters[10][4]))
            self.pushButton_105.setText(_translate("Formiki", self.board.letters[10][5]))
            self.pushButton_106.setText(_translate("Formiki", self.board.letters[10][6]))
            self.pushButton_107.setText(_translate("Formiki", self.board.letters[10][7]))
            self.pushButton_108.setText(_translate("Formiki", self.board.letters[10][8]))
            self.pushButton_109.setText(_translate("Formiki", self.board.letters[10][9]))
            self.pushButton_1010.setText(_translate("Formiki", self.board.letters[10][10]))
            self.pushButton_1011.setText(_translate("Formiki", self.board.letters[10][11]))
        except:
            pass

        try:
            self.pushButton_1100.setText(_translate("Formiki", self.board.letters[11][0]))
            self.pushButton_1111.setText(_translate("Formiki", self.board.letters[11][1]))
            self.pushButton_112.setText(_translate("Formiki", self.board.letters[11][2]))
            self.pushButton_113.setText(_translate("Formiki", self.board.letters[11][3]))
            self.pushButton_114.setText(_translate("Formiki", self.board.letters[11][4]))
            self.pushButton_115.setText(_translate("Formiki", self.board.letters[11][5]))
            self.pushButton_116.setText(_translate("Formiki", self.board.letters[11][6]))
            self.pushButton_117.setText(_translate("Formiki", self.board.letters[11][7]))
            self.pushButton_118.setText(_translate("Formiki", self.board.letters[11][8]))
            self.pushButton_119.setText(_translate("Formiki", self.board.letters[11][9]))
            self.pushButton_11110.setText(_translate("Formiki", self.board.letters[11][10]))
            self.pushButton_11111.setText(_translate("Formiki", self.board.letters[11][11]))
        except:
            pass
        self.label.setText(_translate("Formiki", "Found Words:"))
        self.label_2.setText(_translate("Formiki", "        Total Points:"))
        self.label_3.setText(_translate("Formiki", "Remaining Time:"))
        self.pushButton_3.setText(_translate("Formiki", "Solve"))
        self.pushButton_2.setText(_translate("Formiki", "Cheat"))
        self.pushButton_4.setText(_translate("Formiki", "Start"))
        self.pushButton_5.setText(_translate("Formiki", "Stop"))
        self.pushButton.setText(_translate("Formiki", "Exit"))

        """ BUTTON-FUNCTION CONNECTIONS """

        self.pushButton_3.clicked.connect(lambda: self.vstimestart())
        self.pushButton_2.clicked.connect(lambda: self.cheat())

        self.pushButton_00.clicked[bool].connect(self.vstimesingle)
        self.pushButton_01.clicked[bool].connect(self.vstimesingle)
        self.pushButton_02.clicked[bool].connect(self.vstimesingle)
        self.pushButton_03.clicked[bool].connect(self.vstimesingle)
        self.pushButton_04.clicked[bool].connect(self.vstimesingle)
        self.pushButton_05.clicked[bool].connect(self.vstimesingle)
        self.pushButton_06.clicked[bool].connect(self.vstimesingle)
        self.pushButton_07.clicked[bool].connect(self.vstimesingle)
        self.pushButton_08.clicked[bool].connect(self.vstimesingle)
        self.pushButton_09.clicked[bool].connect(self.vstimesingle)
        self.pushButton_010.clicked[bool].connect(self.vstimesingle)
        self.pushButton_011.clicked[bool].connect(self.vstimesingle)

        self.pushButton_10.clicked[bool].connect(self.vstimesingle)
        self.pushButton_11.clicked[bool].connect(self.vstimesingle)
        self.pushButton_12.clicked[bool].connect(self.vstimesingle)
        self.pushButton_13.clicked[bool].connect(self.vstimesingle)
        self.pushButton_14.clicked[bool].connect(self.vstimesingle)
        self.pushButton_15.clicked[bool].connect(self.vstimesingle)
        self.pushButton_16.clicked[bool].connect(self.vstimesingle)
        self.pushButton_17.clicked[bool].connect(self.vstimesingle)
        self.pushButton_18.clicked[bool].connect(self.vstimesingle)
        self.pushButton_19.clicked[bool].connect(self.vstimesingle)
        self.pushButton_110.clicked[bool].connect(self.vstimesingle)
        self.pushButton_111.clicked[bool].connect(self.vstimesingle)

        self.pushButton_20.clicked[bool].connect(self.vstimesingle)
        self.pushButton_21.clicked[bool].connect(self.vstimesingle)
        self.pushButton_22.clicked[bool].connect(self.vstimesingle)
        self.pushButton_23.clicked[bool].connect(self.vstimesingle)
        self.pushButton_24.clicked[bool].connect(self.vstimesingle)
        self.pushButton_25.clicked[bool].connect(self.vstimesingle)
        self.pushButton_26.clicked[bool].connect(self.vstimesingle)
        self.pushButton_27.clicked[bool].connect(self.vstimesingle)
        self.pushButton_28.clicked[bool].connect(self.vstimesingle)
        self.pushButton_29.clicked[bool].connect(self.vstimesingle)
        self.pushButton_210.clicked[bool].connect(self.vstimesingle)
        self.pushButton_211.clicked[bool].connect(self.vstimesingle)

        self.pushButton_30.clicked[bool].connect(self.vstimesingle)
        self.pushButton_31.clicked[bool].connect(self.vstimesingle)
        self.pushButton_32.clicked[bool].connect(self.vstimesingle)
        self.pushButton_33.clicked[bool].connect(self.vstimesingle)
        self.pushButton_34.clicked[bool].connect(self.vstimesingle)
        self.pushButton_35.clicked[bool].connect(self.vstimesingle)
        self.pushButton_36.clicked[bool].connect(self.vstimesingle)
        self.pushButton_37.clicked[bool].connect(self.vstimesingle)
        self.pushButton_38.clicked[bool].connect(self.vstimesingle)
        self.pushButton_39.clicked[bool].connect(self.vstimesingle)
        self.pushButton_310.clicked[bool].connect(self.vstimesingle)
        self.pushButton_311.clicked[bool].connect(self.vstimesingle)

        self.pushButton_40.clicked[bool].connect(self.vstimesingle)
        self.pushButton_41.clicked[bool].connect(self.vstimesingle)
        self.pushButton_42.clicked[bool].connect(self.vstimesingle)
        self.pushButton_43.clicked[bool].connect(self.vstimesingle)
        self.pushButton_44.clicked[bool].connect(self.vstimesingle)
        self.pushButton_45.clicked[bool].connect(self.vstimesingle)
        self.pushButton_46.clicked[bool].connect(self.vstimesingle)
        self.pushButton_47.clicked[bool].connect(self.vstimesingle)
        self.pushButton_48.clicked[bool].connect(self.vstimesingle)
        self.pushButton_49.clicked[bool].connect(self.vstimesingle)
        self.pushButton_410.clicked[bool].connect(self.vstimesingle)
        self.pushButton_411.clicked[bool].connect(self.vstimesingle)

        self.pushButton_50.clicked[bool].connect(self.vstimesingle)
        self.pushButton_51.clicked[bool].connect(self.vstimesingle)
        self.pushButton_52.clicked[bool].connect(self.vstimesingle)
        self.pushButton_53.clicked[bool].connect(self.vstimesingle)
        self.pushButton_54.clicked[bool].connect(self.vstimesingle)
        self.pushButton_55.clicked[bool].connect(self.vstimesingle)
        self.pushButton_56.clicked[bool].connect(self.vstimesingle)
        self.pushButton_57.clicked[bool].connect(self.vstimesingle)
        self.pushButton_58.clicked[bool].connect(self.vstimesingle)
        self.pushButton_59.clicked[bool].connect(self.vstimesingle)
        self.pushButton_510.clicked[bool].connect(self.vstimesingle)
        self.pushButton_511.clicked[bool].connect(self.vstimesingle)

        self.pushButton_60.clicked[bool].connect(self.vstimesingle)
        self.pushButton_61.clicked[bool].connect(self.vstimesingle)
        self.pushButton_62.clicked[bool].connect(self.vstimesingle)
        self.pushButton_63.clicked[bool].connect(self.vstimesingle)
        self.pushButton_64.clicked[bool].connect(self.vstimesingle)
        self.pushButton_65.clicked[bool].connect(self.vstimesingle)
        self.pushButton_66.clicked[bool].connect(self.vstimesingle)
        self.pushButton_67.clicked[bool].connect(self.vstimesingle)
        self.pushButton_68.clicked[bool].connect(self.vstimesingle)
        self.pushButton_69.clicked[bool].connect(self.vstimesingle)
        self.pushButton_610.clicked[bool].connect(self.vstimesingle)
        self.pushButton_611.clicked[bool].connect(self.vstimesingle)

        self.pushButton_70.clicked[bool].connect(self.vstimesingle)
        self.pushButton_71.clicked[bool].connect(self.vstimesingle)
        self.pushButton_72.clicked[bool].connect(self.vstimesingle)
        self.pushButton_73.clicked[bool].connect(self.vstimesingle)
        self.pushButton_74.clicked[bool].connect(self.vstimesingle)
        self.pushButton_75.clicked[bool].connect(self.vstimesingle)
        self.pushButton_76.clicked[bool].connect(self.vstimesingle)
        self.pushButton_77.clicked[bool].connect(self.vstimesingle)
        self.pushButton_78.clicked[bool].connect(self.vstimesingle)
        self.pushButton_79.clicked[bool].connect(self.vstimesingle)
        self.pushButton_710.clicked[bool].connect(self.vstimesingle)
        self.pushButton_711.clicked[bool].connect(self.vstimesingle)

        self.pushButton_80.clicked[bool].connect(self.vstimesingle)
        self.pushButton_81.clicked[bool].connect(self.vstimesingle)
        self.pushButton_82.clicked[bool].connect(self.vstimesingle)
        self.pushButton_83.clicked[bool].connect(self.vstimesingle)
        self.pushButton_84.clicked[bool].connect(self.vstimesingle)
        self.pushButton_85.clicked[bool].connect(self.vstimesingle)
        self.pushButton_86.clicked[bool].connect(self.vstimesingle)
        self.pushButton_87.clicked[bool].connect(self.vstimesingle)
        self.pushButton_88.clicked[bool].connect(self.vstimesingle)
        self.pushButton_89.clicked[bool].connect(self.vstimesingle)
        self.pushButton_810.clicked[bool].connect(self.vstimesingle)
        self.pushButton_811.clicked[bool].connect(self.vstimesingle)

        self.pushButton_90.clicked[bool].connect(self.vstimesingle)
        self.pushButton_91.clicked[bool].connect(self.vstimesingle)
        self.pushButton_92.clicked[bool].connect(self.vstimesingle)
        self.pushButton_93.clicked[bool].connect(self.vstimesingle)
        self.pushButton_94.clicked[bool].connect(self.vstimesingle)
        self.pushButton_95.clicked[bool].connect(self.vstimesingle)
        self.pushButton_96.clicked[bool].connect(self.vstimesingle)
        self.pushButton_97.clicked[bool].connect(self.vstimesingle)
        self.pushButton_98.clicked[bool].connect(self.vstimesingle)
        self.pushButton_99.clicked[bool].connect(self.vstimesingle)
        self.pushButton_910.clicked[bool].connect(self.vstimesingle)
        self.pushButton_911.clicked[bool].connect(self.vstimesingle)

        self.pushButton_100.clicked[bool].connect(self.vstimesingle)
        self.pushButton_101.clicked[bool].connect(self.vstimesingle)
        self.pushButton_102.clicked[bool].connect(self.vstimesingle)
        self.pushButton_103.clicked[bool].connect(self.vstimesingle)
        self.pushButton_104.clicked[bool].connect(self.vstimesingle)
        self.pushButton_105.clicked[bool].connect(self.vstimesingle)
        self.pushButton_106.clicked[bool].connect(self.vstimesingle)
        self.pushButton_107.clicked[bool].connect(self.vstimesingle)
        self.pushButton_108.clicked[bool].connect(self.vstimesingle)
        self.pushButton_109.clicked[bool].connect(self.vstimesingle)
        self.pushButton_1010.clicked[bool].connect(self.vstimesingle)
        self.pushButton_1011.clicked[bool].connect(self.vstimesingle)

        self.pushButton_1100.clicked[bool].connect(self.vstimesingle)
        self.pushButton_1111.clicked[bool].connect(self.vstimesingle)
        self.pushButton_112.clicked[bool].connect(self.vstimesingle)
        self.pushButton_113.clicked[bool].connect(self.vstimesingle)
        self.pushButton_114.clicked[bool].connect(self.vstimesingle)
        self.pushButton_115.clicked[bool].connect(self.vstimesingle)
        self.pushButton_116.clicked[bool].connect(self.vstimesingle)
        self.pushButton_117.clicked[bool].connect(self.vstimesingle)
        self.pushButton_118.clicked[bool].connect(self.vstimesingle)
        self.pushButton_119.clicked[bool].connect(self.vstimesingle)
        self.pushButton_11110.clicked[bool].connect(self.vstimesingle)
        self.pushButton_11111.clicked[bool].connect(self.vstimesingle)
        
        # Break Buttons
        
        self.pushButton.clicked.connect(self.brokeiki)
        self.pushButton_4.clicked.connect(self.brokeiki)
        self.pushButton_5.clicked.connect(self.brokeiki)

        # Shortcuts
        self.shortcut.activated.connect(self.cleartable)
        
        # Text to Click
        self.lineEdit.textChanged.connect(self.textToClick)

        """ Button List """
        self.blist = [[self.pushButton_00, self.pushButton_01, self.pushButton_02, self.pushButton_03, self.pushButton_04,self.pushButton_05, self.pushButton_06, self.pushButton_07, self.pushButton_08, self.pushButton_09,self.pushButton_010, self.pushButton_011],
                      [self.pushButton_10, self.pushButton_11, self.pushButton_12, self.pushButton_13, self.pushButton_14,self.pushButton_15, self.pushButton_16, self.pushButton_17, self.pushButton_18, self.pushButton_19,self.pushButton_110, self.pushButton_111],
                      [self.pushButton_20, self.pushButton_21, self.pushButton_22, self.pushButton_23, self.pushButton_24,self.pushButton_25, self.pushButton_26, self.pushButton_27, self.pushButton_28, self.pushButton_29,self.pushButton_210, self.pushButton_211],
                      [self.pushButton_30, self.pushButton_31, self.pushButton_32, self.pushButton_33, self.pushButton_34,self.pushButton_35, self.pushButton_36, self.pushButton_37, self.pushButton_38, self.pushButton_39,self.pushButton_310, self.pushButton_311],
                      [self.pushButton_40, self.pushButton_41, self.pushButton_42, self.pushButton_43, self.pushButton_44,self.pushButton_45, self.pushButton_46, self.pushButton_47, self.pushButton_48, self.pushButton_49,self.pushButton_410, self.pushButton_411],
                      [self.pushButton_50, self.pushButton_51, self.pushButton_52, self.pushButton_53, self.pushButton_54,self.pushButton_55, self.pushButton_56, self.pushButton_57, self.pushButton_58, self.pushButton_59,self.pushButton_510, self.pushButton_511],
                      [self.pushButton_60, self.pushButton_61, self.pushButton_62, self.pushButton_63, self.pushButton_64,self.pushButton_65, self.pushButton_66, self.pushButton_67, self.pushButton_68, self.pushButton_69,self.pushButton_610, self.pushButton_611],
                      [self.pushButton_70, self.pushButton_71, self.pushButton_72, self.pushButton_73, self.pushButton_74,self.pushButton_75, self.pushButton_76, self.pushButton_77, self.pushButton_78, self.pushButton_79,self.pushButton_710, self.pushButton_711],
                      [self.pushButton_80, self.pushButton_81, self.pushButton_82, self.pushButton_83, self.pushButton_84,self.pushButton_85, self.pushButton_86, self.pushButton_87, self.pushButton_88, self.pushButton_89,self.pushButton_810, self.pushButton_811],
                      [self.pushButton_90, self.pushButton_91, self.pushButton_92, self.pushButton_93, self.pushButton_94,self.pushButton_95, self.pushButton_96, self.pushButton_97, self.pushButton_98, self.pushButton_99,self.pushButton_910, self.pushButton_911],
                      [self.pushButton_100, self.pushButton_101, self.pushButton_102, self.pushButton_103,self.pushButton_104, self.pushButton_105, self.pushButton_106, self.pushButton_107,self.pushButton_108, self.pushButton_109, self.pushButton_1010, self.pushButton_1011],
                      [self.pushButton_1100, self.pushButton_1111, self.pushButton_112, self.pushButton_113,self.pushButton_114, self.pushButton_115, self.pushButton_116, self.pushButton_117,self.pushButton_118, self.pushButton_119, self.pushButton_11110, self.pushButton_11111]]
        
        
        
        if not self.t1.isAlive():
            self.label_4.setText("Press Start")
            self.dis_act_all()
        """ WHAT TO SHOW """
        if self.n > 4:
            for i in range(self.n):
                for j in range(self.n):
                    self.blist[i][j].show()
        if self.n>=10:    # If Board is big, make it full screen
            Formiki.showFullScreen()


        # if self.t1.isAlive():
        #         self.pushButton_4.setEnabled(False)
        # else:
        #         self.pushButton_4.setEnabled(True)

    """ BUTTON FUNCTIONS """

    def brokeiki(self):
        sender = self.Formiki.sender()
        if sender.text() == "Exit":
            self.Formiki.close()
        sender = self.Formiki.sender()
        if sender.text() == "Start":
            #self.t1 = Thread(target=self.countdown, args=(self.ctd,))
            
            self.dis_act_all(active=True)
            self.all_default_col()
            # self.lcdNumber.display(formatSec(self.countdown(180)))
            self.t1.start()
            self.pushButton_4.setText("Rest.")
            self.pushButton_4.setStyleSheet(self.darkblue)
        if sender.text() == "Rest.":
            if self.t1.isAlive():
                pass
            else:
                self.chain = []
                self.w= ""
                self.wordlist =[]
                self.lcdNumber_2.display(0)
                self.lcdNumber_3.display(0)
                self.label_4.setText('')
                self.all_uncheck()
                self.cleartable()
                self.dis_act_all(active=True)
                self.all_default_col()
                self.AItextEdit_2.setText("")
                self.t1 = Thread(target=self.countdown, args=(self.ctd,))
                #self.t1.start()
                self.pushButton_4.setText("Start")
                self.pushButton_4.setStyleSheet(" color: #303030;\n"
                                                "\n"
                                                "background: #00b894 ;\n"
                                                "border: 2px solid #303030;\n"
                                                "    border-radius: 20px;\n"
                                                "    border-style: outset;\n"
                                                "\n"
                                                "Text-align:center")
        if sender.text() == "Stop":
            #stop t1
            pass

            
            
    
    
    
    def cleartable(self):
        if not self.t1.isAlive():
            pass
        else:
            for j in self.blist:
                for k in j:
                    k.setEnabled(True)
            for i in self.chain:
                self.blist[i[0]][i[1]].setStyleSheet(self.defa)
                self.blist[i[0]][i[1]].setChecked(False)
            self.w = ""
            self.label_4.setText(self.w)
            self.chain = []
        

            
    

    def vstimesingle(self, pressed):
        
        source = self.Formiki.sender()

        if pressed:
            self.label_4.setText("")
            QtWidgets.qApp.processEvents()
            pos = i_list(source, self.blist)
            self.chain.append(pos)    # Add position to the chain as tuple
            for i in self.chain:
                 self.blist[i[0]][i[1]].setStyleSheet(self.blue)
            self.w += source.text()   # Expand the word with the new letter
            self.label_4.setText(self.w)  # show the word on line edit
            for j in self.blist:
                for k in j:
                    k.setEnabled(True)
            for i in self.chain[:-1]:
                self.blist[i[0]][i[1]].setEnabled(False)
                

            """ NEIGHBOR OR NOT SITUATION """
            #if len(self.chain) ==1:

            if len(self.chain) > 1:
                last = self.chain[-2]
                hood = self.hoodie(last)
                
                if pos not in hood:
                    for i in self.chain[0:(len(self.chain) - 1)]:
                        QtWidgets.qApp.processEvents()
                        self.blist[i[0]][i[1]].setStyleSheet(self.defa)
                        self.blist[i[0]][i[1]].setChecked(False)
                        self.blist[i[0]][i[1]].setEnabled(True)
                    self.chain = self.chain[-1:]  # Chain will be reduced to the last element
                    self.label_4.setText(self.w[-1])  # Line edit will be reduced to last letter
                    self.w = self.w[-1]  # The word will be reduced to last letter

            """ VALID WORD SITUATION """
            if len(self.w) >= 3 and self.w in self.words.list:
                
                # Repetition prevention # self.chain in self.paths or
                if self.w in self.wordlist:
                    for i in self.chain:
                        self.blist[i[0]][i[1]].setStyleSheet(self.red)
                    self.label_4.setText("Already in the list!")
                else:
                    self.wordlist.append(self.w)
                    # for i in self.wordlist:
                    self.AItextEdit_2.append(self.w)
                    self.paths.append(self.chain)
                    
                    for i in self.chain:
                        self.blist[i[0]][i[1]].setStyleSheet(self.green)
                    points = 0
                    polist = list(self.wordlist)
                    
                    # Points
                    for po in polist:
                            if len(po) <= 4:
                                    points += 1
                            elif len(po) == 5:
                                    points += 2
                            elif len(po) == 6:
                                    points += 3
                            elif len(po) == 7:
                                    points += 5
                            elif len(po) > 7:
                                    points += 11
                    self.lcdNumber_3.display(points)
                    self.lcdNumber_2.display(len(self.wordlist))


        else:
            QtWidgets.qApp.processEvents()
            source.setStyleSheet(self.defa)

            """ DESELECTION SITUATION """
            self.w = self.w[:-1]
            self.chain = self.chain[:-1]
            self.label_4.setText(self.w)
            for j in self.blist:
                for k in j:
                    k.setEnabled(True)
            for i in self.chain[:-1]:
                self.blist[i[0]][i[1]].setEnabled(False)

    def textToClick(self):

        if not self.dfsed:
            for i in range(self.n):
                for j in range(self.n):
                    startChar = self.board.letters[i][j]
                    temp = copy.deepcopy(self.board.letters)
                    temp[i][j] = '-'
                    Board.dfs(self.board, temp, self.trie, (i,j), startChar, False, None, False, None, [(i,j)], delay=0)
            self.dfsed = True

        txt = self.lineEdit.text()
        self.w = txt
        blinklist = []
        hood = []
        self.label_4.setText(txt)

        for i in self.blist:
            for j in i:
                j.setStyleSheet(self.defa)
            #reset board
        if txt != '':
            if txt in self.board.words:
                # Repetition prevention # self.chain in self.paths or
                if txt in self.wordlist:
                    for i in foundWordlist(txt, self.board.letters):
                        if i != None:
                            for j in i:
                                for k in j:
                                    x, y = k
                                    self.blist[x][y].setStyleSheet(self.red)
                                    self.chain.append((x,y))
                    self.label_4.setText("Already in the list!")
                else:
                    self.wordlist.append(txt)
                    self.AItextEdit_2.append(txt)
                    
                    for i in foundWordlist(txt, self.board.letters):
                        if i != None:
                            for j in i:
                                for k in j:
                                    x, y = k
                                    self.blist[x][y].setStyleSheet(self.green)
                                    self.chain.append((x,y))
                    points = 0
                    polist = list(self.wordlist)
                    
                    # Points
                    for po in polist:
                            if len(po) <= 4:
                                    points += 1
                            elif len(po) == 5:
                                    points += 2
                            elif len(po) == 6:
                                    points += 3
                            elif len(po) == 7:
                                    points += 5
                            elif len(po) > 7:
                                    points += 11
                    self.lcdNumber_3.display(points)
                    self.lcdNumber_2.display(len(self.wordlist))
            else:
                for i in foundWordlist(txt, self.board.letters):
                    if i != None:
                        for j in i:
                            for k in j:
                                x, y = k
                                self.blist[x][y].setStyleSheet(self.blue)
                                self.chain.append((x,y))





    def cheat(self):
        if self.chain == []:
            return
        self.stop = False
        temp = copy.deepcopy(self.board.letters)
        for k in self.chain:
            i, j = k
            temp[i][j] = '-'
        Board.dfs(self.board, temp, self.trie, self.chain[len(self.chain) - 1], self.w, False, None, True, self, [(i,j)], delay=0)
        for i in self.chain:
                 self.blist[i[0]][i[1]].setStyleSheet(self.blue)

    def vstimestart(self):
        self.stop = False
        for i in range(self.n):
                for j in range(self.n):
                    startChar = self.board.letters[i][j]
                    temp = copy.deepcopy(self.board.letters)
                    temp[i][j] = '-'
                    Board.dfs(self.board, temp, self.trie, (i,j), startChar, False, None, True, self, [(i,j)], delay=0)

        self.board.words.sort()
        self.AItextEdit_2.clear()
        for i in self.board.words:
            self.AItextEdit_2.append(i)
        
    
    """ SUPLEMENTARY METHODS """

    def countdown(self, nsec):
        self.sec = nsec
        for x in range(nsec, -1, -1):
            QtWidgets.qApp.processEvents()
            time.sleep(1)
            self.lcdNumber.display(x)
        self.sec = x
        self.dis_act_all()
            

    def hoodie(self, last):
        hood = []
        for i in self.directions:
            QtWidgets.qApp.processEvents()
            candi = tuple(map(add, i, last))
            if self.n > candi[0] >= 0 and self.n > candi[1] >= 0:
                hood.append(candi)
        return hood
    
    def dis_act_all(self, active = False):
        if active == True:
            for i in range(self.n ):
                for j in range(self.n ):
                    self.blist[i][j].setEnabled(True)
                    
        else:
            for i in range(self.n):
                for j in range(self.n):
                    self.blist[i][j].setEnabled(False)
    
    def all_default_col(self):
        for i in range(self.n ):
            for j in range(self.n ):
                self.blist[i][j].setStyleSheet(self.defa)
    def all_uncheck(self):
        for i in range(self.n ):
            for j in range(self.n ):
                self.blist[i][j].setChecked(False)
    



    






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Formiki = QtWidgets.QWidget()
    ui = Ui_Formiki(Formiki)
    ui.setupUi(Formiki)
    Formiki.show()
    sys.exit(app.exec_())