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


from matplotlib import pyplot as plt
import pandas as pd

import CircleCalc
import Canvas
import SaveFig
from Shape import *
from CustomCombo import *

class WindowCircle(QWidget, ShapeFunctionality):
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

        # Button to solve and plot the circle
        self.buttonplotCircle = QPushButton('Solve and Plot')
        self.buttonplotCircle.clicked.connect(lambda: self.plot_circle(sc, self.combo_color.currentText()))
        self.buttonplotCircle.setToolTip("Solve and plot picture")

        # Button to export the graph as an image
        self.buttonPicture = QPushButton('Graph Export')
        self.buttonPicture.clicked.connect(lambda: SaveFig.save_fig(self, self.fig, 'Circle.png'))
        self.buttonPicture.setEnabled(False)
        
        # Button to export data to Excel 
        self.buttonExport = QPushButton('Excel Export')
        self.buttonExport.clicked.connect(lambda: self.export_excel())
        self.buttonExport.setEnabled(False)
                
        # Button to clear all inputs, results, and the graph
        self.buttonClear = QPushButton('Clear')
        self.buttonClear.clicked.connect(lambda: self.clear_inputs(sc))
        self.buttonClear.setEnabled(False)
        
        # Button to close the window
        self.buttonClose = QPushButton('Close')
        self.buttonClose.clicked.connect(self.close)

        # Create a toolbar for frequently used actions
        toolbar = QToolBar()
        toolbar.setIconSize(QtCore.QSize(50, 50))

        # Set the window size
        self.setFixedSize(850, 448)

        hbox1 = QHBoxLayout()
        
        
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.buttonplotCircle)
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
        self.setWindowTitle('Circle')  

        # validators - regular expression
        validator_positive = QRegExpValidator(QtCore.QRegExp(r'([1-9][0-9]{0,6})|([0])|([0][.][1-9][0-9]{0,6})|([1-9][0-9]{0,6}[.][1-9][0-9]{0,6})'))
        validator_double = QRegExpValidator(QtCore.QRegExp(r'([-][1-9][0-9]{0,6})|([-][1-9][0-9]{0,6}[.])|([-][0][.][0-9]{1,6})|([-][1-9]{1,6}[.][0-9]{1,6})|([1-9][0-9]{0,6})|([1-9][0-9]{0,6}[.])|([0][.][0-9]{1,6})|([1-9]{1,6}[.][0-9]{1,6})'))

        # Create input field for radius
        self.label_radius = QLabel("Radius (r):")
        self.label_radius.setAlignment(QtCore.Qt.AlignLeft)
        self.label_radius.setFixedWidth(150)
        layout_param.addWidget(self.label_radius,0,0)

        self.edit_radius = QLineEdit(self)
        self.edit_radius.setValidator(validator_positive)
        self.edit_radius.setAlignment(QtCore.Qt.AlignRight)
        self.edit_radius.setFixedWidth(150)
        layout_param.addWidget(self.edit_radius,0,1)

        self.label_dim_radius = QLabel("cm")
        self.label_dim_radius.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_radius.setFixedWidth(30)
        layout_param.addWidget(self.label_dim_radius,0,2)

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


        self.label_combo_color = QLabel("Circle Color:")
        self.label_combo_color.setAlignment(QtCore.Qt.AlignLeft)
        self.label_combo_color.setFixedWidth(150)
        layout_param.addWidget(self.label_combo_color,3,0)

        # Create combo for color
        self.combo_color = custom_combo(self)
        layout_param.addWidget(self.combo_color,3,1)
        
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
        self.label_res_area.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_area.setFixedWidth(150)
        layout_res.addWidget(self.label_res_area,1,1)

        self.label_dim_area = QLabel("cm<sup>2</sup>")
        self.label_dim_area.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_area.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_area,1,2)

        
        # Solve and plot picture - button in the top toolbar
        self.exportPictAction = QAction(self)
        self.exportPictAction.setToolTip("Solve and plot picture")
        self.exportPictAction.setIcon(QIcon('CalculateIcon.svg'))
        self.exportPictAction.triggered.connect(lambda: self.plot_circle(sc, self.combo_color.currentText()))
        toolbar.addAction(self.exportPictAction)

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
        self.exportXlsxAction.triggered.connect(self.export_excel)
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

        self.edit_radius.textChanged.connect(self.check_state_rad_and_set_color)
        self.edit_radius.textChanged.connect(lambda: self.clear_results(sc))
        self.edit_radius.textChanged.emit(self.edit_radius.text())

        self.edit_centerX.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerX.textChanged.connect(lambda: self.clear_results(sc))
        self.edit_centerX.textChanged.emit(self.edit_centerX.text())
        
        self.edit_centerY.textChanged.connect(self.check_state_and_set_color)
        self.edit_centerY.textChanged.connect(lambda: self.clear_results(sc))
        self.edit_centerY.textChanged.emit(self.edit_centerY.text())

        self.combo_color.currentIndexChanged.connect(lambda: self.clear_results(sc))


    def plot_circle(self, circle_plot, circle_color):

        circle_plot.axes.cla()
        circle_plot.draw()
        self.label_res_area.setText("0.0")
        self.label_res_perimeter.setText("0.0")
        

        if self.edit_radius.text() in ["", "0", "0.", "+", "-"]:
            self.custom_messagebox("Radius can be only a positive number!")

        elif self.edit_centerX.text() in ["", "+", "-"]:
            self.custom_messagebox("X coordinate (x₀) is missing!")

        elif self.edit_centerY.text() in ["", "+", "-"]:
            self.custom_messagebox("Y coordinate (y₀) is missing!")

        else:
            Drawing_colored_circle = plt.Circle((float(self.edit_centerX.text()),(float(self.edit_centerY.text()))),float(self.edit_radius.text()))
            Drawing_colored_circle.set_color(circle_color)

            minus_x = float(self.edit_centerX.text())-2*float(self.edit_radius.text())
            plus_x = float(self.edit_centerX.text())+2*float(self.edit_radius.text())
            minus_y = float(self.edit_centerY.text())-2*float(self.edit_radius.text())
            plus_y = float(self.edit_centerY.text())+2*float(self.edit_radius.text())

            circle_plot.axes.set_xlim(minus_x, plus_x)
            circle_plot.axes.set_ylim(minus_y, plus_y)

            circle_plot.axes.add_artist(Drawing_colored_circle)
            
            circle_plot.draw()

            self.fig = circle_plot.figure
            
            self.calculate_circle()
            self.clearAction.setEnabled(True)
            self.buttonClear.setEnabled(True)
            self.exportPictAction.setEnabled(True)
            self.buttonPicture.setEnabled(True)
            self.exportXlsxAction.setEnabled(True)
            self.buttonExport.setEnabled(True)

    def calculate_circle(self):

        radius_circle = float(self.edit_radius.text())
        myCircle = CircleCalc.Circle(radius_circle)
        circle_perimeter = round(myCircle.circumference(),5)
        circle_area = round(myCircle.area(),5)

        self.label_res_perimeter.setText(str(circle_perimeter))
        self.label_res_area.setText(str(circle_area))


    def clear_inputs(self, sc):
        """
        Clears all inputs, results, and the graph.

        This method clears the text in the radius, x coordinate, and y coordinate
        fields, as well as the result fields for circumference, and area.
        It also clears the plot on the Matplotlib canvas.

        Args:
            sc: The Matplotlib canvas object used for plotting.
        """
        sc.axes.cla()
        sc.draw()
        self.edit_radius.clear()
        self.edit_centerX.clear()
        self.edit_centerY.clear()
        self.label_res_area.setText("0.0")
        self.label_res_perimeter.setText("0.0")
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
        self.label_res_area.setText("0.0")
        self.label_res_perimeter.setText("0.0")
        self.clearAction.setEnabled(False)
        self.exportPictAction.setEnabled(False)
        self.buttonPicture.setEnabled(False)
        self.exportXlsxAction.setEnabled(False)
        self.buttonExport.setEnabled(False)
        self.buttonClear.setEnabled(False)

    def export_excel(self):

        # Get custom filename from user
        file_name, _ = QFileDialog.getSaveFileName(self, 'Export to Excel', os.path.join(os.getcwd(), 'Results', 'circle.xlsx'), 'Excel (*.xlsx)')

        if not file_name:
            return  # User canceled the file selection dialog

        try:
            # Create Pandas DataFrame objects
            data = {
            'Property': [self.label_radius.text(),
                        self.label_centerX.text(),
                        self.label_centerY.text()],
            'Value': [float(self.edit_radius.text()), 
                    float(self.edit_centerX.text()),
                    float(self.edit_centerY.text())],
            'Unit': ['cm', 
                    'cm',
                    'cm']
            }

            results = {
            'Result': [self.label_perimeter.text(),
                        self.label_area.text()],
            'Value': [float(self.label_res_perimeter.text()), 
                    float(self.label_res_area.text())],
            'Unit': ['cm', 
                    'cm^2']
            }

            df = pd.DataFrame(data)
            df_res = pd.DataFrame(results)

            # Create Excel writer with custom filename
            writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
            workbook = writer.book
            worksheet = workbook.add_worksheet('Circle Calculation')

            # Define header format with background color
            header_format = workbook.add_format({
                'bg_color': '#EAF1FF',
                'bold': True,
                'align': 'center',
                'valign': 'vcenter',
                'border': 1
            })

            # Write data to Excel
            df.to_excel(writer, sheet_name='Circle Calculation', startrow=0, startcol=0, index=False)
            df_res.to_excel(writer, sheet_name='Circle Calculation', startrow=5, startcol=0, index=False)
            for col_idx, col in enumerate(df.columns):
                worksheet.write(0, col_idx, col, header_format)

            # Save the image (assuming self.fig is a Matplotlib figure)
            self.fig.savefig(f'.\\Results\\circle_plot.png')  # Adjust path if needed
            worksheet.insert_image('F2', f'.\\Results\\circle_plot.png')  # Adjust cell location if needed
            for col_idx, col in enumerate(df_res.columns):
                worksheet.write(5, col_idx, col, header_format)

            writer.close()

            QMessageBox.information(self, 'Success', 'Data exported to Excel successfully.')

        except Exception as e:
            QMessageBox.warning(self, 'Error', f'An error occurred while exporting the data: {e}')