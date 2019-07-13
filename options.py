# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Mode1 import Ui_Form
from Mode2 import Ui_Formiki
from Board import Board

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(370, 198)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-20, 161, 341, 21))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 19, 323, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.hide()
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.gridLayout.addLayout(self.formLayout, 5, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setRange(1,10)
        self.gridLayout.addWidget(self.spinBox_2, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 4, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setRange(4,10)
        self.gridLayout.addWidget(self.spinBox, 0, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.label_5.hide()
        self.gridLayout.addWidget(self.label_5, 5, 3, 1, 1, QtCore.Qt.AlignVCenter)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Mode:"))
        self.label_3.setText(_translate("Dialog", "Level:"))
        self.label_2.setText(_translate("Dialog", "Custom:"))
        self.label.setText(_translate("Dialog", "Size: "))
        self.radioButton.setText(_translate("Dialog", "Solver"))
        self.radioButton_2.setText(_translate("Dialog", "vs Com."))
        self.label_5.setText(_translate("Dialog", "(enter all letters as one string)"))

        self.checkBox.stateChanged.connect(lambda: self.updateCustom())
        self.buttonBox.accepted.connect(lambda: self.openMain())

    def updateCustom(self):
        if self.checkBox.isChecked():
            self.lineEdit.show()
            self.label_5.show()
        else:
            self.lineEdit.hide()
            self.label_5.hide()

    def openMain(self):

        Dialog.close()
        n = self.spinBox.value()

        if self.checkBox.isChecked():
            try:
                letters = [['' for i in range(n)] for j in range(n)]
                lRaw = self.lineEdit.text()
                index = 0
                for i in range(n):
                    for j in range(n):
                        letters[i][j] = lRaw[index]
                        index += 1
            except:
                print(f'Custom input should have {n**2} letters, entered as one string,')
                print('please try again.')
                sys.exit()

            b = Board(self.spinBox.value(), False, letters)
        else:
            b = None

        if self.radioButton.isChecked():
            global Form
            Form = QtWidgets.QWidget()
            ui = Ui_Form(board = b, size = n, trie = None, words = None)
            ui.setupUi(Form)
            Form.show()
        elif self.radioButton_2.isChecked():
            global Formiki
            Formiki = QtWidgets.QWidget()
            ui = Ui_Formiki(Formiki, board = b, size = n, trie = None, words = None)
            ui.setupUi(Formiki)
            Formiki.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())