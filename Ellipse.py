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


from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse

import numpy as np

import EllipseCalc

import Canvas


class WindowEllipse(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        sc = Canvas.MplCanvas(self, width=6, height=6, dpi=100)

        buttonplotEllipse = QPushButton('Plot Ellipse')
        buttonplotEllipse.clicked.connect(lambda: self.plot_ellipse(sc, self.combo_color.currentText()))
        buttonClear = QPushButton('Clear')
        buttonClear.clicked.connect(lambda: self.clear_inputs(sc))
        buttonClose = QPushButton('Close')
        buttonClose.clicked.connect(self.close)

        self.setFixedSize(800, 405)

        hbox1 = QHBoxLayout()
        
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(buttonplotEllipse)
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
        self.setWindowTitle('Ellipse')  

        validator_double = QDoubleValidator()
        validator_possitive = QRegExpValidator(QtCore.QRegExp(r'([1-9][0-9]{0,6})|([0][.][0-9]{1,6})|([1-9]{1,6}[.][0-9]{1,6})'))

        self.label_axis_a = QLabel("Semi-major axis a:")
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


        self.label_axis_b = QLabel("Semi-minor axis b:")
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


        self.label_centerX = QLabel("Center - X coord.:")
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

        self.label_centerY = QLabel("Center - Y coord.:")
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


        self.combo_color = QComboBox(self)
        self.combo_color.addItem("green")
        self.combo_color.addItem("red")
        self.combo_color.addItem("blue")
        self.combo_color.addItem("orange")
        self.combo_color.setFixedWidth(150)
        self.combo_color.setFixedHeight(28)
        layout_param.addWidget(self.combo_color,4,1)
        

        self.label_perimeter = QLabel("Ellipse Perimeter:")
        self.label_perimeter.setAlignment(QtCore.Qt.AlignLeft)
        self.label_perimeter.setFixedWidth(150)
        layout_res.addWidget(self.label_perimeter,0,0)

        self.label_res_perimeter = QLabel('0.0')
        self.label_res_perimeter.setStyleSheet("background-color : white; color : darkblue")
        self.label_res_perimeter.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_perimeter.setFixedWidth(150)
        layout_res.addWidget(self.label_res_perimeter,0,1)

        self.label_dim_per = QLabel("cm")
        self.label_dim_per.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_per.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_per,0,2)


        self.label_area = QLabel("Ellipse  Area:")
        self.label_area.setAlignment(QtCore.Qt.AlignLeft)
        self.label_area.setFixedWidth(150)
        layout_res.addWidget(self.label_area,1,0)

        self.label_res_area = QLabel('0.0')
        # self.label_res_area.setFont(QFont('Arial', 12))
        self.label_res_area.setStyleSheet("background-color : white; color : darkblue")
        self.label_res_area.setAlignment(QtCore.Qt.AlignRight)
        self.label_res_area.setFixedWidth(150)
        layout_res.addWidget(self.label_res_area,1,1)

        self.label_dim_area = QLabel("cm<sup>2</sup>")
        self.label_dim_area.setAlignment(QtCore.Qt.AlignLeft)
        self.label_dim_area.setFixedWidth(30)
        layout_res.addWidget(self.label_dim_area,1,2)


        self.edit_axis_a.textChanged.connect(self.check_state_axis_a)
        self.edit_axis_a.textChanged.emit(self.edit_axis_a.text())

        self.edit_axis_b.textChanged.connect(self.check_state_axis_b)
        self.edit_axis_b.textChanged.emit(self.edit_axis_b.text())

        self.edit_centerX.textChanged.connect(self.check_state_centerX)
        self.edit_centerX.textChanged.emit(self.edit_centerX.text())

        self.edit_centerY.textChanged.connect(self.check_state_centerY)
        self.edit_centerY.textChanged.emit(self.edit_centerY.text())



    def plot_ellipse(self, ellipse_plot, ellipse_color):
        
        ellipse_plot.axes.cla()
        ellipse_plot.draw()
        self.label_res_area.setText("0.0")
        self.label_res_perimeter.setText("0.0")
        

        if self.edit_axis_a.text() == "0" or self.edit_axis_a.text() == "":
            QMessageBox.about(self, 'Error','Major axis can be only a possitive number')

        elif self.edit_axis_b.text() == "0" or self.edit_axis_b.text() == "":
            QMessageBox.about(self, 'Error','Minor axis can be only a possitive number')

        elif self.edit_centerX.text() == "":
            QMessageBox.about(self, 'Error','Center - X coord. is missing')

        elif self.edit_centerY.text() == "":
            QMessageBox.about(self, 'Error','Center - Y coord. is missing')

        else:

            Drawing_colored_ellipse = Ellipse((float(self.edit_centerX.text()),(float(self.edit_centerY.text()))),2*float(self.edit_axis_a.text()),2*float(self.edit_axis_b.text()))
            Drawing_colored_ellipse.set_color(ellipse_color)

            minus_x = float(self.edit_centerX.text())-2*float(self.edit_axis_a.text())
            plus_x = float(self.edit_centerX.text())+2*float(self.edit_axis_a.text())
            minus_y = float(self.edit_centerY.text())-2*float(self.edit_axis_b.text())
            plus_y = float(self.edit_centerY.text())+2*float(self.edit_axis_b.text())

            ellipse_plot.axes.set_xlim(minus_x, plus_x)
            ellipse_plot.axes.set_ylim(minus_y, plus_y)

            ellipse_plot.axes.add_artist(Drawing_colored_ellipse)
            ellipse_plot.draw()

            self.calculate_ellipse()

    def calculate_ellipse(self):

        axis_a = float(self.edit_axis_a.text())
        axis_b = float(self.edit_axis_b.text())
        myEllipse = EllipseCalc.Elipsa(axis_a, axis_b)
        ellipse_perimeter = round(myEllipse.obvod(),5)
        ellipse_area = round(myEllipse.obsah(),5)

        self.label_res_perimeter.setText(str(ellipse_perimeter))
        self.label_res_area.setText(str(ellipse_area))


    def clear_inputs(self, sc):
        sc.axes.cla()
        sc.draw()
        self.edit_axis_a.clear()
        self.edit_axis_b.clear()
        self.edit_centerX.clear()
        self.edit_centerY.clear()
        self.label_res_area.setText("0.0")
        self.label_res_perimeter.setText("0.0")


    def check_state_axis_a(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if self.edit_axis_a.text() == "0" or self.edit_axis_a.text() == "":
            color = '#f6989d' # red
        elif state == QValidator.Acceptable:
            color = '#c4df9b' # green
        elif state == QValidator.Intermediate:
            color = '#fff79a' # yellow
        else:
            color = '#f6989d' # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)


    def check_state_axis_b(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if self.edit_axis_b.text() == "0" or self.edit_axis_b.text() == "":
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
    

        


        