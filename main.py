from tkinter import Button
from turtle import color
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QProgressBar
import sys
import instagram

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setStyleSheet(
            "background:rgb(26, 26, 26)"
        )

        self.progressBar = QProgressBar()

        self.title = QLabel()
        self.title.setText("ITRAGRAM")
        self.title.setStyleSheet(
            """
            color:white;
            font-size:20px;
            font-weight:bold;
            margin-bottom:20px;
            margin-left:240px;
            """
        )

        self.usernameInput = QLineEdit()
        self.usernameInput.setPlaceholderText("Kullanıcı Adı")
        self.usernameInput.setTextMargins(5,5,5,5)
        self.usernameInput.setFixedHeight(30)
        self.usernameInput.setContentsMargins(150,0,150,0)
        self.usernameInput.setStyleSheet("""
            color:rgb(255,255,255);
            background:rgb(100, 100, 100);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;""".format(5)
        )

        self.passwordInput = QLineEdit()
        self.passwordInput.setPlaceholderText("Şifre")
        self.passwordInput.setTextMargins(5,5,5,5)
        self.passwordInput.setFixedHeight(30)
        self.passwordInput.setContentsMargins(150,0,150,0)
        self.passwordInput.setStyleSheet("""
            color:rgb(255,255,255);
            background:rgb(100, 100, 100);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;""".format(5)
        )

        self.logInButton = QPushButton()
        self.designLogInButton()
        self.logInButton.setCheckable(True)
        self.logInButton.clicked.connect(self.logIn)
        
        self.logInAlert = QLabel()
        self.logInAlert.setText("Kullanıcı adı veya parola boş bırakılamaz")
        self.logInAlert.setStyleSheet(
            "color:white"
        )
        self.logInAlert.setVisible(False)
        self.logInAlert.setContentsMargins(210,10,0,0)

        layout = QVBoxLayout()
        layout.addWidget(self.title)
        layout.addWidget(self.usernameInput)
        layout.addWidget(self.passwordInput)
        layout.addWidget(self.logInButton)
        layout.addWidget(self.logInAlert)
        layout.setContentsMargins(0,200,0,0)

        container = QWidget()
        container.setLayout(layout)
        
        self.setMenuWidget(container)

        self.setFixedSize(QSize(600,600))
    
    def the_button_clicked(self):
            print("Okey")

    def logIn(self):
        if(self.usernameInput.text != "" and self.passwordInput.text != ""):
            try:
                instagram.logIn(self.usernameInput.text,self.passwordInput.text)
            except:
                print("Hata")
        else:
            self.logInAlert.setVisible(True)

    def designLogInButton(self):
        self.logInButton.setText("Giriş")
        self.logInButton.setFixedHeight(30)
        self.logInButton.setStyleSheet("""
            color:white;
            margin-right:150px;
            margin-left:150px;
            background:rgb(193, 53, 132);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;""".format(5))

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()