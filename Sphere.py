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

        buttonplotCircle = QPushButton('Plot Sphere')
        buttonplotCircle.clicked.connect(lambda: self.plot_sphere(sc))
        buttonClose = QPushButton('Close')
        buttonClose.clicked.connect(self.close)

        self.setFixedSize(800, 400)

        hbox1 = QHBoxLayout()
        
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(buttonplotCircle)
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
        self.setWindowTitle('Sphere')


        self.label_radius = QLabel("Radius:")
        self.label_radius.setAlignment(QtCore.Qt.AlignLeft)
        self.label_radius.setFixedWidth(150)
        layout_param.addWidget(self.label_radius,0,0)

        self.edit_radius = QLineEdit(self)
        self.edit_radius.setAlignment(QtCore.Qt.AlignRight)
        self.edit_radius.setFixedWidth(150)
        layout_param.addWidget(self.edit_radius,0,1)

        self.label_dim_radius = QLabel("cm")
        self.label_dim_radius.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_radius.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_radius,0,2)


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


    def plot_sphere(self, sphere_plot):
        u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:20j]
        x = 2 * np.cos(u) * np.sin(v)
        y = 2 * np.sin(u) * np.sin(v)
        z = 2 * np.cos(v)

        sphere_plot.axes.plot_surface(x, y, z, cmap=plt.cm.Pastel2_r)
        # YlGnBu_r

        sphere_plot.draw()



        
      