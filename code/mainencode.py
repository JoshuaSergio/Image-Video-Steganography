from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QFileDialog
from PIL import Image
from Crypto.Cipher import AES
import main, encoderesult
import os, shutil
import cv2
from timeit import default_timer as timer
import numpy as np
from subprocess import call,STDOUT

MAX_COLOR_VALUE = 256
MAX_BIT_VALUE = 8

class Ui_Dialog(object):

    def __init__(self, a):
        self.a = a

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(812, 581)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 821, 581))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(105, 193, 185, 255), stop:1 rgba(255, 255, 255, 255))}\n"
"")
        self.widget.setObjectName("widget")
        self.button = QtWidgets.QPushButton(self.widget)
        self.button.setGeometry(QtCore.QRect(320, 140, 171, 41))
        self.button.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(0, 148, 158);\n"
"font: 14pt \"Microsoft Sans MS\";\n"
"color:rgb(255, 255, 255);")
        self.button.setObjectName("button")
        self.label2 = QtWidgets.QLabel(self.widget)
        self.label2.setGeometry(QtCore.QRect(80, 190, 661, 20))
        self.label2.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";")
        self.label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label2.setObjectName("label2")
        self.button2 = QtWidgets.QPushButton(self.widget)
        self.button2.setGeometry(QtCore.QRect(320, 260, 171, 41))
        self.button2.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(0, 148, 158);\n"
"font: 14pt \"Microsoft Sans MS\";\n"
"color:rgb(255, 255, 255);")
        self.button2.setObjectName("button2")
        self.label3 = QtWidgets.QLabel(self.widget)
        self.label3.setGeometry(QtCore.QRect(80, 310, 661, 20))
        self.label3.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";")
        self.label3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(self.widget)
        self.label4.setGeometry(QtCore.QRect(75, 388, 661, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label4.setFont(font)
        self.label4.setStyleSheet("color:rgb(0, 148, 158);\n"
"font: 16pt \"Microsoft Sans Serif\";")
        self.label4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label4.setObjectName("label4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(255, 420, 301, 31))
        self.lineEdit.setStyleSheet("border-radius: 15px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(75, 50, 661, 41))
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 30pt \"Microsoft Sans Serif\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.button3 = QtWidgets.QPushButton(self.widget)
        self.button3.setGeometry(QtCore.QRect(320, 510, 171, 41))
        self.button3.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(0, 169, 218);\n"
"font: 14pt \"Microsoft Sans MS\";\n"
"color:rgb(255, 255, 255);")
        self.button3.setObjectName("button3")
        self.button4 = QtWidgets.QPushButton(self.widget)
        self.button4.setGeometry(QtCore.QRect(20, 30, 91, 31))
        self.button4.setStyleSheet("border-top-left-radius :15px;\n"
"border-top-right-radius : 5px; \n"
"border-bottom-left-radius : 15px; \n"
"border-bottom-right-radius : 5px;\n"
"background-color:rgb(0, 169, 218);\n"
"font: 12pt \"Microsoft Sans MS\";\n"
"color:rgb(255, 255, 255);")
        self.button4.setObjectName("button4")
        self.label5 = QtWidgets.QLabel(self.widget)
        self.label5.setGeometry(QtCore.QRect(80, 470, 661, 41))
        self.label5.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";")
        self.label5.setText("")
        self.label5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label5.setObjectName("label5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button.setText(_translate("Dialog", "Choose Image File"))
        self.label2.setText(_translate("Dialog", "*Pilih citra digital yang akan disisipkan kedalam video (.jpg/.jpeg)"))
        self.button2.setText(_translate("Dialog", "Choose Video File"))
        self.label3.setText(_translate("Dialog", "*Pilih video yang akan digunakan sebagai media penampung (.mp4)"))
        self.label4.setText(_translate("Dialog", "Password Enkripsi"))
        self.label.setText(_translate("Dialog", "Penyisipan Citra Digital ke Video"))
        self.button3.setText(_translate("Dialog", "Submit"))
        self.button4.setText(_translate("Dialog", "Back"))

        self.checkimg = True
        self.checkvid = True

        self.button.clicked.connect(self.chooseimage)
        self.button2.clicked.connect(self.choosevideo)
        self.button3.clicked.connect(self.lsbencrypt)
        self.button4.clicked.connect(self.mainmenu)

    def create_image(self, data, resolution): #buat image berdasarkan data
        image = Image.new("RGB", resolution)
        image.putdata(data)

        return image

    def remove_n_lsb(self, value, n): #fungsi hapus n lsb
        value = value >> n 
        return value << n

    def get_n_lsb(self, value, n): #fungsi ambil n lsb
        value = value << MAX_BIT_VALUE - n
        value = value % MAX_COLOR_VALUE
        return value >> MAX_BIT_VALUE - n

    def get_n_msb(self, value, n): #fungsi ambil n msb
        return value >> MAX_BIT_VALUE - n

    def messageToBinary(self, message): #fungsi konversi ke biner
        if type(message) == str:
                return ''.join([ format(ord(i), "08b") for i in message ])
        elif type(message) == bytes or type(message) == np.ndarray:
                return [ format(i, "08b") for i in message ]
        elif type(message) == int or type(message) == np.uint8:
                return format(message, "08b")
        else:
                raise TypeError("[INFO] input type not supported")

    def frame_extraction(self, video): #fungsi ekstraki frame video
        if os.path.exists("./tmp-stegano"):
                shutil.rmtree("./tmp-stegano")
                print("[INFO] tmp folder detected, deleting tmp folder")
             
        os.makedirs("tmp-stegano")
        temp_folder="./tmp-stegano"
        print("[INFO] tmp-stegano directory is created")

        vidcap = cv2.VideoCapture(video)
        count = 0

        while True:
                success, image = vidcap.read()
                if not success:
                        break
                cv2.imwrite(os.path.join(temp_folder, "{:d}.png".format(count)), image) 
                count += 1
        print("[INFO] done frame extraction (total {} frames)".format(count))

    def encrypt(self, password): #fungsi enkripsi

        while len(password) % 16 != 0:
                password += "$"

        key = password.encode('utf-8')
        iv = b'0000000000000000'
        img = cv2.imread(self.image_with_background_path)
        
        if img.size % 16 > 0: #padding
                row = img.shape[0]
                pad = 16 - (row % 16)  
                img = np.pad(img, ((0, pad), (0, 0), (0, 0)))  
                img[-1, -1, 0] = pad  

        img_bytes = img.tobytes() 
        enc_img_bytes = AES.new(key, AES.MODE_CBC, iv).encrypt(img_bytes) 
        enc_img = np.frombuffer(enc_img_bytes, np.uint8).reshape(img.shape)
        cv2.imwrite('tmp-stegano/enc_img.png', enc_img)
        print("[INFO] done encrypt")

    def encode0(self, image_to_hide, image_to_hide_in, n_bits):

        width, height = image_to_hide.size #ukuran citra

        #load citra rgb
        hide_image = image_to_hide.load()
        hide_in_image = image_to_hide_in.load()

        data = []
        
        for y in range(height):
                for x in range(width):
                        r_hide, g_hide, b_hide = hide_image[x,y] 

                        #get MSB citra
                        r_hide = self.get_n_msb(r_hide, n_bits)
                        g_hide = self.get_n_msb(g_hide, n_bits)
                        b_hide = self.get_n_msb(b_hide, n_bits)

                        r_hide_in, g_hide_in, b_hide_in = hide_in_image[x,y] 

                        #remove LSB frame
                        r_hide_in = self.remove_n_lsb(r_hide_in, n_bits)
                        g_hide_in = self.remove_n_lsb(g_hide_in, n_bits)
                        b_hide_in = self.remove_n_lsb(b_hide_in, n_bits)
                

                        #gabung MSB citra dan LSB frame
                        data.append((r_hide + r_hide_in, 
                                     g_hide + g_hide_in,
                                     b_hide + b_hide_in))

        print("[INFO] done encode frame 0")
        return self.create_image(data, image_to_hide.size)

    def encode1(self, image_to_hide, image_to_hide_in, n_bits):

        width, height = image_to_hide.size #get image size

        #load image
        hide_image = image_to_hide.load()
        hide_in_image = image_to_hide_in.load()

        data = []
        
        for y in range(height):
                for x in range(width):

                        r_hide, g_hide, b_hide = hide_image[x,y] #get image rgb

                        #get rgb for n MSB in img1
                        r_hide = self.get_n_lsb(r_hide, n_bits)
                        g_hide = self.get_n_lsb(g_hide, n_bits)
                        b_hide = self.get_n_lsb(b_hide, n_bits)

                        r_hide_in, g_hide_in, b_hide_in = hide_in_image[x,y] #get image rgb


                        #remove n LSB in img2
                        r_hide_in = self.remove_n_lsb(r_hide_in, n_bits)
                        g_hide_in = self.remove_n_lsb(g_hide_in, n_bits)
                        b_hide_in = self.remove_n_lsb(b_hide_in, n_bits)
                        

                        #combine the img1 MSB to img2 LSB
                        data.append((r_hide + r_hide_in, 
                                        g_hide + g_hide_in,
                                        b_hide + b_hide_in))

        print("[INFO] done encode frame 1")
        return self.create_image(data, image_to_hide.size)

    def encode2(self, img, string):
        string += "#####" #penambahan pembatas

        data_index = 0
        bin_string = self.messageToBinary(string)
        data_len = len(bin_string)

        for values in img:
            for pixel in values:
                #konversi RGB ke biner
                r, g, b = self.messageToBinary(pixel)
                #proses LSB jika masih ada data yang tersisa
                if data_index < data_len:
                        #penyisipan data ke LSB piksel R
                        pixel[0] = int(r[:-1] + bin_string[data_index], 2)
                        data_index += 1
                if data_index < data_len:
                        #penyisipan data ke LSB piksel G
                        pixel[1] = int(g[:-1] + bin_string[data_index], 2)
                        data_index += 1
                if data_index < data_len:
                        #penyisipan data ke LSB piksel B
                        pixel[2] = int(b[:-1] + bin_string[data_index], 2)
                        data_index += 1
                #jika data habis, break
                if data_index >= data_len:
                        break
        
        print("[INFO] done encode frame 2")
        cv2.imwrite(self.frame2_path, img)

    def clean_tmp(self, path="./tmp-stegano"): #fungsi hapus folder temp
        if os.path.exists(path):
           shutil.rmtree(path)
           print("[INFO] tmp files are cleaned up")
    
    def chooseimage(self): #fungsi validasi image
        self.image_file = QFileDialog.getOpenFileName(os.getenv("Desktop"))

        try:

            Image.open(self.image_file[0])
            self.label2.setText(self.image_file[0])
            self.image_to_hide_path = self.image_file[0]
            self.checkimg = False

        except:

            self.label2.setText("Incorrect file type")
            self.checkimg = True

    def choosevideo(self): #fungsi validasi video
        self.video_file = QFileDialog.getOpenFileName(os.getenv("Desktop"))

        try:
            self.label3.setText(self.video_file[0])
            self.video_path = self.video_file[0]
            self.checkvid = False

            if self.video_path.endswith("mp4") == False:
                self.label3.setText("Incorrect file type")
                self.checkvid = True

        except:
            self.label3.setText("Incorrect file type")
            self.checkvid = True
    
    def lsbencrypt(self):

        #validasi masukan    
        if self.checkimg or self.checkvid:
                return(self.typemessage())
        password = self.lineEdit.text()
        if not password:
                return(self.passmessage1())
        if password.isalnum()==False:
                return(self.passmessage2())

        start = timer()

        n_bits = 4

        #frame extraction
        self.frame_extraction(self.video_path)
        frame0_path = "tmp-stegano/0.png"
        frame1_path = "tmp-stegano/1.png"
        self.frame2_path = "tmp-stegano/2.png"

        image_hide = Image.open(self.image_file[0])
        frame0 = Image.open(frame0_path).convert('RGB')
        frame1 = Image.open(frame1_path).convert('RGB')

        self.image_with_background_path = "tmp-stegano/temp-img.png"

        #resize citra
        fixed_height = frame0.size[1]
        fixed_width = frame0.size[0]
        height_percent = (fixed_height / float(image_hide.size[1]))
        width_percent = (fixed_width / float(image_hide.size[0]))

        if fixed_height > fixed_width:
                height_size = int((float(image_hide.size[1]) * float(width_percent)))
                image = image_hide.resize((fixed_width, height_size))
                str_size = str(fixed_width) + "x" + str(height_size)
        else:
                width_size = int((float(image_hide.size[0]) * float(height_percent)))
                image = image_hide.resize((width_size, fixed_height))
                str_size = str(width_size) + "x" + str(fixed_height)

        img_w, img_h = image.size
        image_to_hide = Image.new('RGB', frame0.size, (0,0,1))
        bg_w, bg_h = image_to_hide.size
        offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
        image_to_hide.paste(image, offset)
        image_to_hide.save(self.image_with_background_path)

        #enkripsi citra
        self.encrypt(password)
        image_encrypt = Image.open('tmp-stegano/enc_img.png')

        #penyisipan LSB
        self.encode0(image_encrypt, frame0, n_bits).save(frame0_path)
        self.encode1(image_encrypt, frame1, n_bits).save(frame1_path)
        frame3 = cv2.imread(self.frame2_path)
        self.encode2(frame3, str_size)

        #penggabungan frame video dan audio
        call(["ffmpeg", "-i", self.video_path, "-q:a", "0", "-map", "a", "tmp-stegano/audio.mp3", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
        print("[INFO] done audio extraction")
        call(["ffmpeg", "-i", "tmp-stegano/%d.png" , "-vcodec", "png", "tmp-stegano/video.mp4", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
        print("[INFO] done combine frames")
        call(["ffmpeg", "-i", "tmp-stegano/video.mp4", "-itsoffset", "0.5", "-i", "tmp-stegano/audio.mp3", "-codec", "copy", "tmp-stegano/output.mp4", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
        print("[INFO] encoding success!")

        end = timer()
        elapsed_time = end - start
        print(f"[INFO] Waktu diperlukan pada proses enkripsi adalah {elapsed_time} s")
        self.result()

    def typemessage(self):
        popup = QMessageBox()
        popup.setWindowTitle("Invalid Type")
        popup.setText("Format file invalid, tidak dapat melakukan penyisipan!")
        popup.setIcon(QMessageBox.Icon.Warning)
        popup.setStandardButtons(QMessageBox.StandardButton.Close)

        popup.buttonClicked.connect(self.mainmenu)

        show = popup.exec()

    def passmessage1(self):
        popup = QMessageBox()
        popup.setWindowTitle("Password Empty")
        popup.setText("Password tidak boleh kosong! Gagal melakukan penyisipan.")
        popup.setIcon(QMessageBox.Icon.Warning)
        popup.setStandardButtons(QMessageBox.StandardButton.Close)

        popup.buttonClicked.connect(self.mainmenu)

        show = popup.exec()

    def passmessage2(self):
        popup = QMessageBox()
        popup.setWindowTitle("Password Empty")
        popup.setText("Password harus terdiri dari huruf dan angka saja tanpa spasi! Gagal melakukan penyisipan.")
        popup.setIcon(QMessageBox.Icon.Warning)
        popup.setStandardButtons(QMessageBox.StandardButton.Close)

        popup.buttonClicked.connect(self.mainmenu)

        show = popup.exec()
    
    def result(self):
        self.mainwin=QMainWindow()  
        self.ui=encoderesult.Ui_Dialog(self.mainwin) 
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setWindowTitle("LSB Encode")
        self.mainwin.show() 
        self.a.hide()
        
    def mainmenu(self):
        self.mainwin=QMainWindow()  
        self.ui=main.Ui_MainWindow(self.mainwin) 
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setWindowTitle("Video Steganography")
        self.mainwin.show() 
        self.a.hide()
