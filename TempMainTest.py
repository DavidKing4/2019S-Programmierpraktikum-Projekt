# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainTest.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 360)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background: #f2f1ef")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(300, 100))
        self.label.setMaximumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet(" color: #303030;\n"
"\n"
"background: #e87461 ;\n"
"border: 2px solid #303030;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.SolverRadio = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.SolverRadio.setFont(font)
        self.SolverRadio.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.SolverRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.SolverRadio.setStyleSheet("")
        self.SolverRadio.setObjectName("SolverRadio")
        self.verticalLayout.addWidget(self.SolverRadio)
        self.VsCompRadio = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.VsCompRadio.setFont(font)
        self.VsCompRadio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.VsCompRadio.setAutoFillBackground(False)
        self.VsCompRadio.setStyleSheet(" color: #303030;\n"
"\n"
"background:#f2f1ef ;\n"
"\n"
"border: ;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"\n"
"Text-align:center")
        self.VsCompRadio.setObjectName("VsCompRadio")
        self.verticalLayout.addWidget(self.VsCompRadio)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_5.addWidget(self.line)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_4.addWidget(self.checkBox)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
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
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setStyleSheet("")
        self.horizontalSlider.setMinimum(4)
        self.horizontalSlider.setMaximum(12)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_5.setStyleSheet(" color: #303030;\n"
"\n"
"background:#f2f1ef ;\n"
"\n"
"border: 2px solid #303030;\n"
"   \n"
"\n"
"Text-align:center")
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.horizontalLayout_2.addWidget(self.lcdNumber_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(10)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayout_3.addWidget(self.horizontalSlider_2)
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_6.setStyleSheet(" color: #303030;\n"
"\n"
"background:#f2f1ef ;\n"
"\n"
"border: 2px solid #303030;\n"
"   \n"
"Text-align:center")
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.horizontalLayout_3.addWidget(self.lcdNumber_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(70, 28))
        self.pushButton_3.setMaximumSize(QtCore.QSize(75, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(14)
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
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(70, 28))
        self.pushButton_2.setMaximumSize(QtCore.QSize(75, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(14)
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
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(3)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(70, 28))
        self.pushButton_4.setMaximumSize(QtCore.QSize(75, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(14)
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
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(70, 28))
        self.pushButton.setMaximumSize(QtCore.QSize(75, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(14)
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
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBegin = QtWidgets.QAction(MainWindow)
        self.actionBegin.setObjectName("actionBegin")
        self.actionGame_Manual = QtWidgets.QAction(MainWindow)
        self.actionGame_Manual.setObjectName("actionGame_Manual")
        self.actionHigh_Scores = QtWidgets.QAction(MainWindow)
        self.actionHigh_Scores.setObjectName("actionHigh_Scores")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionBegin)
        self.menuFile.addAction(self.actionGame_Manual)
        self.menuFile.addAction(self.actionHigh_Scores)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.horizontalSlider.sliderMoved['int'].connect(self.lcdNumber_5.display)
        self.horizontalSlider_2.sliderMoved['int'].connect(self.lcdNumber_6.display)
        self.checkBox.clicked['bool'].connect(self.lineEdit.setEnabled)
        self.actionGame_Manual.triggered.connect(self.pushButton_2.click)
        self.actionBegin.triggered.connect(self.pushButton_4.click)
        self.actionHigh_Scores.triggered.connect(self.pushButton_3.click)
        self.actionQuit.triggered.connect(self.pushButton.click)
        self.checkBox.clicked['bool'].connect(self.lineEdit.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Boggle"))
        self.SolverRadio.setText(_translate("MainWindow", "Solver         "))
        self.VsCompRadio.setText(_translate("MainWindow", "Time Trial  "))
        self.checkBox.setText(_translate("MainWindow", "Custom Board"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Ex: abcdefghjklmnopr"))
        self.label_2.setText(_translate("MainWindow", "Board size  "))
        self.label_4.setText(_translate("MainWindow", "Com. Speed"))
        self.pushButton_3.setText(_translate("MainWindow", "Scores"))
        self.pushButton_2.setText(_translate("MainWindow", "Manual"))
        self.label_3.setText(_translate("MainWindow", "Play Time"))
        self.pushButton_4.setText(_translate("MainWindow", "Begin"))
        self.pushButton.setText(_translate("MainWindow", "Quit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionBegin.setText(_translate("MainWindow", "Begin"))
        self.actionGame_Manual.setText(_translate("MainWindow", "Game Manual"))
        self.actionHigh_Scores.setText(_translate("MainWindow", "High Scores"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
