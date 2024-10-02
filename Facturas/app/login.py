import sys
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit, QPushButton, QMessageBox, QCheckBox)
from PyQt6.QtGui import QFont, QPixmap
from conexionDB import cursor1
from conexionDB import conexion1
from conexionDB import psycopg2
from conexionDB import bcrypt

class login(QWidget):
    
    def __init__(self):
        super().__init__()
        self.InicializarUI()
        
    def InicializarUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("Sistema de Facturación")
        self.generarLogin()
        self.show()
    
    def generarLogin(self):
        self.is_logged = False

        userLabel = QLabel(self)
        userLabel.setText("Usuario:")
        userLabel.setFont(QFont("Arial", 12))
        userLabel.move(20, 20)

        self.userImput = QLineEdit(self)
        self.userImput.resize(100, 30)
        self.userImput.move(120, 20)

        passwordLabel = QLabel(self)
        passwordLabel.setText("Contraseña:")
        passwordLabel.setFont(QFont("Arial", 12))
        passwordLabel.move(20, 60)

        self.passwordInput = QLineEdit(self)
        self.passwordInput.resize(100, 30)
        self.passwordInput.move(120, 60)
        self.passwordInput.setEchoMode(
            QLineEdit.EchoMode.Password
        )
        self.buttonViewPassword = QPushButton("Ver Contraseña", self)
        self.buttonViewPassword.move(230, 70)
        self.buttonViewPassword.setCheckable(True)
        self.buttonViewPassword.toggled.connect(self.viewPassword)

        loginButton = QPushButton("Login", self)
        loginButton.move(120, 100)
        loginButton.clicked.connect(self.login)


    def viewPassword(self,clicked):
        if clicked:
            self.passwordInput.setEchoMode(
            QLineEdit.EchoMode.Normal
        )
            self.buttonViewPassword.setText("Ocultar Contraseña")
        else:
            self.passwordInput.setEchoMode(
            QLineEdit.EchoMode.Password
        )
            self.buttonViewPassword.setText("Ver Contraseña")


    def login(self):
        try:
            password = self.passwordInput.text().encode()
            sql = "select * from users where usuario = %s"
            user = self.userImput.text()
            cursor1.execute(sql, (user,))
            resultado = cursor1.fetchone()

            if resultado is None:
                QMessageBox.warning(self, "Error", 
                                "El usuario no existe",
                                QMessageBox.StandardButton.Close, 
                                QMessageBox.StandardButton.Close)
            else:
                resultado_encoded = resultado[2].encode() 
                if bcrypt.checkpw(password, resultado_encoded):
                    QMessageBox.information(self, "Login", 
                                        "Login Correcto", 
                                        QMessageBox.StandardButton.Ok, 
                                        QMessageBox.StandardButton.Ok)
                    self.is_logged = True
                    self.close()
                    self.openMainWindow()
                else:
                    QMessageBox.warning(self, "Error", 
                                    "Credenciales incorrectas",
                                    QMessageBox.StandardButton.Close, 
                                    QMessageBox.StandardButton.Close)
        except psycopg2.Error:
            QMessageBox.critical(self, "Error", 
                             "Error en la conexión con la base de datos",
                             QMessageBox.StandardButton.Close, 
                             QMessageBox.StandardButton.Close)
            



            

    def openMainWindow(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = login()
    sys.exit(app.exec())
 