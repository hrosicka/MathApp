from PyQt5.QtWidgets import (
    QAction,
    QComboBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

from PyQt5 import QtCore
from PyQt5.QtGui import (
    QDoubleValidator,
    QIcon,
    QPixmap,
    QRegExpValidator,
    QValidator,
)  

import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

import numpy as np
import EllipsoidCalc
import CanvasThreeD
import SaveFig
from Shape import *

class WindowEllipsoid(QWidget, ShapeFunctionality):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Initializes the user interface of the window.

        This method sets up the window layout, widgets, and their connections.
        """
        # Create a 3D Matplotlib canvas for plotting the circle
        sc = CanvasThreeD.MplCanvas(self, width=6, height=5, dpi=100)
        self.setWindowIcon(QIcon('D:\\Programovani\\Python\\naucse\\PyQtMathApp\\Shape_ico.png'))
        
        # Button to solve and plot the circle
        self.buttonplotEllipsoid = QPushButton('Solve and Plot')
        self.buttonplotEllipsoid.clicked.connect(lambda: self.plot_ellipsoid(sc, self.combo_color.currentText()))
        self.buttonplotEllipsoid.setToolTip("Solve and plot picture")

        # Button to export the graph as an image
        self.buttonPicture = QPushButton('Graph Export')
        self.buttonPicture.clicked.connect(lambda: SaveFig.save_fig(self, self.fig, 'Sphere.png'))
        self.buttonPicture.setEnabled(False)

        # Button to export data to Excel 
        self.buttonExport = QPushButton('Excel Export')
        # self.buttonExport.clicked.connect(lambda: self.export_excel())
        self.buttonExport.setEnabled(False)

        # Button to clear all inputs, results, and the graph
        self.buttonClear = QPushButton('Clear')
        self.buttonClear.clicked.connect(lambda: self.clear_inputs(sc))

        # Button to close the window
        self.buttonClose = QPushButton('Close')
        self.buttonClose.clicked.connect(self.close)

        # Create a toolbar for frequently used actions
        toolbar = QToolBar()
        toolbar.setIconSize(QtCore.QSize(50, 50))

        self.setFixedSize(800, 400)

        hbox1 = QHBoxLayout()
        
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.buttonplotEllipsoid)
        hbox2.addWidget(self.buttonPicture)
        hbox2.addWidget(self.buttonExport)
        hbox2.addWidget(self.buttonClear)
        hbox2.addWidget(self.buttonClose)



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
        self.setWindowTitle('Ellipsoid')


        # validators - regular expression
        validator_possitive = QRegExpValidator(QtCore.QRegExp(r'([1-9][0-9]{0,6})|([0])|([0][.][1-9][0-9]{0,6})|([1-9][0-9]{0,6}[.][1-9][0-9]{0,6})'))
        validator_double = QRegExpValidator(QtCore.QRegExp(r'([-][1-9][0-9]{0,6})|([-][1-9][0-9]{0,6}[.])|([-][0][.][0-9]{1,6})|([-][1-9]{1,6}[.][0-9]{1,6})|([1-9][0-9]{0,6})|([1-9][0-9]{0,6}[.])|([0][.][0-9]{1,6})|([1-9]{1,6}[.][0-9]{1,6})'))

        # Create input field for Semi-major axis (a)
        self.label_axis_a = QLabel("Semi axis (a):")
        self.label_axis_a.setAlignment(QtCore.Qt.AlignLeft)
        self.label_axis_a.setFixedWidth(150)
        layout_param.addWidget(self.label_axis_a,0,0)

        self.edit_axis_a = QLineEdit(self)
        self.edit_axis_a.setValidator(validator_possitive)
        self.edit_axis_a.setAlignment(QtCore.Qt.AlignRight)
        self.edit_axis_a.setFixedWidth(150)
        layout_param.addWidget(self.edit_axis_a,0,1)

        self.label_dim_axis_a = QLabel("cm")
        self.label_dim_axis_a.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_axis_a.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_axis_a,0,2)

        
        # Create input field for Semi-minor axis (b)
        self.label_axis_b = QLabel("Semi axis (b):")
        self.label_axis_b.setAlignment(QtCore.Qt.AlignLeft)
        self.label_axis_b.setFixedWidth(150)
        layout_param.addWidget(self.label_axis_b,1,0)

        self.edit_axis_b = QLineEdit(self)
        self.edit_axis_b.setValidator(validator_possitive)
        self.edit_axis_b.setAlignment(QtCore.Qt.AlignRight)
        self.edit_axis_b.setFixedWidth(150)
        layout_param.addWidget(self.edit_axis_b,1,1)

        self.label_dim_axis_b = QLabel("cm")
        self.label_dim_axis_b.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_axis_b.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_axis_b,1,2)

        # Create input field for Semi-minor axis (c)
        self.label_axis_c = QLabel("Semi axis (c):")
        self.label_axis_c.setAlignment(QtCore.Qt.AlignLeft)
        self.label_axis_c.setFixedWidth(150)
        layout_param.addWidget(self.label_axis_c,2,0)

        self.edit_axis_c = QLineEdit(self)
        self.edit_axis_c.setValidator(validator_possitive)
        self.edit_axis_c.setAlignment(QtCore.Qt.AlignRight)
        self.edit_axis_c.setFixedWidth(150)
        layout_param.addWidget(self.edit_axis_c,2,1)

        self.label_dim_axis_c = QLabel("cm")
        self.label_dim_axis_c.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_axis_c.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_axis_c,2,2)

        # Create input field for center coordinate x₀
        self.label_centerX = QLabel("X coordinate (x₀):")
        self.label_centerX.setAlignment(QtCore.Qt.AlignLeft)
        self.label_centerX.setFixedWidth(150)
        layout_param.addWidget(self.label_centerX,3,0)

        self.edit_centerX = QLineEdit(self)
        self.edit_centerX.setValidator(validator_double)
        self.edit_centerX.setAlignment(QtCore.Qt.AlignRight)
        self.edit_centerX.setFixedWidth(150)
        layout_param.addWidget(self.edit_centerX,3,1)

        self.label_dim_x = QLabel("cm")
        self.label_dim_x.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_x.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_x,3,2)

        # Create input field for center coordinate y₀
        self.label_centerY = QLabel("Y coordinate (y₀):")
        self.label_centerY.setAlignment(QtCore.Qt.AlignLeft)
        self.label_centerY.setFixedWidth(150)
        layout_param.addWidget(self.label_centerY,4,0)

        self.edit_centerY = QLineEdit(self)
        self.edit_centerY.setValidator(validator_double)
        self.edit_centerY.setAlignment(QtCore.Qt.AlignRight)
        self.edit_centerY.setFixedWidth(150)
        layout_param.addWidget(self.edit_centerY,4,1)

        self.label_dim_y = QLabel("cm")
        self.label_dim_y.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_y.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_y,4,2)

        # Create input field for center coordinate z₀
        self.label_centerZ = QLabel("Z coordinate (z₀):")
        self.label_centerZ.setAlignment(QtCore.Qt.AlignLeft)
        self.label_centerZ.setFixedWidth(150)
        layout_param.addWidget(self.label_centerZ,5,0)

        self.edit_centerZ = QLineEdit(self)
        self.edit_centerZ.setValidator(validator_double)
        self.edit_centerZ.setAlignment(QtCore.Qt.AlignRight)
        self.edit_centerZ.setFixedWidth(150)
        layout_param.addWidget(self.edit_centerZ,5,1)

        self.label_dim_z = QLabel("cm")
        self.label_dim_z.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_z.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_z,5,2)

        self.label_combo_color = QLabel("Sphere Color:")
        self.label_combo_color.setAlignment(QtCore.Qt.AlignLeft)
        self.label_combo_color.setFixedWidth(150)
        layout_param.addWidget(self.label_combo_color,6,0)


        self.label_combo_color = QLabel("Ellipsoid Color:")
        self.label_combo_color.setAlignment(QtCore.Qt.AlignLeft)
        self.label_combo_color.setFixedWidth(150)
        layout_param.addWidget(self.label_combo_color,6,0)


        self.combo_color = QComboBox(self)
        colors = ["black", 
                  "blue", 
                  "gray", 
                  "green", 
                  "magenta", 
                  "orange", 
                  "pink", 
                  "red", 
                  "violet", 
                  "yellow"]
        self.combo_color.addItems(colors)
        
        self.combo_color.setFixedWidth(150)
        self.combo_color.setFixedHeight(28)
        layout_param.addWidget(self.combo_color,6,1)




        self.label_volume = QLabel("Ellipsoid Volume:")
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


        self.label_surface = QLabel("Ellipsoid Surface:")
        self.label_surface.setAlignment(QtCore.Qt.AlignLeft)
        self.label_surface.setFixedWidth(150)
        layout_res.addWidget(self.label_surface,1,0)

        self.label_res_surface = QLabel('0.0')
        self.label_res_surface.setStyleSheet("background-color : white; color : darkblue")
        self.label_res_surface.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_surface.setFixedWidth(150)
        layout_res.addWidget(self.label_res_surface,1,1)

        self.label_dim_surface = QLabel("cm<sup>2</sup>")
        self.label_dim_surface.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_surface.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_surface,1,2)


        self.edit_axis_a.textChanged.connect(self.check_state_rad_and_set_color)
        self.edit_axis_a.textChanged.emit(self.edit_axis_a.text())

        self.edit_axis_b.textChanged.connect(self.check_state_rad_and_set_color)
        self.edit_axis_b.textChanged.emit(self.edit_axis_b.text())

        self.edit_axis_c.textChanged.connect(self.check_state_rad_and_set_color)
        self.edit_axis_c.textChanged.emit(self.edit_axis_c.text())

        self.edit_centerX.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerX.textChanged.emit(self.edit_centerX.text())

        self.edit_centerY.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerY.textChanged.emit(self.edit_centerY.text())

        self.edit_centerZ.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerZ.textChanged.emit(self.edit_centerZ.text())


    def plot_ellipsoid(self, sphere_plot, circle_color):
        
        sphere_plot.axes.cla()
        sphere_plot.draw()
        self.label_res_surface.setText("0.0")
        self.label_res_volume.setText("0.0")
        

        if self.edit_axis_a.text() in ["", "0", "0.", "+", "-"]:
            self.custom_messagebox("Semi axis (a) can be only a possitive number!")

        elif self.edit_axis_b.text() in ["", "0", "0.", "+", "-"]:
            self.custom_messagebox("Semi axis (b) can be only a possitive number!")

        elif self.edit_axis_c.text() in ["", "0", "0.", "+", "-"]:
            self.custom_messagebox("Semi axis (c) can be only a possitive number!")

        elif self.edit_centerX.text() in ["", "+", "-"]:
            self.custom_messagebox("X coordinate (x₀) is missing!")

        elif self.edit_centerY.text() in ["", "+", "-"]:
            self.custom_messagebox("Y coordinate (y₀) is missing!")

        elif self.edit_centerZ.text() in ["", "+", "-"]:
            self.custom_messagebox("Z coordinate (z₀) is missing!")
 
        else:

            center_x = float(self.edit_centerX.text())
            center_y = float(self.edit_centerY.text())
            center_z = float(self.edit_centerZ.text())
            r = float(self.edit_axis_a.text())

            u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:30j]
            
            x = r * np.outer(np.cos(u), np.sin(v)) + center_x
            y = r * np.outer(np.sin(u), np.sin(v)) + center_y
            z = r * np.outer(np.ones(np.size(u)), np.cos(v)) + center_z

            sphere_plot.axes.plot_surface(x, y, z, color=circle_color)
            sphere_plot.draw()

            self.fig = sphere_plot.figure

            self.calculate_ellipsoid()

            #self.clearAction.setEnabled(True)
            self.buttonClear.setEnabled(True)
            #self.exportPictAction.setEnabled(True)
            self.buttonPicture.setEnabled(True)
            #self.exportXlsxAction.setEnabled(True)
            self.buttonExport.setEnabled(True)


    def calculate_ellipsoid(self):

        semi_axis_a = float(self.edit_axis_a.text())
        semi_axis_b = float(self.edit_axis_b.text())
        semi_axis_c = float(self.edit_axis_c.text())

        myEllipsoid = EllipsoidCalc.Ellipsoid(semi_axis_a, semi_axis_b, semi_axis_c)
        ellipsoid_volume = round(myEllipsoid.volume(),5)
        ellipsoid_surface = round(myEllipsoid.surface_area(),5)

        self.label_res_volume.setText(str(ellipsoid_volume))
        self.label_res_surface.setText(str(ellipsoid_surface))



        
      