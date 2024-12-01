from PyQt5.QtWidgets import (
    QAction,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

from PyQt5 import QtCore
from PyQt5.QtGui import (
    QDoubleValidator,
    QIcon,
    QRegExpValidator,
)  

import matplotlib
matplotlib.use('Qt5Agg')

import numpy as np
import CubeCalc
import CanvasThreeD
import SaveFig
from Shape import *

class WindowCube(QWidget, ShapeFunctionality):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Initializes the user interface of the window.

        This method sets up the window layout, widgets, and their connections.
        """
        # Create a 3D Matplotlib canvas for plotting the cube
        sc = CanvasThreeD.MplCanvas(self, width=6, height=5, dpi=100)
        self.setWindowIcon(QIcon('D:\\Programovani\\Python\\naucse\\PyQtMathApp\\Shape_ico.png'))

        # Button to solve and plot Cube
        self.buttonplotCube = QPushButton('Solve and Plot')
        self.buttonplotCube.clicked.connect(lambda: self.plot_cube(sc, self.combo_color.currentText()))
        self.buttonplotCube.setToolTip("Solve and plot picture")

        # Button to export the graph as an image
        self.buttonPicture = QPushButton('Graph Export')
        self.buttonPicture.clicked.connect(lambda: SaveFig.save_fig(self, self.fig, 'Cube.png'))
        self.buttonPicture.setEnabled(False)

        # Button to export data to Excel 
        self.buttonExport = QPushButton('Excel Export')
        self.buttonExport.clicked.connect(lambda: self.export_excel('Cube'))
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
        hbox2.addWidget(self.buttonplotCube)
        hbox2.addWidget(self.buttonPicture)
        hbox2.addWidget(self.buttonExport)
        hbox2.addWidget(self.buttonClear)
        hbox2.addWidget(self.buttonClose)

        # Create layout and group box for input parameters
        layout_param = QGridLayout()
        groupBoxParameters = QGroupBox("Parameters")
        groupBoxParameters.setLayout(layout_param)

        # Create layout and group box for results
        layout_res = QGridLayout()
        groupBoxResults = QGroupBox("Results")
        groupBoxResults.setLayout(layout_res)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(groupBoxParameters)
        vbox1.addWidget(groupBoxResults)
        vbox1.addStretch(1)

        # Create horizontal layout for the graph and the group boxes with input/results
        hbox1.addLayout(vbox1)
        hbox1.addWidget(sc)

        # vertical box layout for:
        # 1. menu
        # 2. horizontal box layout for vbox1 with groupboxes and graph
        # 3. horizontal box layout with buttons
        vbox2 = QVBoxLayout()
        vbox2.setMenuBar(toolbar)
        vbox2.addLayout(hbox1)
        vbox2.addStretch(1)
        vbox2.addLayout(hbox2)

        self.setLayout(vbox2)
        self.setWindowTitle('Cube')

        validator_double = QDoubleValidator(-10000000,10000000,5)
        locale = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)
        validator_double.setLocale(locale)
        validator_double.setNotation(QDoubleValidator.StandardNotation)
        
        validator_possitive = QRegExpValidator(QtCore.QRegExp(r'([1-9][0-9]{0,6})|([0][.][0-9]{1,6})|([1-9]{1,6}[.][0-9]{1,6})'))
        validator_double = QRegExpValidator(QtCore.QRegExp(r'([-][1-9][0-9]{0,6})|([-][1-9][0-9]{0,6}[.])|([-][0][.][0-9]{1,6})|([-][1-9]{1,6}[.][0-9]{1,6})|([1-9][0-9]{0,6})|([1-9][0-9]{0,6}[.])|([0][.][0-9]{1,6})|([1-9]{1,6}[.][0-9]{1,6})'))

        self.label_edge = QLabel("Edge Length:")
        self.label_edge.setAlignment(QtCore.Qt.AlignLeft)
        self.label_edge.setFixedWidth(150)
        layout_param.addWidget(self.label_edge,0,0)

        self.edit_edge = QLineEdit(self)
        self.edit_edge.setValidator(validator_possitive)
        self.edit_edge.setAlignment(QtCore.Qt.AlignRight)
        self.edit_edge.setFixedWidth(150)
        layout_param.addWidget(self.edit_edge,0,1)

        self.label_dim_edge = QLabel("cm")
        self.label_dim_edge.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_edge.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_edge,0,2)


        # Create input field for center coordinate x₀
        self.label_centerX = QLabel("X coordinate (x₀):")
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

        # Create input field for center coordinate y₀
        self.label_centerY = QLabel("Y coordinate (y₀):")
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

        # Create input field for center coordinate z₀
        self.label_centerZ = QLabel("Z coordinate (z₀):")
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

        self.label_combo_color = QLabel("Cube Color:")
        self.label_combo_color.setAlignment(QtCore.Qt.AlignLeft)
        self.label_combo_color.setFixedWidth(150)
        layout_param.addWidget(self.label_combo_color,4,0)

        # Create combo for color
        self.combo_color = self.custom_combo()
        layout_param.addWidget(self.combo_color,4,1)

        # Create field for result - Volume (V)
        self.label_volume = QLabel("Cube Volume (V):")
        self.label_volume.setAlignment(QtCore.Qt.AlignLeft)
        self.label_volume.setFixedWidth(150)
        layout_res.addWidget(self.label_volume,0,0)

        self.label_res_volume = QLabel('0.0')
        self.label_res_volume.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_volume.setFixedWidth(150)
        layout_res.addWidget(self.label_res_volume,0,1)

        self.label_dim_vol = QLabel("cm<sup>3</sup>")
        self.label_dim_vol.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_vol.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_vol,0,2)

        # Create field for result - Surface (S)
        self.label_surface = QLabel("Cube Surface (S):")
        self.label_surface.setAlignment(QtCore.Qt.AlignLeft)
        self.label_surface.setFixedWidth(150)
        layout_res.addWidget(self.label_surface,1,0)

        self.label_res_surface = QLabel('0.0')
        self.label_res_surface.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_surface.setFixedWidth(150)
        layout_res.addWidget(self.label_res_surface,1,1)

        self.label_dim_surface = QLabel("cm<sup>2</sup>")
        self.label_dim_surface.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_surface.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_surface,1,2)

        # Solve and plot picture - button in the top toolbar
        self.exportPictAction = QAction(self)
        self.exportPictAction.setToolTip("Solve and plot picture")
        self.exportPictAction.setIcon(QIcon('CalculateIcon.svg'))
        self.exportPictAction.triggered.connect(lambda: self.plot_cube(sc, self.combo_color.currentText()))
        toolbar.addAction(self.exportPictAction)

        # Export graph as PNG - button in the top toolbar
        self.exportPictAction = QAction(self)
        self.exportPictAction.setToolTip("Save graph as picture")
        self.exportPictAction.setIcon(QIcon('SavePictureIcon.svg'))
        self.exportPictAction.triggered.connect(lambda: SaveFig.save_fig(self, self.fig, 'Cube.png'))
        self.exportPictAction.setEnabled(False)
        toolbar.addAction(self.exportPictAction)

        # Export inputs, results and graph into Excel file - button in the top toolbar
        self.exportXlsxAction = QAction(self)
        self.exportXlsxAction.setToolTip("Export input data, results\nand graph into Excel")
        self.exportXlsxAction.setIcon(QIcon('ExportXLSIcon.svg'))
        self.exportXlsxAction.triggered.connect(lambda: self.export_excel('Cube'))
        self.exportXlsxAction.setEnabled(False)
        toolbar.addAction(self.exportXlsxAction)
        

        # Clear all - inputs, results and graph - button in the top toolbar
        # Button is disable, when result are not allowable
        self.clearAction = QAction(self)
        self.clearAction.setToolTip("Clear all data and results")
        self.clearAction.setIcon(QIcon('ClearResultsIcon.svg'))
        self.clearAction.triggered.connect(lambda: self.clear_inputs(sc))
        self.clearAction.setEnabled(False)
        toolbar.addAction(self.clearAction)

        # Close window - - button in the top toolbar
        self.closeAction = QAction(self)
        self.closeAction.setToolTip("Close window")
        self.closeAction.setIcon(QIcon('CloseAppIcon.svg'))
        self.closeAction.triggered.connect(self.close)
        toolbar.addAction(self.closeAction)


        self.edit_edge.textChanged.connect(self.check_state_rad_and_set_color)
        self.edit_edge.textChanged.connect(lambda: self.clear_results_3D(sc))
        self.edit_edge.textChanged.emit(self.edit_edge.text())

        self.edit_centerX.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerX.textChanged.connect(lambda: self.clear_results_3D(sc))
        self.edit_centerX.textChanged.emit(self.edit_centerX.text())

        self.edit_centerY.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerY.textChanged.connect(lambda: self.clear_results_3D(sc))
        self.edit_centerY.textChanged.emit(self.edit_centerY.text())

        self.edit_centerZ.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerZ.textChanged.connect(lambda: self.clear_results_3D(sc))
        self.edit_centerZ.textChanged.emit(self.edit_centerZ.text())

        self.combo_color.currentIndexChanged.connect(lambda: self.clear_results_3D(sc))

    def plot_cube(self, cube_plot, cube_color):

        if self.edit_edge.text() in ["", "0", "0.", "+", "-"]:
            self.custom_messagebox("Edge can be only a possitive number!")

        elif self.edit_centerX.text() in ["", "+", "-"]:
            self.custom_messagebox("X coordinate (x₀) is missing!")

        elif self.edit_centerY.text() in ["", "+", "-"]:
            self.custom_messagebox("Y coordinate (y₀) is missing!")

        elif self.edit_centerZ.text() in ["", "+", "-"]:
            self.custom_messagebox("Y coordinate (z₀) is missing!")

        else:

            edge = int(self.edit_edge.text())

            axes = [edge, edge, edge]

            data = np.ones(axes, dtype=np.bool_)

            cube_plot.axes.voxels(data, facecolors=cube_color, edgecolors='white')
            # YlGnBu_r

            cube_plot.draw()

            # Update figure reference and perform additional actions
            self.fig = cube_plot.figure
            self.calculate_cube()
            self.clearAction.setEnabled(True)
            self.buttonClear.setEnabled(True)
            self.exportPictAction.setEnabled(True)
            self.buttonPicture.setEnabled(True)
            self.exportXlsxAction.setEnabled(True)
            self.buttonExport.setEnabled(True)


    def calculate_cube(self):

        try:
            edge_cube = float(self.edit_edge.text())
        except ValueError:
            raise ValueError("Please enter a valid numeric value for the edge length.")

        myCube = CubeCalc.Cube(edge_cube)
        cube_volume = round(myCube.volume(),5)
        cube_surface = round(myCube.surface_area(),5)

        self.label_res_volume.setText(str(cube_volume))
        self.label_res_surface.setText(str(cube_surface))

        
    def clear_inputs(self, sc):
        """
        Clears input fields.

        This method clears the text in the radius, x, y and z coordinate fields.
        It then calls the `clear_results_3D` method to clear the results and plot.

        Args:
            sc: The Matplotlib canvas object used for plotting.
        """
        self.edit_edge.clear()
        self.edit_centerX.clear()
        self.edit_centerY.clear()
        self.edit_centerZ.clear()

        # Clears results and the plot using a helper function
        self.clear_results_3D(sc)