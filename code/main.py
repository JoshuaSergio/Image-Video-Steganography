from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow
import mainencode, maindecode
import os, shutil

class Ui_MainWindow(object):
    
    def __init__(self, a):

        self.a = a

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(105, 193, 185, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(175, 40, 451, 91))
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 36pt \"Microsoft Sans Serif\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.button1 = QtWidgets.QPushButton(self.widget)
        self.button1.setGeometry(QtCore.QRect(295, 270, 211, 51))
        self.button1.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(0, 148, 158);\n"
"font: 18pt \"Georgia\";\n"
"color:rgb(255, 255, 255);\n"
"")
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(self.widget)
        self.button2.setGeometry(QtCore.QRect(295, 370, 211, 51))
        self.button2.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(0, 148, 158);\n"
"font: 18pt \"Georgia\";\n"
"color:rgb(255, 255, 255);")
        self.button2.setObjectName("button2")
        self.label2 = QtWidgets.QLabel(self.widget)
        self.label2.setGeometry(QtCore.QRect(180, 130, 451, 21))
        self.label2.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 18pt \"Microsoft Sans Serif\";")
        self.label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.widget)
        self.label3.setGeometry(QtCore.QRect(180, 160, 451, 21))
        self.label3.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 18pt \"Microsoft Sans Serif\";")
        self.label3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label3.setObjectName("label3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(305, 550, 191, 16))
        self.label_4.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.button3 = QtWidgets.QPushButton(self.widget)
        self.button3.setGeometry(QtCore.QRect(20, 520, 81, 31))
        self.button3.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(80, 148, 158);\n"
"font: 14pt \"Georgia\";\n"
"color:rgb(255, 255, 255);")
        self.button3.setObjectName("button3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Client-side Steganography"))
        self.button1.setText(_translate("MainWindow", "Penyisipan"))
        self.button2.setText(_translate("MainWindow", "Ekstraksi"))
        self.label2.setText(_translate("MainWindow", "Implementasi Steganografi Least Significant Bit pada"))
        self.label3.setText(_translate("MainWindow", "Citra Digital ke dalam Video"))
        self.label_4.setText(_translate("MainWindow", "Credit. Chrisna Joshua Sergio"))
        self.button3.setText(_translate("MainWindow", "Exit"))

        self.button1.clicked.connect(self.encodepage)
        self.button2.clicked.connect(self.decodepage)
        self.button3.clicked.connect(self.exit)
    
    def encodepage(self):
        self.mainwin=QMainWindow()  
        self.ui=mainencode.Ui_Dialog(self.mainwin) 
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setWindowTitle("LSB Encode")
        self.mainwin.show() 
        self.a.hide()

    def decodepage(self):
        self.mainwin=QMainWindow()  
        self.ui=maindecode.Ui_Dialog(self.mainwin) 
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setWindowTitle("LSB Decode")
        self.mainwin.show() 
        self.a.hide()

    def clean_tmp(self, path="./tmp-stegano"):
        if os.path.exists(path):
           shutil.rmtree(path)
           print("[INFO] tmp files are cleaned up")

    def exit(self):
        self.clean_tmp()
        quit() 


"""def init():

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Video Steganography")
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":

    init()"""


