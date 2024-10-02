import sys
from PyQt6.QtWidgets import QApplication, QWidget
class ventanaVacia(QWidget):
    
    def __init__(self):
        super().__init__()
        self.InicializarUI()
        
    def InicializarUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Mi primera ventana")
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ventanaVacia()
    sys.exit(app.exec())