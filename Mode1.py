from Board import *
from Words import Words
import sys
import time
import threading


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 515)
        Form.setStyleSheet("background: #f2f1ef")
        self.form = Form
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # Start
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setMaximumSize(QtCore.QSize(70, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(" color: #303030;\n"
                                        "\n"
                                        "background: #00b894 ;\n"
                                        "border: 2px solid #303030;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "\n"
                                        "Text-align:center")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 4, 1, 1)

        # Stop
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setMaximumSize(QtCore.QSize(70, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(" color: #303030;\n"
                                        "\n"
                                        "background: #fdcb6e ;\n"
                                        "border: 2px solid #303030;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "\n"
                                        "Text-align:center")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 5, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Form)
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
        self.gridLayout_2.addWidget(self.lcdNumber_2, 2, 1, 1, 1)

        # Exit
        self.pushButton = QtWidgets.QPushButton(Form)
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
        self.gridLayout_2.addWidget(self.pushButton, 2, 6, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(121, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
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
        self.gridLayout_2.addWidget(self.lcdNumber, 1, 6, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("\n"
                                       "QProgressBar {\n"
                                       "    border: 2px solid grey;\n"
                                       "    border-radius: 5px;\n"
                                       "    border-color: #303030\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "QProgressBar::chunk {\n"
                                       "    background-color: #05B8CC;\n"
                                       "    width: 20px;\n"
                                       "}\n"
                                       ";\n"
                                       "Text-align:center\n"
                                       "")
        self.progressBar.setProperty("value", 00)
        self.progressBar.setObjectName("progressBar")

        # GRID
        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 6)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_00 = QtWidgets.QPushButton(Form)
        self.pushButton_00.setEnabled(True)
        self.pushButton_00.setMinimumSize(QtCore.QSize(100, 100))
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
        self.pushButton_03 = QtWidgets.QPushButton(Form)
        self.pushButton_03.setEnabled(True)
        self.pushButton_03.setMinimumSize(QtCore.QSize(100, 100))
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
        self.pushButton_01 = QtWidgets.QPushButton(Form)
        self.pushButton_01.setEnabled(True)
        self.pushButton_01.setMinimumSize(QtCore.QSize(100, 100))
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
        self.pushButton_02 = QtWidgets.QPushButton(Form)
        self.pushButton_02.setEnabled(True)
        self.pushButton_02.setMinimumSize(QtCore.QSize(100, 100))
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
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setEnabled(True)
        self.pushButton_11.setMinimumSize(QtCore.QSize(100, 100))
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
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setMinimumSize(QtCore.QSize(100, 100))
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
        self.pushButton_20 = QtWidgets.QPushButton(Form)
        self.pushButton_20.setEnabled(True)
        self.pushButton_20.setMinimumSize(QtCore.QSize(100, 100))
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
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setEnabled(True)
        self.pushButton_12.setMinimumSize(QtCore.QSize(100, 100))
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
        self.pushButton_13 = QtWidgets.QPushButton(Form)
        self.pushButton_13.setEnabled(True)
        self.pushButton_13.setMinimumSize(QtCore.QSize(100, 100))
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
        self.pushButton_21 = QtWidgets.QPushButton(Form)
        self.pushButton_21.setEnabled(True)
        self.pushButton_21.setMinimumSize(QtCore.QSize(100, 100))
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
        self.pushButton_22 = QtWidgets.QPushButton(Form)
        self.pushButton_22.setEnabled(True)
        self.pushButton_22.setMinimumSize(QtCore.QSize(100, 100))
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
        self.pushButton_23 = QtWidgets.QPushButton(Form)
        self.pushButton_23.setEnabled(True)
        self.pushButton_23.setMinimumSize(QtCore.QSize(100, 100))
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
        self.pushButton_31 = QtWidgets.QPushButton(Form)
        self.pushButton_31.setEnabled(True)
        self.pushButton_31.setMinimumSize(QtCore.QSize(100, 100))
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
        self.pushButton_32 = QtWidgets.QPushButton(Form)
        self.pushButton_32.setEnabled(True)
        self.pushButton_32.setMinimumSize(QtCore.QSize(100, 100))
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
        self.pushButton_33 = QtWidgets.QPushButton(Form)
        self.pushButton_33.setEnabled(True)
        self.pushButton_33.setMinimumSize(QtCore.QSize(100, 100))
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
        self.pushButton_30 = QtWidgets.QPushButton(Form)
        self.pushButton_30.setEnabled(True)
        self.pushButton_30.setMinimumSize(QtCore.QSize(100, 100))
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
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 5)
        self.textEdit = QtWidgets.QTextEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(" color: #303030;\n"
                                        "\n"
                                        "background:#f2f1ef ;\n"
                                        "\n"
                                        "border: 2px solid #303030;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "\n"
                                        "Text-align:center")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 5, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMaximumSize(QtCore.QSize(121, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 2, 1, 1)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(Form)
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
        self.gridLayout_2.addWidget(self.lcdNumber_3, 2, 3, 1, 1)



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    """ BOARD SETTINGS """

    def __init__(self, board=None, size=4, trie=None, words=None):
        """ Board """
        if board == None:
            self.board = Board()
        if words == None:
            self.words = Words()
        if trie == None:
            self.trie = self.words.trie()
        self.wordList = []



    def retranslateUi(self, Form):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Exit"))
        self.pushButton_2.setText(_translate("Form", "Stop"))
        self.pushButton_3.setText(_translate("Form", "Start"))

        self.label.setText(_translate("Form", "Found Words:"))
        self.label_2.setText(_translate("Form", "Total Points"))

        self.pushButton_13.setText(_translate("MainWindow", self.board.letters[1][3]))
        self.pushButton_20.setText(_translate("MainWindow", self.board.letters[2][0]))
        self.pushButton_01.setText(_translate("MainWindow", self.board.letters[0][1]))
        self.pushButton_00.setText(_translate("MainWindow", self.board.letters[0][0]))
        self.pushButton_03.setText(_translate("MainWindow", self.board.letters[0][3]))
        self.pushButton_02.setText(_translate("MainWindow", self.board.letters[0][2]))
        self.pushButton_11.setText(_translate("MainWindow", self.board.letters[1][1]))
        self.pushButton_10.setText(_translate("MainWindow", self.board.letters[1][0]))
        self.pushButton_12.setText(_translate("MainWindow", self.board.letters[1][2]))
        self.pushButton_22.setText(_translate("MainWindow", self.board.letters[2][2]))
        self.pushButton_23.setText(_translate("MainWindow", self.board.letters[2][3]))
        self.pushButton_31.setText(_translate("MainWindow", self.board.letters[3][1]))
        self.pushButton_30.setText(_translate("MainWindow", self.board.letters[3][0]))
        self.pushButton_21.setText(_translate("MainWindow", self.board.letters[2][1]))
        self.pushButton_32.setText(_translate("MainWindow", self.board.letters[3][2]))
        self.pushButton_33.setText(_translate("MainWindow", self.board.letters[3][3]))

        """ BUTTON-FUNCTION CONNECTIONS """
        self.pushButton_3.clicked.connect(lambda: self.dfsguiprep())
        self.pushButton_13.clicked.connect(lambda: self.dfsguisingle((1, 3)))
        self.pushButton_00.clicked.connect(lambda: self.dfsguisingle((0, 0)))
        self.pushButton_01.clicked.connect(lambda: self.dfsguisingle((0, 1)))
        self.pushButton_02.clicked.connect(lambda: self.dfsguisingle((0, 2)))
        self.pushButton_03.clicked.connect(lambda: self.dfsguisingle((0, 3)))
        self.pushButton_10.clicked.connect(lambda: self.dfsguisingle((1, 0)))
        self.pushButton_11.clicked.connect(lambda: self.dfsguisingle((1, 1)))
        self.pushButton_12.clicked.connect(lambda: self.dfsguisingle((1, 2)))
        self.pushButton_20.clicked.connect(lambda: self.dfsguisingle((2, 0)))
        self.pushButton_21.clicked.connect(lambda: self.dfsguisingle((2, 1)))
        self.pushButton_22.clicked.connect(lambda: self.dfsguisingle((2, 2)))
        self.pushButton_23.clicked.connect(lambda: self.dfsguisingle((2, 3)))
        self.pushButton_30.clicked.connect(lambda: self.dfsguisingle((3, 0)))
        self.pushButton_31.clicked.connect(lambda: self.dfsguisingle((3, 1)))
        self.pushButton_32.clicked.connect(lambda: self.dfsguisingle((3, 2)))
        self.pushButton_33.clicked.connect(lambda: self.dfsguisingle((3, 3)))

        # Break Buttons
        self.process = QtCore.QProcess()
        self.pushButton.clicked.connect(self.broke)
        self.pushButton_2.clicked.connect(self.broke)


        """ Button List """
        self.blist = [[self.pushButton_00, self.pushButton_01, self.pushButton_02, self.pushButton_03],
                      [self.pushButton_10, self.pushButton_11, self.pushButton_12, self.pushButton_13],
                      [self.pushButton_20, self.pushButton_21, self.pushButton_22, self.pushButton_23],
                      [self.pushButton_30, self.pushButton_31, self.pushButton_32, self.pushButton_33]]

        # """ Timer """
        # self.timer = QtCore.QTimer(self)
        # self.timer.timeout.connect(self.Time)
        #
        # self.start = QtGui.QPushButton("Start", self)
        # self.start.clicked.connect(self.Start)
        #
        # self.stop = QtGui.QPushButton("Stop", self)
        # self.stop.clicked.connect(lambda: self.timer.stop())
        #
        # self.reset = QtGui.QPushButton("Reset", self)
        # self.reset.clicked.connect(self.Reset)



    """ BUTTON FUNCTIONS """

    def swatch(self):
        now = time.time()
        self.lcdNumber.display(time.time()-now)

    # Break functions
    def broke(self):
        sender = self.form.sender()
        if sender.text() == "Exit":
            self.form.close()
        elif sender.text() == "Stop":

            QtWidgets.qApp.processEvents()



    def dfsguisingle(self, bs, delay = 0):
        self.board.words = []    # Whenever you press start the list and points will be resetted
        self.textEdit.clear()    # Text edit must be cleared

        stringTrie = self.trie
        startChar = self.board.letters[bs[0]][bs[1]]
        temp = copy.deepcopy(self.board.letters)
        temp[bs[0]][bs[1]] = '-'

        Board.dfs(self.board, temp, stringTrie, (bs[0], bs[1]), startChar, False, None, True, self, [(bs[0], bs[1])])
        points = 0
        polist = list(self.board.words)
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
        self.lcdNumber_2.display(len(self.board.words))


    def dfsguiprep(self):
        count = 0
        limit = 100
        n = 4
        self.board.words = []    # Whenever you press start the list and points will be resetted
        self.textEdit.clear()    # clear Textedit


        now = time.time()
        # t = threading.Thread(target= self.swatch, name='th1')
        # t.start()



        stringTrie = self.trie
        for i in range(n):
            for j in range(n):
                self.lcdNumber.display(round(time.time()-now,2))
                QtWidgets.qApp.processEvents()
                startChar = self.board.letters[i][j]
                temp = copy.deepcopy(self.board.letters)
                temp[i][j] = '-'

                Board.dfs(self.board, temp, stringTrie, (i,j), startChar, False, None, True, self, [(i,j)], delay=0)

                count += 100 / n**2
                self.progressBar.setValue(count)
                # self.lcdNumber.display(count)    # It must work as a timer

                points = 0
                polist = list(self.board.words)
                for po in polist:
                    if len(po)<= 4:
                        points+=1
                    elif len(po) == 5:
                        points+=2
                    elif len(po) == 6:
                        points+=3
                    elif len(po) == 7:
                        points+=5
                    elif len(po) > 7:
                        points += 11
                self.lcdNumber_3.display(points)
                self.lcdNumber_2.display(len(self.board.words))







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
