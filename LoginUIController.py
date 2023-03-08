from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap, QIcon
from LoginGUI import Ui_LoginGUI
from timetableController import MyMainForm,courseForm
import cv2
import detect
import time
from functionList import DatabaseCursor

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginGUI()
        self.ui.setupUi(self)
        self.setup_control()
        self.detector = detect.Detector()

    def setup_control(self):
        self.img_path = 'resourses\\popo_close.png'
        self.displayImg()
        self.ui.pushButton_Password.clicked.connect(self.passwordButtonClicked)
        self.ui.pushButton_Face.clicked.connect(self.faceButtonClicked)

    def displayImg(self):
        self.img = cv2.imread(self.img_path) # load image form the resource
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(self.qimg)
        self.qpixmap_height = self.qpixmap.height()
        #print(self.ui.pushButton_Face.__dir__())
        self.ui.pushButton_Face.setIcon(QIcon(self.img_path))
        self.ui.pushButton_Face.setIconSize(QtCore.QSize(300,300))
        #self.ui.pushButton_Face.setPixmap(QPixmap.fromImage(self.qimg))

    def passwordButtonClicked(self):
        # get user input from 
        userID = self.ui.lineEdit_UserID.text()
        password = self.ui.lineEdit_Password.text()

        # check empty userID
        if len(userID) == 0:
            self.ui.label_Message.setText('Please input your name')
        # check empty password
        elif len(password) == 0:
            self.ui.label_Message.setText('Please input your password')
        else:
            dbcursor = DatabaseCursor("Haoyun0916")
            result = dbcursor.authenticate(userID, password)
            if result:
                # to next UI
                self.toTable(userID)
            else: 
                self.ui.label_Message.setText("Invalid password or userID, please try again")


    def faceButtonClicked(self):
        userID = self.ui.lineEdit_UserID.text()
        if len(userID) == 0:
            self.ui.label_Message.setText('Please input your name')
            return
        self.ui.label_Message.setText('Please look at your camera')
        #time.sleep(1) # allow user to look at camera
        result = self.detector.detect()
        if result == userID:
            #to next UI
            self.toTable(userID)
        elif result == "timeout":
            self.ui.label_Message.setText("Timeout, please try again")   
        else:
            self.ui.label_Message.setText("Not identified, please try again") 
    
    def toTable(self, userID):
        # keep record of the user
        self.userID = userID
        self.hide()
        # open table
        self.table = MyMainForm(student_ID = userID)
        self.table.open()


