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
    QIcon,
    QRegExpValidator,
)  

import matplotlib
matplotlib.use('Qt5Agg')

import matplotlib.patches as patches

import SquareCalc
import Canvas
import SaveFig
from Shape import *


class WindowSquare(QWidget, ShapeFunctionality):
    """
    This class represents the main window of the square calculation application.

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
        # Create a Matplotlib canvas for plotting the square
        sc = Canvas.MplCanvas(self, width=6, height=6, dpi=100)
        self.setWindowIcon(QIcon('D:\\Programovani\\Python\\naucse\\PyQtMathApp\\Shape_ico.png'))

        # Button to solve and plot the square
        self.buttonplotSquare = QPushButton('Solve and Plot')
        self.buttonplotSquare.clicked.connect(lambda: self.plot_square(sc, self.combo_color.currentText()))
        self.buttonplotSquare.setToolTip("Solve and plot picture")

        # Button to export the graph as an image
        self.buttonPicture = QPushButton('Graph Export')
        self.buttonPicture.clicked.connect(lambda: SaveFig.save_fig(self, self.fig, 'Square.png'))
        self.buttonPicture.setEnabled(False)
        self.buttonPicture.setToolTip("Save graph as picture")
        
        # Button to export data to Excel 
        self.buttonExport = QPushButton('Excel Export')
        self.buttonExport.clicked.connect(lambda: self.export_excel('Square'))
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
        self.setFixedSize(850, 448)

        hbox1 = QHBoxLayout()
        
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.buttonplotSquare)
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
        self.setWindowTitle('Square')


        # validators - regular expression
        validator_possitive = QRegExpValidator(QtCore.QRegExp(r'([1-9][0-9]{0,6})|([1-9][0-9]{0,6}[.])|([0][.][0-9]{1,6})|([1-9]{1,6}[.][0-9]{1,6})'))
        validator_double = QRegExpValidator(QtCore.QRegExp(r'([-][1-9][0-9]{0,6})|([-][1-9][0-9]{0,6}[.])|([-][0][.][0-9]{1,6})|([-][1-9]{1,6}[.][0-9]{1,6})|([1-9][0-9]{0,6})|([1-9][0-9]{0,6}[.])|([0][.][0-9]{1,6})|([1-9]{1,6}[.][0-9]{1,6})'))
        

        # Create input field for side
        self.label_side = QLabel("Side Length (a):")
        self.label_side.setAlignment(QtCore.Qt.AlignLeft)
        self.label_side.setFixedWidth(150)
        layout_param.addWidget(self.label_side,0,0)

        self.edit_side = QLineEdit(self)
        self.edit_side.setValidator(validator_possitive)
        self.edit_side.setAlignment(QtCore.Qt.AlignRight)
        self.edit_side.setFixedWidth(150)
        layout_param.addWidget(self.edit_side,0,1)

        self.label_dim_side = QLabel("cm")
        self.label_dim_side.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_side.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_side,0,2)

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


        self.label_combo_color = QLabel("Square Color:")
        self.label_combo_color.setAlignment(QtCore.Qt.AlignLeft)
        self.label_combo_color.setFixedWidth(150)
        layout_param.addWidget(self.label_combo_color,3,0)

        # Create combo for color
        self.combo_color = self.custom_combo()
        layout_param.addWidget(self.combo_color,3,1)
        
        # Create field for result - Circumference (c)
        self.label_perimeter = QLabel("Circumference (c):")
        self.label_perimeter.setAlignment(QtCore.Qt.AlignLeft)
        self.label_perimeter.setFixedWidth(150)
        layout_res.addWidget(self.label_perimeter,0,0)

        self.label_res_perimeter = QLabel('0.0')
        self.label_res_perimeter.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_perimeter.setFixedWidth(150)
        self.label_res_perimeter.setFixedHeight(20)
        layout_res.addWidget(self.label_res_perimeter,0,1)

        self.label_dim_per = QLabel("cm")
        self.label_dim_per.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_per.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_per,0,2)

        # Create field for result - Area (A)# Create field for result - Area (A)
        self.label_area = QLabel("Area (A):")
        self.label_area.setAlignment(QtCore.Qt.AlignLeft)
        self.label_area.setFixedWidth(150)
        layout_res.addWidget(self.label_area,1,0)

        self.label_res_area = QLabel('0.0')
        self.label_res_area.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_area.setFixedWidth(150)
        self.label_res_area.setFixedHeight(20)
        layout_res.addWidget(self.label_res_area,1,1)

        self.label_dim_area = QLabel("cm<sup>2</sup>")
        self.label_dim_area.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_area.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_area,1,2)

        # Solve and plot picture - button in the top toolbar
        self.solveAction = QAction(self)
        self.solveAction.setToolTip("Solve and plot picture")
        self.solveAction.setIcon(QIcon('CalculateIcon.svg'))
        self.solveAction.triggered.connect(lambda: self.plot_square(sc, self.combo_color.currentText()))
        toolbar.addAction(self.solveAction)

        # Export graph as PNG - button in the top toolbar
        self.exportPictAction = QAction(self)
        self.exportPictAction.setToolTip("Save graph as picture")
        self.exportPictAction.setIcon(QIcon('SavePictureIcon.svg'))
        self.exportPictAction.triggered.connect(lambda: SaveFig.save_fig(self, self.fig, 'Square.png'))
        self.exportPictAction.setEnabled(False)
        toolbar.addAction(self.exportPictAction)

        # Export inputs, results and graph into Excel file - button in the top toolbar
        self.exportXlsxAction = QAction(self)
        self.exportXlsxAction.setToolTip("Export input data, results\nand graph into Excel")
        self.exportXlsxAction.setIcon(QIcon('ExportXLSIcon.svg'))
        self.exportXlsxAction.triggered.connect(lambda: self.export_excel('Square'))
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



        self.edit_side.textChanged.connect(self.check_state_rad_and_set_color)
        self.edit_side.textChanged.connect(lambda: self.clear_results_2D(sc))
        self.edit_side.textChanged.emit(self.edit_side.text())

        self.edit_centerX.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerX.textChanged.connect(lambda: self.clear_results_2D(sc))
        self.edit_centerX.textChanged.emit(self.edit_centerX.text())

        self.edit_centerY.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerY.textChanged.connect(lambda: self.clear_results_2D(sc))
        self.edit_centerY.textChanged.emit(self.edit_centerY.text())



    def plot_square(self, square_plot, square_color):
        """
        Plots a square on the provided Matplotlib figure and updates display elements.

        This method performs the following actions:
        1. Validates user input for side length and center coordinates (x, y):
        - Displays a custom message box using `self.custom_messagebox` if:
            - Side length is 0, empty, or invalid.
            - X coordinate (x₀) is missing.
            - Y coordinate (y₀) is missing.
        2. If all input is valid:
        - Clears the existing plot on `square_plot`.
        - Creates a `patches.Rectangle` object representing the square with the specified center, side length, and color.
        - Sets the plot's X and Y limits to ensure the entire square is visible.
        - Adds the square to the plot's artist list.
        - Redraws the plot.
        - Updates `self.fig` to reference the Matplotlib figure for potential future use.
        - Calls `self.calculate_square()` to calculate and display square properties.
        - Enables the "Clear" and "Export" buttons for user interaction.

        Args:
            square_plot (matplotlib.pyplot.Figure): The Matplotlib figure to plot the square on.
            square_color (str): The color of the square to be plotted.
        """

        if self.edit_side.text() in ["", "0", "0.", "+", "-"]:
            self.custom_messagebox("Side can be only a possitive number!")

        elif self.edit_centerX.text() in ["", "+", "-"]:
            self.custom_messagebox("X coordinate (x₀) is missing!")

        elif self.edit_centerY.text() in ["", "+", "-"]:
            self.custom_messagebox("Y coordinate (y₀) is missing!")

        else:
            
            square_plot.axes.cla()

            center_x = float(self.edit_centerX.text())
            center_y = float(self.edit_centerY.text())
            side_length = float(self.edit_side.text())

            square = patches.Rectangle((center_x - side_length / 2, center_y - side_length / 2), 
                side_length,
                side_length,
                    edgecolor=square_color,
                facecolor=square_color,
                )
            minus_x = center_x - side_length
            plus_x = center_x + side_length
            minus_y = center_y - side_length
            plus_y = center_y + side_length

            square_plot.axes.set_xlim(minus_x, plus_x)
            square_plot.axes.set_ylim(minus_y, plus_y)

            square_plot.axes.add_patch(square)
            square_plot.draw()

            self.fig = square_plot.figure
            self.calculate_square()
            
            self.clearAction.setEnabled(True)
            self.buttonClear.setEnabled(True)
            self.exportPictAction.setEnabled(True)
            self.buttonPicture.setEnabled(True)
            self.exportXlsxAction.setEnabled(True)
            self.buttonExport.setEnabled(True)


    def calculate_square(self):
        """
        Calculates the perimeter and area of a square.

        This method retrieves the side length of a square from the user interface,
        creates a `SquareCalc.Square` object, calculates the square's perimeter
        and area rounded to five decimal places, and updates the corresponding
        labels with the results.

        Raises:
            ValueError: If the entered side length is not a valid number.
        """

        try:
            side_square = float(self.edit_side.text())
        except ValueError:
            raise ValueError("Please enter a valid numeric value for the side length.")

        mySquare = SquareCalc.Square(side_square)
        square_perimeter = round(mySquare.circumference(),5)
        square_area = round(mySquare.area(),5)

        self.label_res_perimeter.setText(str(square_perimeter))
        self.label_res_area.setText(str(square_area))

        
    def clear_inputs(self, sc):
        """
        Clears input fields.

        This method clears the text in the side, x coordinate, and y coordinate fields.
        It then calls the `clear_results_2D` method to clear the results and plot.

        Args:
            sc: The Matplotlib canvas object used for plotting.
        """
        self.edit_side.clear()
        self.edit_centerX.clear()
        self.edit_centerY.clear()

        # Clears results and the plot using a helper function
        self.clear_results_2D(sc)