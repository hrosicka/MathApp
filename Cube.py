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

import CubeCalc

import CanvasThreeD

import random

class WindowCube(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        sc = CanvasThreeD.MplCanvas(self, width=6, height=5, dpi=100)

        buttonplotCube = QPushButton('Plot Cube')
        buttonplotCube.clicked.connect(lambda: self.plot_cube(sc))
        buttonClear = QPushButton('Clear')
        buttonClear.clicked.connect(lambda: self.clear_inputs())
        buttonClose = QPushButton('Close')
        buttonClose.clicked.connect(self.close)

        self.setFixedSize(800, 400)

        hbox1 = QHBoxLayout()
        
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(buttonplotCube)
        hbox2.addWidget(buttonClear)
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
        self.setWindowTitle('Cube')


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

        self.label_centerZ = QLabel("Center - Z coord.:")
        self.label_centerZ.setAlignment(QtCore.Qt.AlignLeft)
        self.label_centerZ.setFixedWidth(150)
        layout_param.addWidget(self.label_centerZ,3,0)

        self.edit_centerZ = QLineEdit(self)
        self.edit_centerZ.setAlignment(QtCore.Qt.AlignRight)
        self.edit_centerZ.setFixedWidth(150)
        layout_param.addWidget(self.edit_centerZ,3,1)

        self.label_dim_z = QLabel("cm")
        self.label_dim_z.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_z.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_z,3,2)

        self.combo_color = QComboBox(self)
        self.combo_color.addItem("green")
        self.combo_color.addItem("red")
        self.combo_color.addItem("blue")
        self.combo_color.addItem("orange")
        self.combo_color.setFixedWidth(150)
        layout_param.addWidget(self.combo_color,4,1)

        self.label_volume = QLabel("Cube Volume:")
        self.label_volume.setAlignment(QtCore.Qt.AlignLeft)
        self.label_volume.setFixedWidth(150)
        layout_res.addWidget(self.label_volume,0,0)

        self.label_res_volume = QLabel('0.0')
        self.label_res_volume.setStyleSheet("background-color : white; color : darkblue")
        self.label_res_volume.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_volume.setFixedWidth(150)
        layout_res.addWidget(self.label_res_volume,0,1)

        self.label_dim_vol = QLabel("cm<sup>3</sup>")
        self.label_dim_vol.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_vol.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_vol,0,2)


        self.label_surface = QLabel("Cube Surface:")
        self.label_surface.setAlignment(QtCore.Qt.AlignLeft)
        self.label_surface.setFixedWidth(150)
        layout_res.addWidget(self.label_surface,1,0)

        self.label_res_surface = QLabel('0.0')
        # self.label_res_area.setFont(QFont('Arial', 12))
        self.label_res_surface.setStyleSheet("background-color : white; color : darkblue")
        self.label_res_surface.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_surface.setFixedWidth(150)
        layout_res.addWidget(self.label_res_surface,1,1)

        self.label_dim_surface = QLabel("cm<sup>2</sup>")
        self.label_dim_surface.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_surface.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_surface,1,2)


    def plot_cube(self, cube_plot):
        u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:20j]
        x = 2 * np.cos(u) * np.sin(v)
        y = 2 * np.sin(u) * np.sin(v)
        z = 2 * np.cos(v)

        cube_plot.axes.plot_surface(x, y, z, cmap=plt.cm.Pastel2_r)
        # YlGnBu_r

        cube_plot.draw()

        self.calculate_sphere()

    def calculate_sphere(self):

        side_cube = float(self.edit_side.text())
        myCube = CubeCalc.Krychle(side_cube)
        cube_volume = round(myCube.objem(),5)
        cube_surface = round(myCube.povrch(),5)

        self.label_res_volume.setText(str(cube_volume))
        self.label_res_surface.setText(str(cube_surface))

        
    def clear_inputs(self):
        self.edit_side.clear()
        self.edit_centerX.clear()
        self.edit_centerY.clear()
        self.label_res_surface.setText("0.0")
        self.label_res_volume.setText("0.0") 