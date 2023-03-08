# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/rebecca/Desktop/timetableTry/coursepageGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Course Page")
        Form.resize(600, 420)
        self.verticalWidget = QtWidgets.QWidget(Form)
        self.verticalWidget.setGeometry(QtCore.QRect(7, 33, 587, 334))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.verticalWidget)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        
        self.line = QtWidgets.QFrame(self.verticalWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.teacher_msg = QtWidgets.QLabel(self.verticalWidget)
        self.teacher_msg.setObjectName("teacher_msg")
        self.verticalLayout.addWidget(self.teacher_msg)
        self.description_link = QtWidgets.QLabel(self.verticalWidget)
        self.description_link.setOpenExternalLinks(False)
        self.description_link.setObjectName("description_link")
        self.verticalLayout.addWidget(self.description_link)
        self.Materials_link = QtWidgets.QLabel(self.verticalWidget)
        self.Materials_link.setObjectName("Materials_link")
        self.verticalLayout.addWidget(self.Materials_link)
        self.notes_link = QtWidgets.QLabel(self.verticalWidget)
        self.notes_link.setObjectName("notes_link")
        self.verticalLayout.addWidget(self.notes_link)
        self.time_address = QtWidgets.QLabel(self.verticalWidget)
        self.time_address.setObjectName("time_address")
        self.verticalLayout.addWidget(self.time_address)
        self.zoom_link = QtWidgets.QLabel(self.verticalWidget)
        self.zoom_link.setObjectName("zoom_link")
        self.verticalLayout.addWidget(self.zoom_link)
        self.email_button = QtWidgets.QPushButton(Form)
        self.email_button.setObjectName("email")
        self.email_button.setGeometry(QtCore.QRect(470, 380, 113, 32))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Course Page"))
        self.title.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:6pt; font-weight:500; font-style:italic; color:#0000c0;\">course_id &amp;&amp; course_name &amp;&amp; sub_class_id</span></p></body></html>"))
        self.teacher_msg.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">teacher_msg</span></p></body></html>")) 
        self.description_link.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Course Information</span></p></body></html>"))
        self.Materials_link.setText(_translate("Form", "<html><head/><body><p align=\"center\">Materials</p></body></html>"))
        self.notes_link.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">notes</span></p></body></html>"))
        self.time_address.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:500;\">class_time &amp;&amp; classroom_address</span></p></body></html>"))
        self.zoom_link.setText(_translate("Form", "<html><head/><body><p align=\"center\">Zoom</p></body></html>"))
        self.email_button.setText(_translate("Form", "Send Email"))

