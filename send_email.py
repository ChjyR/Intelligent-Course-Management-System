import smtplib
import sys
from email.message import EmailMessage

def send_email(mail_addr,course_info):
    """function to send a email.

    Args:
        mail_addr (str): Target email address.
        list of tuple(10): corresponding info is:
            0: course_id, 1: sub_class_id,
            2: course_name 
            3:discription, 4: classroom_address,
            5: teacher_msg, 6: link,
            7: notes, 8: materials,
            9: [(week_day, start_time, end_time)*n]
    """    
    sender = 'dbproj2348@hotmail.com'   # A hotmail account used to send email.
    passwd = 'coursework2022'

    content = f"""
*Hi, this is the course information*

Course: {course_info[0]} {course_info[1]} {course_info[2]}

<Course Description> 
{course_info[3]}

<Classroom Address>
{course_info[4]}
<Teacher's Message>
{course_info[5]}

<Zoom link>
{course_info[6]}
<Note> 
{course_info[7]}
<Related Materials>
{course_info[8]}

Have a nice day!

*this is system generated message, please do not reply*
"""
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = f'Course Info of {course_info[0]} {course_info[1]} {course_info[2]}'
    msg['From'] = sender
    msg['To'] = mail_addr
    #try:
    with smtplib.SMTP('smtp-mail.outlook.com',587) as host:
        host.starttls()
        host.login(sender,passwd)
        host.send_message(msg,sender,mail_addr)
    #except:
    #    print("Error: unable to send email.")
    #    print(f"{sys.exc_info()[1]}")

if __name__ == '__main__':
    # send_email('u3600103@connect.hku.hk','Hello world')
    test_content = ("id",'sub','course','address','teahcer','link','note','material')
    send_email('harry666@connect.hku.hk',test_content)