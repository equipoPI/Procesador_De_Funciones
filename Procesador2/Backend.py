#rojo rgb(220,0,0) - #dc0000
#gris rgb(17,17,17) - #111111
#negro rgb(0,0,0) - #000000
#azul verdoso(5,211,170) - #05d3aa

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice, QPoint
from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg 
import numpy as np
import sys

class MyApp(QMainWindow):
    def __inti__(self):
        super(MyApp, self).__init__()
        loadUi('untilted.iu',self)

        self.bt.normal.hide()
        self.click_posicion = QPoint()
        self.bt_minimize.clicked.connect(lambda :self.showMinimized())
        self.bt_normal.clicked.connect(self.control_bt_normal)
        self.bt_maximize.clicked.connect(self.control_bt_maximize)
        self.bt_normal.clicked.connect(lambda :self.close())

        #eliminacion de recuadro original de la pestaña
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #tamaño del Grip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        #movimiento de ventana
        self.frame_superior.mouseMoveEvent = self.move_ventana

        #conrol de coneccion
        self.serial = QSerialPort()
        self.bt_Actualizar.clicked.connect(self.read_ports)
        self.bt_Conectar.clicked.connect(self.serial_connect)
        self.bt_Desconectar.clicked.connect(lambda:self.serial.close())

        self.serial.readyRead.connect(self.read_data)
        
        self.x = list(np.linspace(0,100,100))
        self.y = list(np.linspace(0,0,100))

        #gafica
        pg.setConfigOption('bacground', '#111111')
        pg.setConfigOption('freground', '#dc0000')
        self.plt = pg.PlotWidget(title= 'Grafica')
        self.graph_layout.addWidget(self.plt)

        self.read_ports()
        

   
