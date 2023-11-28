#Para inicializar una ventana en python de QT5 comandos basicos
import sys
import os 
from PyQt5 import uic, QtWidgets

# Ruta absoluta al archivo UI e Inicializa las ventanas
qtCreatorFile = os.path.join(os.path.dirname(__file__), "Procesador2.ui")
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow): 
    
    def link (self):
        print('Conectar')

    def unplug (self):
        print('Desconectar')
    
    def start (self):
        print('Iniciar')

    def stop (self):
        print('Parar')


    def __init__(self): 
        QtWidgets.QMainWindow.__init__(self) 
        Ui_MainWindow.__init__(self) 
        self.setupUi(self) 

        self.Conectar.clicked.connect(self.link)
        self.Desconectar.clicked.connect(self.unplug)
        self.Iniciar.clicked.connect(self.start)
        self.Pausar.clicked.connect(self.stop)
        




        self.show()

if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv) 
    window = MyApp() 
    app.exec_()
