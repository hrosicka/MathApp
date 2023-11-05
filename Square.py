import sys
from random import randint

from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from PyQt5 import QtCore
from PyQt5.QtGui import QFont

import matplotlib
matplotlib.use('Qt5Agg')


from matplotlib import pyplot as plt

import numpy as np

import SquareCalc

import Canvas


class WindowSquare(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        sc = Canvas.MplCanvas(self, width=6, height=6, dpi=100)

        buttonplotSquare = QPushButton('Plot Square')
        buttonplotSquare.clicked.connect(lambda: self.plot_square(sc, self.combo_color.currentText()))
        buttonClose = QPushButton('Close')
        buttonClose.clicked.connect(self.close)

        self.setFixedSize(800, 365)

        hbox1 = QHBoxLayout()
        
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(buttonplotSquare)
        hbox2.addWidget(buttonClose)



        vbox1 = QVBoxLayout()

        vbox2 = QVBoxLayout()

        layout_param = QGridLayout()
        layout_res = QGridLayout()


        groupBoxParameters = QGroupBox("Parameters")
        groupBoxParameters.setLayout(layout_param)
        groupBoxResults = QGroupBox("Results")
        groupBoxResults.setLayout(layout_res)
        vbox1.addWidget(groupBoxParameters)
        vbox1.addWidget(groupBoxResults)

        hbox1.addLayout(vbox1)
        hbox1.addWidget(sc)

        vbox2.addLayout(hbox1)
        vbox2.addStretch(1)
        vbox2.addLayout(hbox2)

        self.setLayout(vbox2)
        self.setWindowTitle('Square')  

        

        self.label_side = QLabel("Side Length:")
        self.label_side.setAlignment(QtCore.Qt.AlignLeft)
        self.label_side.setFixedWidth(150)
        layout_param.addWidget(self.label_side,0,0)

        self.edit_side = QLineEdit(self)
        self.edit_side.setAlignment(QtCore.Qt.AlignRight)
        self.edit_side.setFixedWidth(150)
        layout_param.addWidget(self.edit_side,0,1)

        self.label_dim_side = QLabel("cm")
        self.label_dim_side.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_side.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_side,0,2)


        self.label_centerX = QLabel("Center - X coord.:")
        self.label_centerX.setAlignment(QtCore.Qt.AlignLeft)
        self.label_centerX.setFixedWidth(150)
        layout_param.addWidget(self.label_centerX,1,0)

        self.edit_centerX = QLineEdit(self)
        self.edit_centerX.setAlignment(QtCore.Qt.AlignRight)
        self.edit_centerX.setFixedWidth(150)
        layout_param.addWidget(self.edit_centerX,1,1)

        self.label_dim_x = QLabel("cm")
        self.label_dim_x.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_x.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_x,1,2)

        self.label_centerY = QLabel("Center - Y coord.:")
        self.label_centerY.setAlignment(QtCore.Qt.AlignLeft)
        self.label_centerY.setFixedWidth(150)
        layout_param.addWidget(self.label_centerY,2,0)

        self.edit_centerY = QLineEdit(self)
        self.edit_centerY.setAlignment(QtCore.Qt.AlignRight)
        self.edit_centerY.setFixedWidth(150)
        layout_param.addWidget(self.edit_centerY,2,1)

        self.label_dim_y = QLabel("cm")
        self.label_dim_y.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_y.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_y,2,2)


        self.label_combo_color = QLabel("Square Color:")
        self.label_combo_color.setAlignment(QtCore.Qt.AlignLeft)
        self.label_combo_color.setFixedWidth(150)
        layout_param.addWidget(self.label_combo_color,3,0)


        self.combo_color = QComboBox(self)
        self.combo_color.addItem("green")
        self.combo_color.addItem("red")
        self.combo_color.addItem("blue")
        self.combo_color.addItem("orange")
        self.combo_color.setFixedWidth(150)
        layout_param.addWidget(self.combo_color,3,1)
        

        self.label_perimeter = QLabel("Square Perimeter:")
        self.label_perimeter.setAlignment(QtCore.Qt.AlignLeft)
        self.label_perimeter.setFixedWidth(150)
        layout_res.addWidget(self.label_perimeter,0,0)

        self.label_res_perimeter = QLabel('0.0')
        self.label_res_perimeter.setStyleSheet("background-color : white; color : darkblue")
        self.label_res_perimeter.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_perimeter.setFixedWidth(150)
        layout_res.addWidget(self.label_res_perimeter,0,1)

        self.label_dim_per = QLabel("cm")
        self.label_dim_per.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_per.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_per,0,2)


        self.label_area = QLabel("Square Area:")
        self.label_area.setAlignment(QtCore.Qt.AlignLeft)
        self.label_area.setFixedWidth(150)
        layout_res.addWidget(self.label_area,1,0)

        self.label_res_area = QLabel('0.0')
        # self.label_res_area.setFont(QFont('Arial', 12))
        self.label_res_area.setStyleSheet("background-color : white; color : darkblue")
        self.label_res_area.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_area.setFixedWidth(150)
        layout_res.addWidget(self.label_res_area,1,1)

        self.label_dim_area = QLabel("cm<sup>2</sup>")
        self.label_dim_area.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_area.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_area,1,2)



    def plot_square(self, square_plot, square_color):
        square_plot.axes.cla()
        Drawing_colored_circle = plt.Circle((float(self.edit_centerX.text()),(float(self.edit_centerY.text()))),float(self.edit_side.text()))
        Drawing_colored_circle.set_color(square_color)

        minus_x = float(self.edit_centerX.text())-2*float(self.edit_side.text())
        plus_x = float(self.edit_centerX.text())+2*float(self.edit_side.text())
        minus_y = float(self.edit_centerY.text())-2*float(self.edit_side.text())
        plus_y = float(self.edit_centerY.text())+2*float(self.edit_side.text())

        square_plot.axes.set_xlim(minus_x, plus_x)
        square_plot.axes.set_ylim(minus_y, plus_y)

        square_plot.axes.add_artist(Drawing_colored_circle)
        square_plot.draw()

        self.calculate_square()

    def calculate_square(self):

        side_square = float(self.edit_side.text())
        mySquare = SquareCalc.Ctverec(side_square)
        square_perimeter = round(mySquare.obvod(),5)
        square_area = round(mySquare.obsah(),5)

        self.label_res_perimeter.setText(str(square_perimeter))
        self.label_res_area.setText(str(square_area))

        


        