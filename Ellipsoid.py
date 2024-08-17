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
        
        # Button to solve and plot the Ellipsoid
        self.buttonplotEllipsoid = QPushButton('Solve and Plot')
        self.buttonplotEllipsoid.clicked.connect(lambda: self.plot_ellipsoid(sc, self.combo_color.currentText()))
        self.buttonplotEllipsoid.setToolTip("Solve and plot picture")

        # Button to export the graph as an image
        self.buttonPicture = QPushButton('Graph Export')
        self.buttonPicture.clicked.connect(lambda: SaveFig.save_fig(self, self.fig, 'Ellipsoid.png'))
        self.buttonPicture.setEnabled(False)

        # Button to export data to Excel 
        self.buttonExport = QPushButton('Excel Export')
        self.buttonExport.clicked.connect(lambda: self.export_excel('Ellipsoid'))
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

        self.setFixedSize(850, 568)

        hbox1 = QHBoxLayout()
        
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.buttonplotEllipsoid)
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
        self.setWindowTitle('Ellipsoid')

        validator_double = QDoubleValidator(-10000000,10000000,5)
        locale = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)
        validator_double.setLocale(locale)
        validator_double.setNotation(QDoubleValidator.StandardNotation)

        validator_possitive = QRegExpValidator(QtCore.QRegExp(r'([1-9][0-9]{0,6})|([0][.][0-9]{1,6})|([1-9]{1,6}[.][0-9]{1,6})'))
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

        # Create combo for color
        self.combo_color = self.custom_combo()
        layout_param.addWidget(self.combo_color,6,1)

        # Create field for result - Volume (V)
        self.label_volume = QLabel("Ellipsoid Volume:")
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
        self.label_surface = QLabel("Ellipsoid Surface:")
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
        self.exportPictAction.triggered.connect(lambda: self.plot_ellipsoid(sc, self.combo_color.currentText()))
        toolbar.addAction(self.exportPictAction)

        # Export graph as PNG - button in the top toolbar
        self.exportPictAction = QAction(self)
        self.exportPictAction.setToolTip("Save graph as picture")
        self.exportPictAction.setIcon(QIcon('SavePictureIcon.svg'))
        self.exportPictAction.triggered.connect(lambda: SaveFig.save_fig(self, self.fig, 'Ellipsoid.png'))
        self.exportPictAction.setEnabled(False)
        toolbar.addAction(self.exportPictAction)

        # Export inputs, results and graph into Excel file - button in the top toolbar
        self.exportXlsxAction = QAction(self)
        self.exportXlsxAction.setToolTip("Export input data, results\nand graph into Excel")
        self.exportXlsxAction.setIcon(QIcon('ExportXLSIcon.svg'))
        self.exportXlsxAction.triggered.connect(lambda: self.export_excel('Ellipsoid'))
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


    def plot_ellipsoid(self, sphere_plot, ellipsoid_color):
        
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
            rx = float(self.edit_axis_a.text())
            ry = float(self.edit_axis_b.text())
            rz = float(self.edit_axis_c.text())

            u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:30j]
            
            x = rx * np.outer(np.cos(u), np.sin(v)) + center_x
            y = ry * np.outer(np.sin(u), np.sin(v)) + center_y
            z = rz * np.outer(np.ones(np.size(u)), np.cos(v)) + center_z

            minus_x = float(self.edit_centerX.text())-1.5*float(self.edit_axis_a.text())
            plus_x = float(self.edit_centerX.text())+1.5*float(self.edit_axis_a.text())
            minus_y = float(self.edit_centerY.text())-2*float(self.edit_axis_b.text())
            plus_y = float(self.edit_centerY.text())+2*float(self.edit_axis_b.text())
            minus_z = float(self.edit_centerZ.text())-2*float(self.edit_axis_c.text())
            plus_z = float(self.edit_centerZ.text())+2*float(self.edit_axis_c.text())

            sphere_plot.axes.set_xlim(minus_x, plus_x)
            sphere_plot.axes.set_ylim(minus_x, plus_x)
            sphere_plot.axes.set_zlim(minus_x, plus_x)

            sphere_plot.axes.plot_wireframe(x, y, z, rstride=20, cstride=20, color=ellipsoid_color)
            sphere_plot.draw()

            self.fig = sphere_plot.figure

            self.calculate_ellipsoid()

            self.clearAction.setEnabled(True)
            self.buttonClear.setEnabled(True)
            self.exportPictAction.setEnabled(True)
            self.buttonPicture.setEnabled(True)
            self.exportXlsxAction.setEnabled(True)
            self.buttonExport.setEnabled(True)


    def calculate_ellipsoid(self):
        """Calculates the volume and surface area of an ellipsoid.

        This method retrieves the semi-axis lengths (a, b, c) from the user interface,
        creates an `EllipsoidCalc.Ellipsoid` object, calculates the ellipsoid's volume
        and surface area rounded to five decimal places, and updates the corresponding
        labels with the results.

        Raises:
            ValueError: If any of the entered semi-axis lengths are non-numeric.
        """
        try:
            semi_axis_a = float(self.edit_axis_a.text())
            semi_axis_b = float(self.edit_axis_b.text())
            semi_axis_c = float(self.edit_axis_c.text())

        except ValueError:
            # Handle non-numeric input gracefully (e.g., display an error message)
            raise ValueError("Please enter valid numeric values for all semi-axis lengths.")

        myEllipsoid = EllipsoidCalc.Ellipsoid(semi_axis_a, semi_axis_b, semi_axis_c)
        ellipsoid_volume = round(myEllipsoid.volume(),5)
        ellipsoid_surface = round(myEllipsoid.surface_area(),5)

        self.label_res_volume.setText(str(ellipsoid_volume))
        self.label_res_surface.setText(str(ellipsoid_surface))


    def clear_inputs(self, sc):
        """Clears input fields, plot, and output labels.

        This method resets the application's state by:
        - Clearing the plot area.
        - Emptying input fields for ellipsoid parameters and center coordinates.
        - Setting output labels for surface area and volume to "0.0".
        - Disabling export and clear buttons.

        Args:
            sc: The plot canvas object.
        """
        sc.axes.cla()
        sc.draw()

        self.edit_axis_a.clear()
        self.edit_axis_b.clear()
        self.edit_axis_c.clear()
        self.edit_centerX.clear()
        self.edit_centerY.clear()
        self.edit_centerZ.clear()

        self.label_res_surface.setText("0.0")
        self.label_res_volume.setText("0.0")
        
        self.clearAction.setEnabled(False)
        self.exportPictAction.setEnabled(False)
        self.buttonPicture.setEnabled(False)
        self.exportXlsxAction.setEnabled(False)
        self.buttonExport.setEnabled(False)
        self.buttonClear.setEnabled(False)

    
    def clear_results(self, sc):
        """
        Clears all inputs, results, and the graph.

        This method clears the text in the radius, x coordinate, and y coordinate
        fields, as well as the result fields for diameter, circumference, and area.
        It also clears the plot on the Matplotlib canvas.

        Args:
            sc: The Matplotlib canvas object used for plotting.
        """
        sc.axes.cla()
        sc.draw()
        self.label_res_surface.setText("0.0")
        self.label_res_volume.setText("0.0")
        self.clearAction.setEnabled(False)
        self.exportPictAction.setEnabled(False)
        self.buttonPicture.setEnabled(False)
        self.exportXlsxAction.setEnabled(False)
        self.buttonExport.setEnabled(False)
        self.buttonClear.setEnabled(False)