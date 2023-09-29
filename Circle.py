import sys
from random import randint

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)


import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

import numpy as np

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class WindowCircle(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        sc = MplCanvas(self, width=6, height=5, dpi=100)

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
        vbox.addWidget(sc)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle('Cirle')  

    def plot_circle(self, circle_plot):
        circle_plot.axes.cla()
        Drawing_colored_circle = plt.Circle((0.5,0.5),0.2)
        Drawing_colored_circle.set_color('green')
        
        circle_plot.axes.add_artist(Drawing_colored_circle)
        circle_plot.draw()

        