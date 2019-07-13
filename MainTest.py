from Board import Board
from PyQt5 import QtCore, QtGui, QtWidgets
from NEWGUI import BOGGLE
from Mode1 import Ui_Form


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(628, 482)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 380, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(370, 220, 241, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(530, 330, 64, 23))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(260, 30, 137, 139))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 0, 0, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout.addWidget(self.lcdNumber_2, 0, 1, 1, 1)
        self.verticalSlider = QtWidgets.QSlider(self.widget)
        self.verticalSlider.setMinimum(4)
        self.verticalSlider.setMaximum(12)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout.addWidget(self.verticalSlider, 1, 0, 1, 1)
        self.verticalSlider_2 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_2.setMinimum(1)
        self.verticalSlider_2.setMaximum(10)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.gridLayout.addWidget(self.verticalSlider_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.verticalSlider.sliderMoved['int'].connect(self.lcdNumber.display)
        self.verticalSlider_2.sliderMoved['int'].connect(self.lcdNumber_2.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "start"))
        self.label.setText(_translate("MainWindow", "Grid"))
        self.label_2.setText(_translate("MainWindow", "Level"))




        """ UI BORDER -------------------------------------------------------------------"""
        self.Form = self.pushButton.clicked.connect(self.open)

    def open(self):
        dal = self.verticalSlider.sliderPosition()
        cuslist = self.lineEdit.text()
        culi = [str.lower() for str in cuslist]
        culi = culi[:dal**2]
        cusboard =[]

        for i in range(0, len(culi), dal):
            cusboard.append(culi[i:i+dal])

        global Form
        Form = QtWidgets.QWidget()
        ui = Ui_Form(board = Board(dal, False, cusboard), size = dal)
        #(self, board=None, size=6, trie=None, words=None):
        #self.ui.board = cusboard
        ui.setupUi(Form)
        Form.show()
        self.MainWindow.close()
        return(Form)
        #sys.exit(app.exec_())

        # app = QtWidgets.QApplication(sys.argv)
        # Form = QtWidgets.QWidget()
        # ui = Ui_Form()
        # ui.setupUi(Form)
        # Form.show()
        # sys.exit(app.exec_())

        # self.window = QtWidgets.QWidget()
        # self.ui = Ui_Form(size=dal, board=cusboard)
        # # self.ui.board.letters = cusboard
        # # self.ui.n = dal
        # self.ui.setupUi(self.window)
        # self.window.show()

        # if dal == 0:
        #
        #     # cus_board = [['d', 'k', 'z', 'l'],
        #     #              ['f', 'p', 'x', 'q'],
        #     #              ['n', 'b', 'g', 'e'],
        #     #              ['i', 'v', 'w', 's']]
        #     self.window = QtWidgets.QWidget()
        #     self.ui = Ui_Form()
        #     self.ui.board.letters = cus_board
        #     self.ui.setupUi(self.window)
        #     self.window.show()






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    print(type(Ui_MainWindow))
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())