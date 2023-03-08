import mysql.connector
import time
# Change the password here in order to connect local mysql 
mysql_password = "123456"

class DatabaseCursor():
    """Aggregate object for database query
    """    
    def __init__(self, password) -> None:
        self.conn = mysql.connector.connect(user='root',password=mysql_password,database='Project3278')
        self.cursor = self.conn.cursor()
            
    def withinTF(self, studentID):
        """if there are classes wihtin 1 hour

        Returns:
            list of tuple(11): corresponding info is:
            0: course_id, 1: sub_class_id,
            2: start_time, 3:course_name, 4:discription,
            5: classroom_address, 6: teacher_msg, 7: link,
            8: notes, 9: materials, 10: week_day
        """
        current_time = time.localtime(time.time())
        clock_time = f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}"

        self.cursor.execute(f"""
            SELECT S.course_id, S.sub_class_id, CT.start_time, C.course_name, C.discription, S.classroom_address, S.teacher_msg, S.link, S.notes, C.materials, CT.week_day
            FROM Course C, Subclass S, ClassTime CT, Take T
            WHERE T.student_id = {studentID} AND
                C.course_id = T.course_id AND
                S.course_id = T.course_id AND
                S.sub_class_id = T.sub_class_id AND
                CT.course_id = T.course_id AND
                CT.sub_class_id = T.sub_class_id AND
                CT.week_day = "{time.asctime(current_time)[0:3]}" AND
                TIMEDIFF(CT.start_time, "{clock_time}") < "1:00:00" AND
                TIMEDIFF(CT.start_time, "{clock_time}") > "0:00:00";
        """)
        values = list(self.cursor)
        return values


    def classList(self, studentID):
        """showing info for specific class in the list

        Returns:
            list of tuple(2): corresponding info is:
            0: course_id, 1: sub_class_id
        """        
        self.cursor.execute(f"""
            SELECT T.course_id, T.sub_class_id 
            FROM Take T 
            WHERE T.student_id = {studentID};
        """)
        values = list(self.cursor)
        return values

    def detailedInfo(self, courseID, subClassID):
        """Course info in detail

        Returns:
            list of tuple(10): corresponding info is:
            0: course_id, 1: sub_class_id,
            2: course_name 
            3:discription, 4: classroom_address,
            5: teacher_msg, 6: link,
            7: notes, 8: materials,
            9: [(week_day, start_time, end_time)*n]
        """        
        self.cursor.execute(f"""
            SELECT S.course_id, S.sub_class_id, C.course_name, C.discription, S.classroom_address, S.teacher_msg, S.link, S.notes, C.materials
            FROM Course C, Subclass S
            WHERE S.course_id = C.course_id AND
                S.course_id = "{courseID}" AND
                S.sub_class_id = "{subClassID}";
        """)
        values = list(*self.cursor)
        self.cursor.execute(f"""
            SELECT CT.week_day, CT.start_time, CT.end_time
            FROM ClassTime CT
            WHERE CT.course_id = "{courseID}" AND
                CT.sub_class_id = "{subClassID}";
        """)
        time = list(self.cursor)
        values.append(time)
        return values


    def timetable(self, studentID):
        """class timetable

        Returns:
            list of tuple(7): corresponding info is:
            0: course_id, 1: sub_class_id,
            2:week_day, 3: start_time,
            4: end_time, 5: start_date,
            6: end_date
        """      
        current_time = time.localtime(time.time())
        date = time.strftime("%Y-%m-%d",current_time)
        self.cursor.execute(f"""
            SELECT CT.course_id, CT.sub_class_id, CT.week_day, CT.start_time, CT.end_time, C.start_date, C.end_date
            FROM ClassTime CT, Take T, Course C
            WHERE T.student_id = {studentID} AND
                CT.course_id = T.course_id AND
                CT.sub_class_id = T.sub_class_id AND
                C.course_id = T.course_id AND
                C.start_date < "{date}" AND
                C.end_date > "{date}";
        """)
        values = list(self.cursor)
        return values

    def record_timestamp(self, student_id, login_time, login_date, duration):
        """record login record

        Args:
            student_id (int): 
            login_time (str): in format "hh:mm:ss" 
            login_date (str): in format "yyyy-MM-dd"
            duration (float): login time in second 
        """    
        self.cursor.execute("SET time_zone='+00:00';")
        self.cursor.execute(f"""
            INSERT INTO Records(student_id, login_time, login_date, duration)
            VALUES ({student_id},"{login_time}","{login_date}",{duration});
        """)
        self.conn.commit()
    
    def authenticate(self, student_id, password):
        """authenticate password

        Args:
            student_id (int): 
            password (str): 

        Returns:
            tuple/bool: tuple of (student_id, name, email)
            or False
        """        
        print(student_id,password)
        print(f"""
            SELECT S.student_id
            FROM Student S
            WHERE S.student_id = {student_id} AND
            S.student_password = "{password}"; 
        """)
        self.cursor.execute(f"""
            SELECT S.student_id
            FROM Student S
            WHERE S.student_id = {student_id} AND
            S.student_password = "{password}"; 
        """)
        values = list(self.cursor)
        if len(values) == 1:
            return values[0]
        return False

    def personal_info(self, student_id):
        """_summary_

        Args:
            student_id (int): _description_
        """        
        self.cursor.execute(f"""
            SELECT student_id, student_name, student_password, email_address
            FROM Student 
            WHERE student_id = {student_id}; 
        """,)

        return list(self.cursor)


    def __del__(self):
        self.conn.close()

if __name__ == '__main__':
    cursor = DatabaseCursor("Haoyun0916")
    cursor.withinTF(3035233527)
    class_id = cursor.classList(3035002978)
    cursor.detailedInfo(*class_id[0])
    cursor.timetable(3035233527)
    cursor.record_timestamp(3035233527,"21:13:00","2022-11-16",14.87)
    cursor.authenticate(3035466731,"OCxQtOYo")