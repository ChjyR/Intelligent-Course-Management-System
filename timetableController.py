import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtCore import QTimer
from Ui_table import Ui_Timetable
from Ui_coursepageGUI import Ui_Form
from functionList import DatabaseCursor
import time

class MyMainForm(QMainWindow, Ui_Timetable):
    def __init__(self, student_ID, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.login_time = time.time()
        #print(time.ctime(self.login_time))
        self.setupUi(self)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.student_ID = student_ID
        self.label.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Welcome, {student_ID}!</span></p></body></html>")
        self.label_3.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Login Time: {time.strftime('%H:%M:%S',time.localtime(self.login_time))}</span></p></body></html>")
        self.dbcursor = DatabaseCursor("Haoyun0916")
        self.personal_info = self.dbcursor.personal_info(self.student_ID)
        self.auto_notice = {}

        course_info = self.dbcursor.classList(self.student_ID)
        buttons = [self.courseButton1,self.courseButton2,self.courseButton3,self.courseButton4,self.courseButton5,self.courseButton6]
        
        for i in range(len(buttons)):
            buttons[i].setVisible(False)

        self.visible_buttons = []
        self.courses = []
        for i in range(len(course_info)):
            buttons[i].setVisible(True)
            buttons[i].setText(course_info[i][0]+course_info[i][1])
            self.courses.append(course_info[i][0]+course_info[i][1])
            self.visible_buttons.append(buttons[i])

        # print(courses)
        timetable = self.dbcursor.timetable(self.student_ID)
        #print(timetable)
        courseDay = []
        for course in timetable:
            if course[2] == 'Mon': day = 1
            elif course[2] == 'Tue': day = 2
            elif course[2] == 'Wed': day = 3
            elif course[2] == 'Thu': day = 4
            elif course[2] == 'Fri': day = 5
            elif course[2] == 'Sat': day = 6
            elif course[2] == 'Sun': day = 7
            start = course[3].seconds//3600 - 8
            end = course[4].seconds//3600 - 8
            for hour in range(start,end):
                courseDay.append((day,hour,self.courses.index(course[0]+course[1])))
                self.auto_notice[course[0]+course[1]+course[2]] = False
        #print(courseDay)
        
        
        # courses = []
        # for i in range(len(buttons)):
        #     buttons[i].setVisible(False)
        # course2id = dict()
        # for i in range(len(course_info)):
        #     buttons[i].setVisible(True)
        #     buttons[i].setText(course_info[i][0]+course_info[i][1])
        #     course2id[course_info[i][0]+course_info[i][1]] = i
        #     courses.append(course_info[i][0]+course_info[i][1])
        # print(courses)

        #courseDay = [(1,4,'COMP3278A'), (4,4,'COMP3278A'), (4,5,'COMP3278A'), (5,0,'COMP3297A')] # test data
        
        COLOR = ['lightcoral', 'sandybrown', 'gold', 'lightgreen', 'mediumturquoise', 'skyblue']

        for i in range(len(buttons)):
            buttons[i].setStyleSheet(f'background-color:{COLOR[i]}')

        for i in range(len(courseDay)):
            item = self.table.item(courseDay[i][1],courseDay[i][0])
            item.setBackground(QBrush(QColor(COLOR[courseDay[i][2]])))
        
        self.coursePages = []
        #print(buttons[0].text())
        for button in self.visible_buttons:
            self.coursePages.append(courseForm(button.text(),self.personal_info))
            button.clicked.connect(self.coursePages[-1].open)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_check)

    def update_check(self):
        course_in_1h = self.dbcursor.withinTF(self.student_ID)
        for course in course_in_1h:
            self.showCourse.setText(f"<html><head/><body><p align=\"center\">{course[0]}{course[1]}</p></body></html>")
            if not self.auto_notice[course[0]+course[1]+course[10]]:
                self.coursePages[self.courses.index(course[0]+course[1])].open()
                self.auto_notice[course[0]+course[1]+course[10]] = True
        if not course_in_1h:
            self.showCourse.setText(f"<html><head/><body><p align=\"center\">(None)</p></body></html>")

    def open(self):
        self.timer.start(3000)
        self.show()

    def closeEvent(self, event):
        
        login_t = time.localtime(self.login_time)
        login_th = time.strftime("%H:%M:%S",login_t)
        duration = time.time()-self.login_time
        login_day = time.strftime("%Y-%m-%d",login_t)
        self.dbcursor.record_timestamp(self.student_ID,login_th,login_day,duration)
        event.accept()



        

class courseForm(QMainWindow, Ui_Form):
    def __init__(self, course_ID, personal_information, parent=None):

        super(courseForm, self).__init__(parent)
        self.setupUi(self)
        self.dbcursor = DatabaseCursor("Haoyun0916")
        courseInfo = self.dbcursor.detailedInfo(course_ID[:-1],course_ID[-1])
        time_string = ""

        for time_slot in courseInfo[9]:
            time_string += f"{time_slot[0]} {time_slot[1]} - {time_slot[2]}\t"
        
        
        #courseName = [course_ID, courseInfo[2]] # test data
        self.title.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#0000c0;\">{course_ID} {courseInfo[2]}</span></p></body></html>")
        
        self.teacher_msg.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">{courseInfo[5]}</span></p></body></html>")
        self.description_link.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><a href=\"{courseInfo[3]}\">Description_link</span></p></body></html>")
        self.description_link.setOpenExternalLinks(True)

        self.Materials_link.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><a href=\"{courseInfo[8]}\">Materials_link</span></p></body></html>")
        self.Materials_link.setOpenExternalLinks(True)

        self.notes_link.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><a href=\"{courseInfo[7]}\">Notes_link</span></p></body></html>")
        self.notes_link.setOpenExternalLinks(True)

        self.time_address.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">{courseInfo[4]}   {time_string}</span></p></body></html>")

        self.zoom_link.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\"><a href=\"{courseInfo[6]}\">Zoom_link</span></p></body></html>")

        self.zoom_link.setStyleSheet('background-color: mediumaquamarine')
        self.zoom_link.setOpenExternalLinks(True)
        
        self.email_button.clicked.connect(lambda:self.sendInfo(courseInfo, personal_information))

    def sendInfo(self, info, email):
        # print(info)
        # print(email)
        import send_email
        send_email.send_email(email[0][-1],info)


    def open(self):
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainPage = MyMainForm(3035233527)
    mainPage.open()
    sys.exit(app.exec_())
