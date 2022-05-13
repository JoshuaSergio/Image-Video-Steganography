from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PyQt6.QtGui import QPixmap
import os, shutil
import main


class Ui_Dialog(object):

    def __init__(self, a):
        self.a = a

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(821, 581)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 821, 581))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(105, 193, 185, 255), stop:1 rgba(255, 255, 255, 255))}\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(75, 50, 661, 41))
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 30pt \"Microsoft Sans Serif\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(self.widget)
        self.label2.setGeometry(QtCore.QRect(550, 490, 181, 41))
        self.label2.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";")
        self.label2.setText("")
        self.label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label2.setObjectName("label2")
        self.button1 = QtWidgets.QPushButton(self.widget)
        self.button1.setGeometry(QtCore.QRect(290, 480, 241, 71))
        self.button1.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(0, 148, 158);\n"
"font: 14pt \"Microsoft Sans MS\";\n"
"color:rgb(255, 255, 255);")
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(self.widget)
        self.button2.setGeometry(QtCore.QRect(20, 30, 101, 31))
        self.button2.setStyleSheet("border-top-left-radius :15px;\n"
"border-top-right-radius : 5px; \n"
"border-bottom-left-radius : 15px; \n"
"border-bottom-right-radius : 5px;\n"
"background-color:rgb(0, 169, 218);\n"
"font: 12pt \"Microsoft Sans MS\";\n"
"color:rgb(255, 255, 255);")
        self.button2.setObjectName("button2")
        self.image_preview = QtWidgets.QLabel(self.widget)
        self.image_preview.setGeometry(QtCore.QRect(80, 120, 661, 321))
        self.image_preview.setText("")
        self.image_preview.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.image_preview.setObjectName("image_preview")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Hasil Ekstraksi Citra Digital"))
        self.button1.setText(_translate("Dialog", "Simpan ke penyimpanan lokal"))
        self.button2.setText(_translate("Dialog", "Main Menu"))
        self.showimage()

        self.button1.clicked.connect(self.saveimage)
        self.button2.clicked.connect(self.mainmenu)
    
    def showimage(self):
        self.image_path = "tmp-stegano/output-extraction.png"
        self.pixmap = QPixmap(self.image_path)
        self.image_preview.setPixmap(self.pixmap)
        self.image_preview.setScaledContents(True)
    
    def saveimage(self):
        file_name = QFileDialog.getSaveFileName(None, "Save file", "", "Images (*.png)")[0]
        if file_name=="":
            print("Saving file cancelled")
            return None
        shutil.copyfile(self.image_path, file_name)
        print("[INFO] image saved to local storage")
        self.message()

    def message(self):
        popup = QMessageBox()
        popup.setWindowTitle("Image Saved")
        popup.setText("Citra berhasil disimpan pada penyimpanan lokal")
        popup.setIcon(QMessageBox.Icon.Information)
        popup.setStandardButtons(QMessageBox.StandardButton.Close)

        popup.buttonClicked.connect(self.mainmenu)

        show = popup.exec()
    
    def clean_tmp(self, path="./tmp-stegano"):
        if os.path.exists(path):
           shutil.rmtree(path)
           print("[INFO] tmp files are cleaned up")

    def mainmenu(self):
        self.clean_tmp()
        self.mainwin=QMainWindow()  
        self.ui=main.Ui_MainWindow(self.mainwin) 
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setWindowTitle("Video Steganography")
        self.mainwin.show() 
        self.a.hide()