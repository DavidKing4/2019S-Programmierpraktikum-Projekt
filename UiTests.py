from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
dlg = uic.loadUi("Mode1.ui")




# dlg.lineEdit.setPlaceholderText("Placeholder")
# dlg.lineEdit.setFocus()    # Automatically initializes this lineedit
# # dlg.lineEdit.returnPressed.connect()    # When "Enter" pressed, initialize...
#
# dlg.pushButton.clicked.connect(start)
#
# def start():


dlg.show()
app.exec()