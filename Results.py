# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Results):
        Results.setObjectName("Results")
        Results.resize(480, 503)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.buttonBox = QtWidgets.QDialogButtonBox(Results)
        self.buttonBox.setGeometry(QtCore.QRect(10, 460, 450, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Results)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(15, 9, 450, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font)
        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font)
        self.gridLayout.addWidget(self.label_4, 2, 5, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Results)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(15, 59, 450, 391))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit_6 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setStyleSheet(" color: #303030;\n"
                                        "\n"
                                        "background:#f2f1ef ;\n"
                                        "\n"
                                        "border: 2px solid #303030;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "\n"
                                        "Text-align:center")
        for i in self.words5:
            self.textEdit_6.append(i)
        self.gridLayout_2.addWidget(self.textEdit_6, 1, 2, 1, 1)
        self.textEdit_3 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet(" color: #303030;\n"
                                        "\n"
                                        "background:#f2f1ef ;\n"
                                        "\n"
                                        "border: 2px solid #303030;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "\n"
                                        "Text-align:center")
        for i in self.words6:
            self.textEdit_3.append(i)
        self.gridLayout_2.addWidget(self.textEdit_3, 3, 0, 1, 1)
        self.textEdit_4 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setStyleSheet(" color: #303030;\n"
                                        "\n"
                                        "background:#f2f1ef ;\n"
                                        "\n"
                                        "border: 2px solid #303030;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "\n"
                                        "Text-align:center")
        for i in self.words3:
            self.textEdit_4.append(i)
        self.gridLayout_2.addWidget(self.textEdit_4, 1, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
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
        for i in self.words8:
            self.textEdit.append(i)
        self.gridLayout_2.addWidget(self.textEdit, 3, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet(" color: #303030;\n"
                                        "\n"
                                        "background:#f2f1ef ;\n"
                                        "\n"
                                        "border: 2px solid #303030;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "\n"
                                        "Text-align:center")
        for i in self.words7:
            self.textEdit_2.append(i)
        self.gridLayout_2.addWidget(self.textEdit_2, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(font)
        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)
        self.textEdit_5 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_5.setReadOnly(True)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setStyleSheet(" color: #303030;\n"
                                        "\n"
                                        "background:#f2f1ef ;\n"
                                        "\n"
                                        "border: 2px solid #303030;\n"
                                        "    border-radius: 20px;\n"
                                        "    border-style: outset;\n"
                                        "\n"
                                        "Text-align:center")
        for i in self.words4:
            self.textEdit_5.append(i)
        self.gridLayout_2.addWidget(self.textEdit_5, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font)
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(font)
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.label_9.setFont(font)
        self.gridLayout_2.addWidget(self.label_9, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.label_10.setFont(font)
        self.gridLayout_2.addWidget(self.label_10, 2, 2, 1, 1)

        self.retranslateUi(Results)
        self.buttonBox.accepted.connect(Results.accept)
        self.buttonBox.rejected.connect(Results.reject)
        QtCore.QMetaObject.connectSlotsByName(Results)

    def retranslateUi(self, Results):
        _translate = QtCore.QCoreApplication.translate
        Results.setWindowTitle(_translate("Results", "Results"))
        self.label.setText(_translate("Results", "<html><head/><body><p align=\"right\">Words Found:</p></body></html>"))
        self.label_3.setText(_translate("Results", "<html><head/><body><p align=\"right\">Points:</p></body></html>"))
        self.label_2.setText(_translate("Results", f"{self.noWords}"))
        self.label_4.setText(_translate("Results", f"{self.points}"))
        self.label_6.setText(_translate("Results", "4 letter words (1pt)"))
        self.label_7.setText(_translate("Results", "5 letter words (2pt)"))
        self.label_5.setText(_translate("Results", "3 letter words (1pt)"))
        self.label_8.setText(_translate("Results", "6 letter words (3pt)"))
        self.label_9.setText(_translate("Results", "7 letter words (5pts)"))
        self.label_10.setText(_translate("Results", "8+ letter words (11pt)"))

    def __init__(self, words = [], noWords = 0, points = 0):

        self.words3 = []
        self.words4 = []
        self.words5 = []
        self.words6 = []
        self.words7 = []
        self.words8 = []

        self.noWords = noWords
        self.points = points

        for i in words:
            if len(i) == 3:
                self.words3.append(i)
            elif len(i) == 4:
                self.words4.append(i)
            elif len(i) == 5:
                self.words5.append(i)
            elif len(i) == 6:
                self.words6.append(i)
            elif len(i) == 7:
                self.words7.append(i)
            elif len(i) == 8:
                self.words8.append(i)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Results = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
    ui = Ui_Dialog()
    ui.setupUi(Results)
    Results.show()
    sys.exit(app.exec_())

