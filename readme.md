## Intelligent Course Management System

This sorftware is a course management system that uses a face recognition to login.



[TOC]

### How to use

#### Setup

1. install packages

```shell
pip install opencv-python
pip install opencv-contrib-python
pip install mysql-connector-python
pip install PyQt5 
pip install --upgrade Pillow
pip install numpy
```

2. Train face classifier

```shell
python face_capture.py #(your user_id here)#
python train.py
```

3. Add your personal information

Open `3278_test_data.sql` and add corresponding personal info into Student table and Subclass table.

4. Create database

```shell
mysql -u root -p #(your mysql password)# < 3278_Tables.sql
mysql -u root -p #(your mysql password)# < 3278_test_data.sql
```

5. Set query function with your mysql password

Open `functionList.py` and change mysql_password in line 4 to your password



#### Run project

1. Execute the following under the project path: 

```shell
python GROUP_Project.py
```

2. Either write your user_id and click the cat for facial login, or write your user_id and password for password login

<img src="resourses\img1.png" alt="img1" style="zoom: 67%;" />

3. If login successful, the software will show a course table and course information if it is starting within 1 hour. This course information page can also be opened by clicking the colored button at the left. 

   Clicking the link will redirect to corresponding webpage. Clicking `Send Email` , the system will automaticly send a email.

<img src="resourses\img1.png" alt="img2" style="zoom:67%;" />

