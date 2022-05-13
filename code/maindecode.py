from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QMessageBox
from PyQt6.QtWidgets import QFileDialog
from PIL import Image
from Crypto.Cipher import AES
import main, decoderesult
import os, shutil
from timeit import default_timer as timer
import cv2
import numpy as np

MAX_COLOR_VALUE = 256
MAX_BIT_VALUE = 8

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
        self.button = QtWidgets.QPushButton(self.widget)
        self.button.setGeometry(QtCore.QRect(320, 190, 171, 41))
        self.button.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(0, 148, 158);\n"
"font: 14pt \"Microsoft Sans MS\";\n"
"color:rgb(255, 255, 255);")
        self.button.setObjectName("button")
        self.label2 = QtWidgets.QLabel(self.widget)
        self.label2.setGeometry(QtCore.QRect(80, 240, 661, 20))
        self.label2.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";")
        self.label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.widget)
        self.label3.setGeometry(QtCore.QRect(75, 318, 661, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color:rgb(0, 148, 158);\n"
"font: 16pt \"Microsoft Sans Serif\";")
        self.label3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label3.setObjectName("label3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(255, 350, 301, 31))
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
        self.button2 = QtWidgets.QPushButton(self.widget)
        self.button2.setGeometry(QtCore.QRect(320, 510, 171, 41))
        self.button2.setStyleSheet("border-radius:15px;\n"
"background-color:rgb(0, 169, 218);\n"
"font: 14pt \"Microsoft Sans MS\";\n"
"color:rgb(255, 255, 255);")
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.widget)
        self.button3.setGeometry(QtCore.QRect(20, 30, 91, 31))
        self.button3.setStyleSheet("border-top-left-radius :15px;\n"
"border-top-right-radius : 5px; \n"
"border-bottom-left-radius : 15px; \n"
"border-bottom-right-radius : 5px;\n"
"background-color:rgb(0, 169, 218);\n"
"font: 12pt \"Microsoft Sans MS\";\n"
"color:rgb(255, 255, 255);")
        self.button3.setObjectName("button3")
        self.label4 = QtWidgets.QLabel(self.widget)
        self.label4.setGeometry(QtCore.QRect(80, 459, 661, 41))
        self.label4.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 13pt \"Microsoft Sans Serif\";")
        self.label4.setText("")
        self.label4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label4.setObjectName("label4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button.setText(_translate("Dialog", "Choose Video File"))
        self.label2.setText(_translate("Dialog", "*Pilih video-stego yang akan diekstraksi (.mp4)"))
        self.label3.setText(_translate("Dialog", "Password Enkripsi"))
        self.label.setText(_translate("Dialog", "Ekstraksi Citra Digital dari Video"))
        self.button2.setText(_translate("Dialog", "Submit"))
        self.button3.setText(_translate("Dialog", "Back"))

        self.button.clicked.connect(self.choosevideo)
        self.button2.clicked.connect(self.lsbdecrypt)
        self.button3.clicked.connect(self.mainmenu)
    
    def create_image(self, data, resolution): #buat image berdasarkan data
        image = Image.new("RGB", resolution)
        image.putdata(data)

        return image

    def get_n_lsb(self, value, n): #fungsi ambil n lsb
        value = value << MAX_BIT_VALUE - n
        value = value % MAX_COLOR_VALUE
        return value >> MAX_BIT_VALUE - n

    def create_8bits_value(self, value, n): #fungsi merubah menjadi 8-bit
        return value << MAX_BIT_VALUE - n
    
    def messageToBinary(self, message): #fungsi konversi ke biner
        if type(message) == str:
                return ''.join([ format(ord(i), "08b") for i in message ])
        elif type(message) == bytes or type(message) == np.ndarray:
                return [ format(i, "08b") for i in message ]
        elif type(message) == int or type(message) == np.uint8:
                return format(message, "08b")
        else:
                raise TypeError("Input type not supported")

    def frame_extraction(self, video): #fungsi ekstraksi frame video
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
    
    def decrypt(self, password): #fungsi dekripsi
    
        while len(password) % 16 != 0:
            password += "$"

        key = password.encode('utf-8')
        iv = b'0000000000000000'

        enc_img = cv2.imread(self.decoded_path)
        dec_img_bytes = AES.new(key, AES.MODE_CBC, iv).decrypt(enc_img.tobytes())
        dec_img = np.frombuffer(dec_img_bytes, np.uint8).reshape(enc_img.shape)

        if dec_img[-1, -1, 0] < 16: #remove padding
            pad = int(dec_img[-1, -1, 0])  
            dec_img = dec_img[0:-pad, :, :].copy()  

        cv2.imwrite(self.output_path, dec_img)
        print("[INFO] done decrypt")
    
    def decode(self, image_to_decode0, image_to_decode1, n_bits):
        width, height = image_to_decode0.size #ukuran citra

        #load citra rgb
        encoded_image = image_to_decode0.load()
        encoded_image1 = image_to_decode1.load()

        data = []

        for y in range(height):
            for x in range(width):

                r_encoded, g_encoded, b_encoded = encoded_image[x,y]
                
                #get LSB frame 1
                r_encoded = self.get_n_lsb(r_encoded, n_bits)
                g_encoded = self.get_n_lsb(g_encoded, n_bits)
                b_encoded = self.get_n_lsb(b_encoded, n_bits)

                #ubah LSB jadi MSB
                r_encoded = self.create_8bits_value(r_encoded, n_bits)
                g_encoded = self.create_8bits_value(g_encoded, n_bits)
                b_encoded = self.create_8bits_value(b_encoded, n_bits)

                r_encoded1, g_encoded1, b_encoded1 = encoded_image1[x,y]
                
                #get LSB frame 2
                r_encoded1 = self.get_n_lsb(r_encoded1, n_bits)
                g_encoded1 = self.get_n_lsb(g_encoded1, n_bits)
                b_encoded1 = self.get_n_lsb(b_encoded1, n_bits)

                #gabung MSB dan LSB
                data.append((r_encoded + r_encoded1, 
                            g_encoded + g_encoded1, 
                            b_encoded + b_encoded1))
                
        print("[INFO] done decode")
        return self.create_image(data, image_to_decode0.size)

    def decode2(self, img):
        bin_data = ""
        for values in img:
            for pixel in values:
                r, g, b = self.messageToBinary(pixel) #konversi RGB ke biner
                bin_data += r[-1] #ekstrak data dari LSB piksel R
                bin_data += g[-1] #ekstrak data dari LSB piksel G
                bin_data += b[-1] #ekstrak data dari LSB piksel B
        
        #bagi data menjadi 8bits
        all_bytes = [ bin_data[i: i+8] for i in range(0, len(bin_data), 8) ]

        #konversi bit ke karakter
        decoded_data = ""
        for byte in all_bytes:
            decoded_data += chr(int(byte, 2))
            if decoded_data[-5:] == "#####": #break saat mencapai pembatas
                break
            
        return decoded_data[:-5] #hapus pembatas
    
    def choosevideo(self):
        self.video_file = QFileDialog.getOpenFileName(os.getenv("Desktop"))

        try:
            self.label2.setText(self.video_file[0])
            self.video_path = self.video_file[0]
            self.checkvid = False

            if self.video_path.endswith("mp4") == False:
                self.label3.setText("Incorrect file type")
                self.checkvid = True

        except:
            self.label3.setText("Incorrect file type")
            self.checkvid = True

    def lsbdecrypt(self):

        #validasi masukan
        if self.checkvid:
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
        frame2_path = "tmp-stegano/2.png"
        self.decoded_path = "tmp-stegano/dec.png"

        #ekstraksi LSB frame 1 dan 2
        image_decode = Image.open(frame0_path).convert('RGB')
        image_decode1 = Image.open(frame1_path).convert('RGB')
        self.decode(image_decode, image_decode1, n_bits).save(self.decoded_path)

        #dekripsi citra
        self.output_path = "tmp-stegano/output-extraction.png"
        self.decrypt(password)

        #ekstraksi LSB frame 3
        resize_size_img = cv2.imread(frame2_path)
        resize_size = self.decode2(resize_size_img)
        print("[INFO] Actual Size:", resize_size)

        #resize citra
        read_img = Image.open(self.output_path)
        decimg_w = read_img.size[0]
        decimg_h = read_img.size[1]

        crop_size = resize_size.split("x")

        if decimg_h > decimg_w :
            height_resize = (decimg_h - int(crop_size[1])) // 2
            left = 0
            up = height_resize
            right = int(crop_size[0]) 
            down = decimg_h - height_resize
        else :
            width_resize = (decimg_w - int(crop_size[0])) // 2
            left = width_resize
            up = 0
            right = decimg_w - width_resize 
            down = int(crop_size[1])

        resized_image = read_img.crop((left, up, right, down))
        resized_image.save(self.output_path)
        print("[INFO] decoding success!")

        end = timer()
        elapsed_time = end - start
        print(f"[INFO] Waktu diperlukan pada proses dekripsi adalah {elapsed_time} s")
        self.result()
    
    def result(self):
        self.mainwin=QMainWindow()  
        self.ui=decoderesult.Ui_Dialog(self.mainwin) 
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setWindowTitle("LSB Encode")
        self.mainwin.show() 
        self.a.hide()
    
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
        popup.setText("Password harus terdiri dari huruf dan angka saja! Gagal melakukan penyisipan.")
        popup.setIcon(QMessageBox.Icon.Warning)
        popup.setStandardButtons(QMessageBox.StandardButton.Close)

        popup.buttonClicked.connect(self.mainmenu)

        show = popup.exec()

    def mainmenu(self):
        self.mainwin=QMainWindow()  
        self.ui=main.Ui_MainWindow(self.mainwin) 
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setWindowTitle("Video Steganography")
        self.mainwin.show() 
        self.a.hide()