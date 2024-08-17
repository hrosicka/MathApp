import os

from PyQt5.QtWidgets import (
    QAction, 
    QFileDialog,
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
    QIcon,
    QRegExpValidator,
)

import matplotlib
matplotlib.use('Qt5Agg')

import pandas as pd
from matplotlib.patches import Ellipse

import EllipseCalc
import Canvas
import SaveFig
from Shape import *

class WindowEllipse(QWidget, ShapeFunctionality):
    """
    This class represents the main window of the circle calculation application.

    It handles the user interface elements, input validation, calculation logic,
    and interaction with external libraries for plotting and data export.
    """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Initializes the user interface of the window.

        This method sets up the window layout, widgets, and their connections.
        """
        # Create a Matplotlib canvas for plotting the circle
        sc = Canvas.MplCanvas(self, width=6, height=6, dpi=100)
        self.setWindowIcon(QIcon('D:\\Programovani\\Python\\naucse\\PyQtMathApp\\Shape_ico.png'))

        # Button to solve and plot the ellipse
        self.buttonplotEllipse = QPushButton('Solve and Plot')
        self.buttonplotEllipse.clicked.connect(lambda: self.plot_ellipse(sc, self.combo_color.currentText()))
        self.buttonplotEllipse.setToolTip("Solve and plot picture")

        # Button to export the graph as an image
        self.buttonPicture = QPushButton('Graph Export')
        self.buttonPicture.clicked.connect(lambda: SaveFig.save_fig(self, self.fig, 'Ellipse.png'))
        self.buttonPicture.setEnabled(False)
        self.buttonPicture.setToolTip("Save graph as picture")

        # Button to export data to Excel 
        self.buttonExport = QPushButton('Excel Export')
        self.buttonExport.clicked.connect(lambda: self.export_excel('Ellipse'))
        self.buttonExport.setEnabled(False)
        self.buttonExport.setToolTip("Save inputs, results and graph into Excel")

        # Button to clear all inputs, results, and the graph
        self.buttonClear = QPushButton('Clear')
        self.buttonClear.clicked.connect(lambda: self.clear_inputs(sc))
        self.buttonClear.setEnabled(False)
        self.buttonClear.setToolTip("Clear all data and results")

        # Button to close the window
        self.buttonClose = QPushButton('Close')
        self.buttonClose.clicked.connect(self.close)
        self.buttonClose.setToolTip("Close window")

        # Create a toolbar for frequently used actions
        toolbar = QToolBar()
        toolbar.setIconSize(QtCore.QSize(50, 50))

        # Set the window size
        self.setFixedSize(850, 488)

        hbox1 = QHBoxLayout()
        
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.buttonplotEllipse)
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
        self.setWindowTitle('Ellipse')  

        # validators - regular expression
        validator_possitive = QRegExpValidator(QtCore.QRegExp(r'([1-9][0-9]{0,6})|([0][.][0-9]{1,6})|([1-9]{1,6}[.][0-9]{1,6})'))
        validator_double = QRegExpValidator(QtCore.QRegExp(r'([-][1-9][0-9]{0,6})|([-][1-9][0-9]{0,6}[.])|([-][0][.][0-9]{1,6})|([-][1-9]{1,6}[.][0-9]{1,6})|([1-9][0-9]{0,6})|([1-9][0-9]{0,6}[.])|([0][.][0-9]{1,6})|([1-9]{1,6}[.][0-9]{1,6})'))
        
        # Create input field for Semi-major axis (a)
        self.label_axis_a = QLabel("Semi-major axis (a):")
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
        self.label_axis_b = QLabel("Semi-minor axis (b):")
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

        # Create input field for center coordinate x₀
        self.label_centerX = QLabel("X coordinate (x₀):")
        self.label_centerX.setAlignment(QtCore.Qt.AlignLeft)
        self.label_centerX.setFixedWidth(150)
        layout_param.addWidget(self.label_centerX,2,0)

        self.edit_centerX = QLineEdit(self)
        self.edit_centerX.setValidator(validator_double)
        self.edit_centerX.setAlignment(QtCore.Qt.AlignRight)
        self.edit_centerX.setFixedWidth(150)
        layout_param.addWidget(self.edit_centerX,2,1)

        self.label_dim_x = QLabel("cm")
        self.label_dim_x.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_x.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_x,2,2)

        # Create input field for center coordinate y₀
        self.label_centerY = QLabel("Y coordinate (y₀):")
        self.label_centerY.setAlignment(QtCore.Qt.AlignLeft)
        self.label_centerY.setFixedWidth(150)
        layout_param.addWidget(self.label_centerY,3,0)

        self.edit_centerY = QLineEdit(self)
        self.edit_centerY.setValidator(validator_double)
        self.edit_centerY.setAlignment(QtCore.Qt.AlignRight)
        self.edit_centerY.setFixedWidth(150)
        layout_param.addWidget(self.edit_centerY,3,1)

        self.label_dim_y = QLabel("cm")
        self.label_dim_y.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_y.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_y,3,2)


        self.label_combo_color = QLabel("Ellipse Color:")
        self.label_combo_color.setAlignment(QtCore.Qt.AlignLeft)
        self.label_combo_color.setFixedWidth(150)
        layout_param.addWidget(self.label_combo_color,4,0)

        # Create combo for color
        self.combo_color = self.custom_combo()
        layout_param.addWidget(self.combo_color,4,1)
        
        # Create field for result - Circumference (c)
        self.label_perimeter = QLabel("Circumference (c):")
        self.label_perimeter.setAlignment(QtCore.Qt.AlignLeft)
        self.label_perimeter.setFixedWidth(150)
        layout_res.addWidget(self.label_perimeter,0,0)

        self.label_res_perimeter = QLabel('0.0')
        self.label_res_perimeter.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_perimeter.setFixedWidth(150)
        layout_res.addWidget(self.label_res_perimeter,0,1)

        self.label_dim_per = QLabel("cm")
        self.label_dim_per.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_per.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_per,0,2)

        # Create field for result - Area (A)
        self.label_area = QLabel("Area (A):")
        self.label_area.setAlignment(QtCore.Qt.AlignLeft)
        self.label_area.setFixedWidth(150)
        layout_res.addWidget(self.label_area,1,0)

        self.label_res_area = QLabel('0.0')
        # self.label_res_area.setFont(QFont('Arial', 12))
        self.label_res_area.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_area.setFixedWidth(150)
        layout_res.addWidget(self.label_res_area,1,1)

        self.label_dim_area = QLabel("cm<sup>2</sup>")
        self.label_dim_area.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_area.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_area,1,2)

        # Solve and plot picture - button in the top toolbar
        self.solveAction = QAction(self)
        self.solveAction.setToolTip("Solve and plot picture")
        self.solveAction.setIcon(QIcon('CalculateIcon.svg'))
        self.solveAction.triggered.connect(lambda: self.plot_circle(sc, self.combo_color.currentText()))
        toolbar.addAction(self.solveAction)

        # Export graph as PNG - button in the top toolbar
        self.exportPictAction = QAction(self)
        self.exportPictAction.setToolTip("Save graph as picture")
        self.exportPictAction.setIcon(QIcon('SavePictureIcon.svg'))
        self.exportPictAction.triggered.connect(lambda: SaveFig.save_fig(self, self.fig, 'Circle.png'))
        self.exportPictAction.setEnabled(False)
        toolbar.addAction(self.exportPictAction)

        # Export inputs, results and graph into Excel file - button in the top toolbar
        self.exportXlsxAction = QAction(self)
        self.exportXlsxAction.setToolTip("Export input data, results\nand graph into Excel")
        self.exportXlsxAction.setIcon(QIcon('ExportXLSIcon.svg'))
        self.exportXlsxAction.triggered.connect(lambda: self.export_excel('Ellipse'))
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
        self.edit_axis_a.textChanged.connect(lambda: self.clear_results_2D(sc))
        self.edit_axis_a.textChanged.emit(self.edit_axis_a.text())

        self.edit_axis_b.textChanged.connect(self.check_state_rad_and_set_color)
        self.edit_axis_b.textChanged.connect(lambda: self.clear_results_2D(sc))
        self.edit_axis_b.textChanged.emit(self.edit_axis_b.text())

        self.edit_centerX.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerX.textChanged.connect(lambda: self.clear_results_2D(sc))
        self.edit_centerX.textChanged.emit(self.edit_centerX.text())

        self.edit_centerY.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerY.textChanged.connect(lambda: self.clear_results_2D(sc))
        self.edit_centerY.textChanged.emit(self.edit_centerY.text())

        self.combo_color.currentIndexChanged.connect(lambda: self.clear_results_2D(sc))


    def plot_ellipse(self, ellipse_plot, ellipse_color):
        """
        Plots an ellipse on the provided Matplotlib figure and updates display elements.

        This method performs the following actions:
        1. Clears the existing plot on `ellipse_plot`.
        2. Resets the ellipse area and perimeter labels to "0.0".
        3. Validates user input for semi-axis lengths (a, b) and center coordinates (x, y):
        - Displays a custom message box using `self.custom_messagebox` if:
            - Semi-major axis (a) is 0 or empty.
            - Semi-minor axis (b) is 0 or empty.
            - X coordinate (x₀) is missing.
            - Y coordinate (y₀) is missing.
        4. If all input is valid:
        - Creates an `Ellipse` object with the specified center, width, height, and color.
        - Sets the plot's X and Y limits to ensure the entire ellipse is visible.
        - Adds the ellipse object to the plot's artist list.
        - Redraws the plot.
        - Updates `self.fig` to reference the Matplotlib figure for potential future use.
        - Calls `self.calculate_ellipse()` to calculate and display ellipse properties.
        - Enables the "Clear" and "Export" buttons for user interaction.

        Args:
            ellipse_plot (matplotlib.pyplot.Figure): The Matplotlib figure to plot the ellipse on.
            ellipse_color (str): The color of the ellipse to be plotted.
        """
        
        ellipse_plot.axes.cla()
        self.label_res_area.setText("0.0")
        self.label_res_perimeter.setText("0.0")
        

        if self.edit_axis_a.text() == "0" or self.edit_axis_a.text() == "":
            self.custom_messagebox("Semi-major axis (a) can be only a possitive number!")

        elif self.edit_axis_b.text() == "0" or self.edit_axis_b.text() == "":
            self.custom_messagebox("Semi-minor axis (b) can be only a possitive number!")

        elif self.edit_centerX.text() == "":
            self.custom_messagebox("X coordinate (x₀) is missing!")

        elif self.edit_centerY.text() == "":
            self.custom_messagebox("Y coordinate (y₀) is missing!")

        else:

            center_x = float(self.edit_centerX.text())
            center_y = float(self.edit_centerY.text())
            width = 2 * float(self.edit_axis_a.text())
            height = 2 * float(self.edit_axis_b.text())
            Drawing_colored_ellipse = Ellipse((center_x, center_y), width, height, color=ellipse_color)

            ellipse_plot.axes.set_xlim(center_x - width, center_x + width)
            ellipse_plot.axes.set_ylim(center_y - height, center_y + height)

            ellipse_plot.axes.add_artist(Drawing_colored_ellipse)
            ellipse_plot.draw()

            self.fig = ellipse_plot.figure
            self.calculate_ellipse()

            self.clearAction.setEnabled(True)
            self.buttonClear.setEnabled(True)
            self.exportPictAction.setEnabled(True)
            self.buttonPicture.setEnabled(True)
            self.exportXlsxAction.setEnabled(True)
            self.buttonExport.setEnabled(True)

    def calculate_ellipse(self):
        """
        Calculates the perimeter and area of an ellipse.

        This method retrieves the semi-axis lengths (a, b) from the user interface,
        creates an `EllipseCalc.Ellipse` object, calculates the ellipse's perimeter
        and area rounded to five decimal places, and updates the corresponding
        labels with the results.

        Raises:
            ValueError: If any of the entered semi-axis lengths are non-numeric.
        """

        try:
            axis_a = float(self.edit_axis_a.text())
            axis_b = float(self.edit_axis_b.text())
        except ValueError:
            # Handle non-numeric input gracefully (e.g., display an error message)
            raise ValueError("Please enter valid numeric values for both semi-axis lengths.")

        myEllipse = EllipseCalc.Ellipse(axis_a, axis_b)
        ellipse_perimeter = round(myEllipse.circumference(),5)
        ellipse_area = round(myEllipse.area(),5)

        self.label_res_perimeter.setText(str(ellipse_perimeter))
        self.label_res_area.setText(str(ellipse_area))


    def clear_inputs(self, sc):
        """
        Clears input fields.

        This method clears the text in the a axis, b axis, x coordinate, and y coordinate fields.
        It then calls the `clear_results_2D` method to clear the results and plot.

        Args:
            sc: The Matplotlib canvas object used for plotting.
        """
        self.edit_axis_a.clear()
        self.edit_axis_b.clear()
        self.edit_centerX.clear()
        self.edit_centerY.clear()

        # Clears results and the plot using a helper function
        self.clear_results_2D(sc)