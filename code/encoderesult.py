from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
import main
import os, shutil
from subprocess import call,STDOUT
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime


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
        self.label.setGeometry(QtCore.QRect(90, 150, 661, 41))
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 30pt \"Microsoft Sans Serif\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.button1 = QtWidgets.QPushButton(self.widget)
        self.button1.setGeometry(QtCore.QRect(315, 430, 201, 41))
        self.button1.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(0, 148, 158);\n"
"font: 12pt \"Microsoft Sans MS\";\n"
"color:rgb(255, 255, 255);")
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(self.widget)
        self.button2.setGeometry(QtCore.QRect(270, 250, 291, 131))
        self.button2.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(0, 148, 158);\n"
"font: 18pt \"Microsoft Sans MS\";\n"
"color:rgb(255, 255, 255);")
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.widget)
        self.button3.setGeometry(QtCore.QRect(20, 30, 101, 31))
        self.button3.setStyleSheet("border-top-left-radius :15px;\n"
"border-top-right-radius : 5px; \n"
"border-bottom-left-radius : 15px; \n"
"border-bottom-right-radius : 5px;\n"
"background-color:rgb(0, 169, 218);\n"
"font: 12pt \"Microsoft Sans MS\";\n"
"color:rgb(255, 255, 255);")
        self.button3.setObjectName("button3")
        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Penyisipan Berhasil Dilakukan!"))
        self.button1.setText(_translate("Dialog", "Simpan ke penyimpanan lokal"))
        self.button2.setText(_translate("Dialog", "Upload ke Google Drive"))
        self.button3.setText(_translate("Dialog", "Main Menu"))

        self.button1.clicked.connect(self.localsave)
        self.button2.clicked.connect(self.drivesave)
        self.button3.clicked.connect(self.mainmenu)

    
    def localsave(self):
        file_name = QFileDialog.getSaveFileName(None, "Save file", "", "Video Files (*.mp4)")[0]
        print(file_name)
        if file_name=="":
            print("Saving file cancelled")
            return None
        else:
            call(["ffmpeg", "-i", "tmp-stegano/video.mp4", "-itsoffset", "0.5", "-i", "tmp-stegano/audio.mp3", "-codec", "copy", file_name, "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)     
            print("[INFO] done save to local")
            #tambah buat cancel
            self.localmessage()

    def upload_msg(self):
        return self.statusbar.showMessage("File Uploading...")

    def drivesave(self):
        path = "tmp-stegano/output.mp4"
        now = datetime.now()
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
        title = "output-stegano " + dt

        #self.upload_msg()
        #QApplication.processEvents()
        try:
            gauth = GoogleAuth()
            gauth.LoadCredentialsFile("credential.txt")
            if gauth.credentials is None:
                gauth.LocalWebserverAuth()
            elif gauth.access_token_expired:
                gauth.Refresh()
            else:
                gauth.Authorize()
            gauth.SaveCredentialsFile("credential.txt")

            drive = GoogleDrive(gauth)

            file = drive.CreateFile({'title': title })
            file.SetContentFile(path)

            print("[INFO] Uploading File...")
            file.Upload()
            print("[INFO] File Uploaded to Google Drive")
            self.drivemessage()
        
        except:
            print("[INFO] Uploading Failed!")
            self.errormessage()
    
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
    
    def localmessage(self):
        popup = QMessageBox()
        popup.setWindowTitle("File Saved")
        popup.setText("Video-stego berhasil disimpan pada penyimpanan lokal")
        popup.setIcon(QMessageBox.Icon.Information)
        popup.setStandardButtons(QMessageBox.StandardButton.Close)

        #popup.buttonClicked.connect(self.mainmenu)

        show = popup.exec()

    def drivemessage(self):
        popup = QMessageBox()
        popup.setWindowTitle("File Uploaded")
        popup.setText("Video-stego berhasil disimpan pada penyimpanan Google Drive")
        popup.setIcon(QMessageBox.Icon.Information)
        popup.setStandardButtons(QMessageBox.StandardButton.Close)

        #popup.buttonClicked.connect(self.mainmenu)

        show = popup.exec()
    
    def errormessage(self):
        popup = QMessageBox()
        popup.setWindowTitle("File Uploaded")
        popup.setText("Gagal menghubungkan ke Google Drive. Periksa koneksi internet anda!")
        popup.setIcon(QMessageBox.Icon.Information)
        popup.setStandardButtons(QMessageBox.StandardButton.Close)

        #popup.buttonClicked.connect(self.mainmenu)

        show = popup.exec()