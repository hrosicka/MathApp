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
        self.axes = fig.add_subplot(projection='3d')
        super(MplCanvas, self).__init__(fig)


class WindowSphere(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        sc = MplCanvas(self, width=6, height=5, dpi=100)

        buttonplotCircle = QPushButton('Plot Square')
        buttonplotCircle.clicked.connect(lambda: self.plot_sphere(sc))
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
        self.setWindowTitle('Square')  

    def plot_circle(self, circle_plot):
        circle_plot.axes.cla()
        Drawing_colored_circle = plt.Circle((0.5,0.5),0.2)
        circle_plot.axes.add_artist(Drawing_colored_circle)
        circle_plot.draw()

    def plot_sphere(self, sphere_plot):
        u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:20j]
        x = 2 * np.cos(u) * np.sin(v)
        y = 2 * np.sin(u) * np.sin(v)
        z = 2 * np.cos(v)

        sphere_plot.axes.plot_surface(x, y, z, cmap=plt.cm.Pastel2_r)
        # YlGnBu_r

        sphere_plot.draw()



        
      