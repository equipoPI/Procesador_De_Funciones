from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout
import pyqtgraph as pg 
import sys

class GUI(QWidget):
    def __init__(self):
         super().__init__()
         self. setWindowTitle('Control SPS')
         self. setStyleSheet('background-color: #00AAAA;')
         self. resize(650, 650)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = GUI()
    my_app.show()
    sys.exit(app.exec_())
    