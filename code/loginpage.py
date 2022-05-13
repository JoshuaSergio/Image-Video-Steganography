from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QLineEdit
import main
import hashlib


class Ui_Dialog(object):

    def __init__(self, a):

        self.a = a

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(801, 581)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(105, 193, 185, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(175, 40, 451, 91))
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 36pt \"Microsoft Sans Serif\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label_2")
        self.button1 = QtWidgets.QPushButton(self.widget)
        self.button1.setGeometry(QtCore.QRect(280, 450, 241, 35))
        self.button1.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(0, 148, 158);\n"
"font: 18pt \"Georgia\";\n"
"color:rgb(255, 255, 255);")
        self.button1.setObjectName("button1_2")
        self.label2 = QtWidgets.QLabel(self.widget)
        self.label2.setGeometry(QtCore.QRect(180, 130, 451, 21))
        self.label2.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 18pt \"Microsoft Sans Serif\";")
        self.label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label2.setObjectName("label2_2")
        self.label3 = QtWidgets.QLabel(self.widget)
        self.label3.setGeometry(QtCore.QRect(180, 160, 451, 21))
        self.label3.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 18pt \"Microsoft Sans Serif\";")
        self.label3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label3.setObjectName("label3_2")
        self.label4 = QtWidgets.QLabel(self.widget)
        self.label4.setGeometry(QtCore.QRect(305, 550, 191, 16))
        self.label4.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";")
        self.label4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label4.setObjectName("label_5")
        self.button2 = QtWidgets.QPushButton(self.widget)
        self.button2.setGeometry(QtCore.QRect(20, 530, 81, 31))
        self.button2.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(80, 148, 158);\n"
"font: 14pt \"Georgia\";\n"
"color:rgb(255, 255, 255);")
        self.button2.setObjectName("button2_2")
        self.label5 = QtWidgets.QLabel(self.widget)
        self.label5.setGeometry(QtCore.QRect(280, 220, 241, 61))
        self.label5.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 24pt \"Microsoft Sans Serif\";")
        self.label5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label5.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 300, 241, 35))
        self.lineEdit.setStyleSheet("border-radius: 15px; background:white; color:rgb(0,0,0);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setPlaceholderText("Masukkan username")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit2.setGeometry(QtCore.QRect(280, 360, 241, 35))
        self.lineEdit2.setStyleSheet("border-radius: 15px; background:white; color:rgb(0,0,0);")
        self.lineEdit2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit2.setPlaceholderText("Masukkan password")
        self.lineEdit2.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit2.setObjectName("lineEdit2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Client-side Steganography"))
        self.button1.setText(_translate("Dialog", "Login"))
        self.label2.setText(_translate("Dialog", "Implementasi Steganografi Least Significant Bit pada"))
        self.label3.setText(_translate("Dialog", "Citra Digital ke dalam Video"))
        self.label4.setText(_translate("Dialog", "Credit: Chrisna Joshua Sergio"))
        self.button2.setText(_translate("Dialog", "Exit"))
        self.label5.setText(_translate("Dialog", "Sign in to Continue"))

        self.button1.clicked.connect(self.Login)
        self.button2.clicked.connect(self.exit)

    def sanitizeName(self, userName):
        userName = userName.split()
        userName = '-'.join(userName)
        return userName

    def hash_password(self, password):
        return hashlib.sha256(str.encode(password)).hexdigest()

    def check_password_hash(self, password, hash):
        return self.hash_password(password) == hash

    def Login(self):
        usersInfo = {}
        with open('db.txt', 'r') as file:
            for line in file:
                line = line.split()
                usersInfo.update({line[0]: line[1]})

        self.userName = self.lineEdit.text()
        self.userName = self.sanitizeName(self.userName)
        userPassword = self.lineEdit2.text()

        if self.userName not in usersInfo:
            print("[INFO] Incorrect username or password!")
            return(self.incorrectmessage())
        elif not self.check_password_hash(userPassword, usersInfo[self.userName]):
            print("[INFO] Incorrect username or password!")
            return(self.incorrectmessage())
        else:
            print("[INFO] Log in Success!")
            self.successmessage()
            self.mainmenu()

    
    def incorrectmessage(self):
        popup = QMessageBox()
        popup.setWindowTitle("Incorrect Username or Password")
        popup.setText("Username atau password yang dimasukkan salah! Silahkan coba lagi.")
        popup.setIcon(QMessageBox.Icon.Warning)
        popup.setStandardButtons(QMessageBox.StandardButton.Close)

        #popup.buttonClicked.connect(self.mainmenu)

        show = popup.exec()
    
    def successmessage(self):
        popup = QMessageBox()
        popup.setWindowTitle("Incorrect Username or Password")
        popup.setText("Login berhasil! Selamat datang " + self.userName)
        popup.setIcon(QMessageBox.Icon.Information)
        popup.setStandardButtons(QMessageBox.StandardButton.Close)

        #popup.buttonClicked.connect(self.mainmenu)

        show = popup.exec()
    
    def exit(self):
        quit()

    def mainmenu(self):
        self.mainwin=QMainWindow()  
        self.ui=main.Ui_MainWindow(self.mainwin) 
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setWindowTitle("Video Steganography")
        self.mainwin.show() 
        self.a.hide() 

def init():

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Video Steganography")
    MainWindow.setFocus()
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":

    init()