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
    QMessageBox,
)

from PyQt5 import QtCore
from PyQt5.QtGui import (
    QFont, 
    QValidator,
    QDoubleValidator, 
    QRegExpValidator,
)  

import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

import numpy as np

import SphereCalc

import CanvasThreeD

import random


class WindowSphere(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        sc = CanvasThreeD.MplCanvas(self, width=6, height=5, dpi=100)

        buttonplotSphere = QPushButton('Plot Sphere')
        buttonplotSphere.clicked.connect(lambda: self.plot_sphere(sc, self.combo_color.currentText()))
        buttonClear = QPushButton('Clear')
        buttonClear.clicked.connect(lambda: self.clear_inputs())
        buttonClose = QPushButton('Close')
        buttonClose.clicked.connect(self.close)

        self.setFixedSize(800, 405)

        hbox1 = QHBoxLayout()
        
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(buttonplotSphere)
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
        self.setWindowTitle('Sphere')

        validator_double = QDoubleValidator()
        validator_possitive = QRegExpValidator(QtCore.QRegExp(r'([1-9][0-9]{0,6})|([0][.][0-9]{1,6})|([1-9]{1,6}[.][0-9]{1,6})'))


        self.label_radius = QLabel("Radius:")
        self.label_radius.setAlignment(QtCore.Qt.AlignLeft)
        self.label_radius.setFixedWidth(150)
        layout_param.addWidget(self.label_radius,0,0)

        self.edit_radius = QLineEdit(self)
        self.edit_radius.setValidator(validator_possitive)
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
        self.edit_centerX.setValidator(validator_double)
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
        self.edit_centerY.setValidator(validator_double)
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
        self.edit_centerZ.setValidator(validator_double)
        self.edit_centerZ.setAlignment(QtCore.Qt.AlignRight)
        self.edit_centerZ.setFixedWidth(150)
        layout_param.addWidget(self.edit_centerZ,3,1)

        self.label_dim_z = QLabel("cm")
        self.label_dim_z.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_z.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_z,3,2)

        self.label_combo_color = QLabel("Circle Color:")
        self.label_combo_color.setAlignment(QtCore.Qt.AlignLeft)
        self.label_combo_color.setFixedWidth(150)
        layout_param.addWidget(self.label_combo_color,4,0)


        self.combo_color = QComboBox(self)
        self.combo_color.addItem("green")
        self.combo_color.addItem("red")
        self.combo_color.addItem("blue")
        self.combo_color.addItem("orange")
        self.combo_color.setFixedWidth(150)
        layout_param.addWidget(self.combo_color,4,1)

        self.label_volume = QLabel("Sphere Volume:")
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


        self.label_surface = QLabel("Sphere Surface:")
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


        self.edit_radius.textChanged.connect(self.check_state_rad)
        self.edit_radius.textChanged.emit(self.edit_radius.text())

        self.edit_centerX.textChanged.connect(self.check_state_centerX)
        self.edit_centerX.textChanged.emit(self.edit_centerX.text())

        self.edit_centerY.textChanged.connect(self.check_state_centerY)
        self.edit_centerY.textChanged.emit(self.edit_centerY.text())

        self.edit_centerZ.textChanged.connect(self.check_state_centerZ)
        self.edit_centerZ.textChanged.emit(self.edit_centerZ.text())


    def plot_sphere(self, sphere_plot, circle_color):
        
        sphere_plot.axes.cla()
        sphere_plot.draw()
        self.label_res_surface.setText("0.0")
        self.label_res_volume.setText("0.0")
        

        if self.edit_radius.text() == "0" or self.edit_radius.text() == "":
            QMessageBox.about(self, 'Error','Radius can be only a possitive number')

        elif self.edit_centerX.text() == "":
            QMessageBox.about(self, 'Error','Center - X coord. is missing')

        elif self.edit_centerY.text() == "":
            QMessageBox.about(self, 'Error','Center - Y coord. is missing')

        elif self.edit_centerZ.text() == "":
            QMessageBox.about(self, 'Error','Center - Z coord. is missing')
 
        else:

            center_x = float(self.edit_centerX.text())
            center_y = float(self.edit_centerY.text())
            center_z = float(self.edit_centerZ.text())
            r = float(self.edit_radius.text())

            u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:30j]
            
            '''
            x = 2 * np.cos(u) * np.sin(v)
            y = 2 * np.sin(u) * np.sin(v)
            z = 2 * np.cos(v)
            '''

            x = r * np.outer(np.cos(u), np.sin(v)) + center_x
            y = r * np.outer(np.sin(u), np.sin(v)) + center_y
            z = r * np.outer(np.ones(np.size(u)), np.cos(v)) + center_z

            # alpha = 1.0 / random.randint(25, 100)
            sphere_plot.axes.plot_surface(x, y, z, color=circle_color)
            # YlGnBu_r
            # Pastel2_r
            # sphere_plot.axes.plot_surface(x, y, z, cmap=plt.cm.YlGnBu_r)
            # sphere_plot.axes.plot_surface(x, y, z, color='b')
            # sphere_plot.axes.plot_surface(x, y, z, cmap=plt.cm.PiYG)

            sphere_plot.draw()

            self.calculate_sphere()

    def calculate_sphere(self):

        radius_sphere = float(self.edit_radius.text())
        mySphere = SphereCalc.Koule(radius_sphere)
        sphere_volume = round(mySphere.objem(),5)
        sphere_surface = round(mySphere.povrch(),5)

        self.label_res_volume.setText(str(sphere_volume))
        self.label_res_surface.setText(str(sphere_surface))


    def clear_inputs(self):
        self.edit_radius.clear()
        self.edit_centerX.clear()
        self.edit_centerY.clear()
        self.edit_centerZ.clear()
        self.label_res_surface.setText("0.0")
        self.label_res_volume.setText("0.0")
        
    def check_state_rad(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if self.edit_radius.text() == "0" or self.edit_radius.text() == "":
            color = '#f6989d' # red
        elif state == QValidator.Acceptable:
            color = '#c4df9b' # green
        elif state == QValidator.Intermediate:
            color = '#fff79a' # yellow
        else:
            color = '#f6989d' # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)


    def check_state_centerX(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if self.edit_centerX.text() == "":
            color = '#f6989d' # red
        elif state == QValidator.Acceptable:
            color = '#c4df9b' # green
        elif state == QValidator.Intermediate:
            color = '#fff79a' # yellow
        else:
            color = '#f6989d' # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)   


    def check_state_centerY(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if self.edit_centerY.text() == "":
            color = '#f6989d' # red
        elif state == QValidator.Acceptable:
            color = '#c4df9b' # green
        elif state == QValidator.Intermediate:
            color = '#fff79a' # yellow
        else:
            color = '#f6989d' # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color) 


    def check_state_centerZ(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if self.edit_centerZ.text() == "":
            color = '#f6989d' # red
        elif state == QValidator.Acceptable:
            color = '#c4df9b' # green
        elif state == QValidator.Intermediate:
            color = '#fff79a' # yellow
        else:
            color = '#f6989d' # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color) 