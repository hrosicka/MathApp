import sys
from random import randint

from PyQt5.QtWidgets import (
    QApplication,
    QGroupBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QGridLayout,
    QMenuBar,
    QMenu,
    QAction,
)

from PyQt5.QtGui import (
    QPixmap, 
    QIcon,
)

from PyQt5 import QtCore

from Circle import *
from Sphere import *
from Ellipse import *
from Ellipsoid import *
from Square import *
from Cube import *

import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

import numpy as np


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.set_aspect('equal', adjustable='box')
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self._createActions()
        self._createMenuBar()

        self.window1 = WindowCircle()
        self.window2 = WindowSphere()
        self.window3 = WindowEllipse()
        self.window4 = WindowEllipsoid()
        self.window5 = WindowSquare()
        self.window6 = WindowCube()

        self.setWindowTitle('PyQt Math App')

        self.setMinimumWidth(400)
        self.setMinimumHeight(400)

        self.setMaximumWidth(800)
        self.setMaximumHeight(800)

        buttonClose = QPushButton('Close')
        buttonClose.clicked.connect(app.closeAllWindows)

        l = QHBoxLayout()
        l.addStretch(1)
        l.addWidget(buttonClose)

        l2 = QVBoxLayout()

        l3 = QGridLayout()

        l2.addLayout(l3)
        

        self.label = QLabel(self)
        self.pixmap = QPixmap('Shapes.png')
        self.setWindowIcon(QIcon('Shape_ico.png'))
        self.label.setPixmap(self.pixmap)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        l3.addWidget(self.label,0,0,1,2)

        button1 = QPushButton("Circle")
        # button1.setStyleSheet('background-color: rgb(128, 0, 32);\ncolor: rgb(255, 255, 255);')

        button1.clicked.connect(
            lambda checked: self.toggle_window(self.window1)
        )
        l3.addWidget(button1,1,0)

        button2 = QPushButton("Sphere")
        # button2.setStyleSheet('background-color: rgb(128, 0, 32);\ncolor: rgb(255, 255, 255);')

        button2.clicked.connect(
            lambda checked: self.toggle_window(self.window2)
        )
        l3.addWidget(button2,1,1)

        button3 = QPushButton("Ellipse")
        # button3.setStyleSheet('background-color: rgb(128, 0, 32);\ncolor: rgb(255, 255, 255);')

        button3.clicked.connect(
            lambda checked: self.toggle_window(self.window3)
        )
        l3.addWidget(button3,2,0)


        button4 = QPushButton("Ellipsoid")
        # button4.setStyleSheet('background-color: rgb(128, 0, 32);\ncolor: rgb(255, 255, 255);')

        button4.clicked.connect(
            lambda checked: self.toggle_window(self.window4)
        )
        l3.addWidget(button4,2,1)


        button5 = QPushButton("Square")
        # button5.setStyleSheet('background-color: rgb(128, 0, 32);\ncolor: rgb(255, 255, 255);')

        button5.clicked.connect(
            lambda checked: self.toggle_window(self.window5)
        )
        l3.addWidget(button5,3,0)


        button6 = QPushButton("Cube")
        # button6.setStyleSheet('background-color: rgb(128, 0, 32);\ncolor: rgb(255, 255, 255);')

        button6.clicked.connect(
            lambda checked: self.toggle_window(self.window6)
        )
        l3.addWidget(button6,3,1)

        l2.addLayout(l)

        w = QWidget()
        w.setLayout(l2)
        self.setCentralWidget(w)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()


    def _createActions(self):
        # Creating action using the first constructor
        self.closeAction = QAction(self)
        self.closeAction.setText("&Close")
        self.closeAction.triggered.connect(app.closeAllWindows)

        self.circleAction = QAction(self)
        self.circleAction.setText("&Circle")
        self.circleAction.triggered.connect(lambda checked: self.toggle_window(self.window1))

        self.sphereAction = QAction(self)
        self.sphereAction.setText("&Sphere")
        self.sphereAction.triggered.connect(lambda checked: self.toggle_window(self.window2))

        self.ellipseAction = QAction(self)
        self.ellipseAction.setText("&Ellipse")
        self.ellipseAction.triggered.connect(lambda checked: self.toggle_window(self.window3))

        self.ellipsoidAction = QAction(self)
        self.ellipsoidAction.setText("&Ellipsoid")
        self.ellipsoidAction.triggered.connect(lambda checked: self.toggle_window(self.window4))

        self.squareAction = QAction(self)
        self.squareAction.setText("&Square")
        self.squareAction.triggered.connect(lambda checked: self.toggle_window(self.window5))

        self.cubeAction = QAction(self)
        self.cubeAction.setText("&Cube")
        self.cubeAction.triggered.connect(lambda checked: self.toggle_window(self.window6))


    def _createMenuBar(self):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        # Creating menus using a QMenu object
        fileMenu = QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        fileMenu.addAction(self.closeAction)

        # Creating menus using a title
        geometryMenu = menuBar.addMenu("&Geometry")

        menuBar.addMenu(geometryMenu)
        geometryMenu.addAction(self.circleAction)
        geometryMenu.addAction(self.sphereAction)
        geometryMenu.addAction(self.ellipseAction)
        geometryMenu.addAction(self.ellipsoidAction)
        geometryMenu.addAction(self.squareAction)
        geometryMenu.addAction(self.cubeAction)


        helpMenu = menuBar.addMenu("&Help")

    
   
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()