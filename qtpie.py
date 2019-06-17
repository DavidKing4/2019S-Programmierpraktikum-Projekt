import PyQt5 as qt
import Board
import Words
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QTextEdit, QLabel, QRadioButton, QCheckBox, QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys
import os


class Boggle(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        """ Labels and Buttons"""
        self.b = QtWidgets.QPushButton("Push me!")
        self.b1 = QtWidgets.QPushButton('Clear')
        self.b2 = QtWidgets.QPushButton('Print')
        self.b3 = QtWidgets.QPushButton('b3')

        self.l = QtWidgets.QLabel("Welcome to our Boggle application")

        # user input
        self.le = QtWidgets.QLineEdit()

        # slider
        self.sl = QSlider(Qt.Vertical)
        self.sl.setMinimum(4)
        self.sl.setMaximum(12)
        self.sl.setValue(4)
        self.sl.setTickInterval(2)
        self.sl.setTickPosition(QSlider.TicksBelow)

        # Checkbox
        self.chx = QCheckBox("What's good?")

        # Radio Button
        self.lbl = QLabel('Choose a Grid:')
        self.g4x4 = QRadioButton('4x4')
        self.g6x6 = QRadioButton('6x6')
        self.g8x8 = QRadioButton('8x8')



        """
        # Board
        self.board = Board.Board()

        # Grid?
        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.board.letters[0][0])

        """


        """Layout Adjustments"""

        # A horizontal one
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.l)
        h_box.addStretch()

        # A vertical one
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)
        v_box.addWidget(self.b3)
        v_box.addWidget(self.sl)
        v_box.addLayout(h_box)
        v_box.addWidget(self.chx)

        v_box.addWidget(self.lbl)
        v_box.addWidget(self.g4x4)
        v_box.addWidget(self.g6x6)
        v_box.addWidget(self.g8x8)

        #layout = QVBoxLayout()
        #layout.addWidget(self.chx)

        # Add Layout
        self.setLayout(v_box)
        # Add master tittle
        self.setWindowTitle('BOGGLE')

        # Button-function connections
        self.b.clicked.connect(self.btn_click)
        self.b1.clicked.connect(lambda: self.bc1('All Cleared'))
        self.b2.clicked.connect(lambda: self.bc1('All Printed'))
        self.b3.clicked.connect(lambda: self.bc1('Hi man, wats up'))
        self.b.clicked.connect(lambda: self.check(self.chx.isChecked(), self.l))
        self.b.clicked.connect(lambda: self.rad(self.g4x4.isChecked(), self.g6x6.isChecked(), self.g8x8.isChecked(), self.lbl))




        self.sl.valueChanged.connect(self.v_change)
        self.show()

    # Button Functions
    def btn_click(self):
        board = Board.Board()
        self.l.setText(board.spcPrint())

    def bc1(self, string):
        sender = self.sender()
        if sender.text() == 'Print':
            print(self.le.text())
        elif sender.text() == 'Clear':
            self.le.clear()
        elif sender.text() == 'b3':
            pass
        print(string)

    def bc2(self, b, string):
        pass

    def check(self, chk, l):
        if chk:
            l.setText('Nice.')
        else:
            l.setText("Who's messing with your vibes?")


    def v_change(self):
        my_value = str(self.sl.value())
        self.le.setText(my_value)

    def rad(self, four, six, eight, lbl):
        if four:
            lbl.setText('4x4')
        elif six:
            lbl.setText('6x6')
        elif eight:
            lbl.setText('8x8')



app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')     # ['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
palette = QPalette()
#palette.setColor(QPalette.Background, Qt.blue)
app.setStyleSheet("QPushButton { margin: 1ex; }")
app.setPalette(palette)
a_window = Boggle()
sys.exit(app.exec_())
