import sys
from random import randint

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from PyQt5 import QtCore
from PyQt5.QtGui import QFont

import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

import numpy as np

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=6, height=6, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class WindowCircle(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        sc = MplCanvas(self, width=6, height=6, dpi=100)

        buttonplotCircle = QPushButton('Plot Circle')
        buttonplotCircle.clicked.connect(lambda: self.plot_circle(sc))
        buttonClose = QPushButton('Close')
        buttonClose.clicked.connect(self.close)


        self.setMinimumWidth(400)
        self.setMinimumHeight(400)

        self.setMaximumWidth(800)
        self.setMaximumHeight(800)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(buttonplotCircle)
        hbox.addWidget(buttonClose)
        vbox = QVBoxLayout()



        l3 = QGridLayout()
        groupBoxParameters = QGroupBox("Parameters")
        groupBoxParameters.setLayout(l3)
        vbox.addWidget(groupBoxParameters)
        vbox.addWidget(sc)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Circle')  

        

        self.label_radius = QLabel("Radius:")
        self.label_radius.setAlignment(QtCore.Qt.AlignLeft)
        l3.addWidget(self.label_radius,0,0)

        self.edit_radius = QLineEdit(self)
        self.edit_radius.setAlignment(QtCore.Qt.AlignRight)
        l3.addWidget(self.edit_radius,0,1)


        self.label_centerX = QLabel("Center - X coord.:")
        self.label_centerX.setAlignment(QtCore.Qt.AlignLeft)
        l3.addWidget(self.label_centerX,1,0)

        self.edit_centerX = QLineEdit(self)
        self.edit_centerX.setAlignment(QtCore.Qt.AlignRight)
        l3.addWidget(self.edit_centerX,1,1)


        self.label_centerY = QLabel("Center - Y coord.:")
        self.label_centerY.setAlignment(QtCore.Qt.AlignLeft)
        l3.addWidget(self.label_centerY,2,0)

        self.edit_centerY = QLineEdit(self)
        self.edit_centerY.setAlignment(QtCore.Qt.AlignRight)
        l3.addWidget(self.edit_centerY,2,1)
        




    def plot_circle(self, circle_plot):
        circle_plot.axes.cla()
        Drawing_colored_circle = plt.Circle((0.5,0.5),0.2)
        Drawing_colored_circle.set_color('green')
        
        circle_plot.axes.add_artist(Drawing_colored_circle)
        circle_plot.draw()

        