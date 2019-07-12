from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 515)
        Form.setStyleSheet("background: #f2f1ef")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
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
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 2, 1)
        self.AItextEdit_2 = QtWidgets.QTextEdit(Form)
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
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(150, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
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
        self.horizontalLayout_2.addWidget(self.lcdNumber_2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMaximumSize(QtCore.QSize(150, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
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
        self.horizontalLayout_2.addWidget(self.lcdNumber_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMaximumSize(QtCore.QSize(150, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
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
        self.pushButton_3 = QtWidgets.QPushButton(Form)
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
        self.pushButton_2 = QtWidgets.QPushButton(Form)
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
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
        self.pushButton_5 = QtWidgets.QPushButton(Form)
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
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton = QtWidgets.QPushButton(Form)
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter:"))
        self.pushButton_33.setText(_translate("Form", "a"))
        self.pushButton_30.setText(_translate("Form", "a"))
        self.pushButton_31.setText(_translate("Form", "a"))
        self.pushButton_32.setText(_translate("Form", "a"))
        self.pushButton_01.setText(_translate("Form", "a"))
        self.pushButton_20.setText(_translate("Form", "a"))
        self.pushButton_03.setText(_translate("Form", "a"))
        self.pushButton_10.setText(_translate("Form", "a"))
        self.pushButton_12.setText(_translate("Form", "a"))
        self.pushButton_11.setText(_translate("Form", "a"))
        self.pushButton_13.setText(_translate("Form", "a"))
        self.pushButton_21.setText(_translate("Form", "a"))
        self.pushButton_02.setText(_translate("Form", "a"))
        self.pushButton_22.setText(_translate("Form", "a"))
        self.pushButton_23.setText(_translate("Form", "a"))
        self.pushButton_00.setText(_translate("Form", "a"))
        self.label.setText(_translate("Form", "Found Words:"))
        self.label_2.setText(_translate("Form", "        Total Points:"))
        self.label_3.setText(_translate("Form", "Remaining Time:"))
        self.pushButton_3.setText(_translate("Form", "Solve"))
        self.pushButton_2.setText(_translate("Form", "Cheat"))
        self.pushButton_4.setText(_translate("Form", "Start"))
        self.pushButton_5.setText(_translate("Form", "Stop"))
        self.pushButton.setText(_translate("Form", "Exit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
