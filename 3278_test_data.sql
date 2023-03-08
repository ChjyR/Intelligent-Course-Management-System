

### Course

INSERT INTO Course (course_id, course_name, materials, start_date, end_date, discription) 
 VALUES ('COMP3230', 'Principles of Operating Systems', 'https://pages.cs.wisc.edu/~remzi/OSTEP/', '2022-09-01', '2022-11-30', 'https://www.cs.hku.hk/index.php/programmes/course-offered?infile=2022/comp3230.html');
INSERT INTO Course (course_id, course_name, materials, start_date, end_date, discription) 
 VALUES ('COMP3234', 'Computer and Communication Networks', 'https://github.com/armatrix/cs-computer-networking/blob/master/computer-networking-a-top-down-approach-8th-edition.pdf', '2022-09-01', '2022-11-30', 'https://www.cs.hku.hk/index.php/programmes/course-offered?infile=2022/comp3234.html');
INSERT INTO Course (course_id, course_name, materials, start_date, end_date, discription) 
 VALUES ('COMP3278', 'Introduction to database management systems', 'https://www.octawian.ro/fisiere/situri/asor/build/html/_downloads/1fcab53a6d916e39c715fc20a9a9c2a8/Silberschatz_A_databases_6th_ed.pdf', '2022-09-01', '2022-11-30', 'https://www.cs.hku.hk/index.php/programmes/course-offered?infile=2022/comp3278.html');
INSERT INTO Course (course_id, course_name, materials, start_date, end_date, discription) 
 VALUES ('COMP3297', 'Software Engineering', 'https://mycourses.aalto.fi/pluginfile.php/1177979/mod_resource/content/1/Sommerville-Software-Engineering-10ed.pdf', '2022-09-01', '2022-11-30', 'https://www.cs.hku.hk/index.php/programmes/course-offered?infile=2022/comp3230.html');
INSERT INTO Course (course_id, course_name, materials, start_date, end_date, discription) 
 VALUES ('ECON2280', 'Introductory Econometrics', 'https://www.amazon.com/Introductory-Econometrics-Modern-Approach-MindTap/dp/1337558869', '2022-09-01', '2022-11-30', 'https://ug.hkubs.hku.hk/f/course/253903/ECON2280%20Introductory%20Econometrics%202022-23%20draft.pdf');

###student

INSERT INTO student(student_id,student_name,student_password,email_address)
VALUES (3036001036, "Wang Haoyun","abc","u3600103@connect.hku.hk"),
(3035466731,"Young Ware","OCxQtOYo","Ware234@connect.hku.hk"),
(3035002978,"Brianna Summers","b6G29urN","Summers134@connect.hku.hk"),
(3035624419,"Jieping Yue","rx1Avfwp","Yue972@connect.hku.hk"),
(3035642392,"Jianfei Liu","stJtE1d7","Jianfei459@connect.hku.hk"),
(3035633982,"Shumei Jones","e9lHxXKT","Jones1230@connect.hku.hk"),
(3035051891,"Ana Arnold","6QvI4OUT","Arnold12023@connect.hku.hk"),
(3035923596,"Haruyoshi Araki","ecoF6WTz","Haruyoshi123@connect.hku.hkw"),
(3035730882,"Rita Chung","rbSItGEs","Rita0909@connect.hku.hk"),
(3035233527,"Yawen Fan","MXDPJdcR","Yawen405@connect.hku.hk"),
(3035135394,"Carmen West","m8sR8BMJ","Carmen4124@connect.hku.hk"),
(3035638052, "LI Haochen", "111","harry666@connect.hku.hk");

### Subclass

INSERT INTO Subclass (course_id, sub_class_id, classroom_address, teacher_msg, link, notes) 
 VALUES ('COMP3230', 'A', 'Tue CPD-LG.01; Thu CYPP2', 'Name: Dr. Chenshu WU; Office: CB315B; Email: chenshu@cs.hku.hk', 'N/A', 'https://moodle.hku.hk/course/view.php?id=96625');
INSERT INTO Subclass (course_id, sub_class_id, classroom_address, teacher_msg, link, notes) 
 VALUES ('COMP3230', 'B', 'CPD-LG.07', 'Name: Dr. Anthony Tam; Email: atctam@cs.hku.hk', 'N/A', 'https://moodle.hku.hk/enrol/index.php?id=966265');
INSERT INTO Subclass (course_id, sub_class_id, classroom_address, teacher_msg, link, notes) 
 VALUES ('COMP3234', 'A', 'LE4', 'Lecturer: Dr. Edith C. H. Ngai', 'https://hku.zoom.us/j/92583823540?pwd=aW00QTBRa29qRW1acWdIM2V4b1hGUT09', 'https://moodle.hku.hk/course/view.php?id=101632');
INSERT INTO Subclass (course_id, sub_class_id, classroom_address, teacher_msg, link, notes) 
 VALUES ('COMP3278', 'A', 'MWT2', 'Course Instructor: Dr. Ping Luo; Office: CB326; Email: pluo@cs.hku.hk', 'https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09', 'https://moodle.hku.hk/course/view.php?id=96513');
INSERT INTO Subclass (course_id, sub_class_id, classroom_address, teacher_msg, link, notes) 
 VALUES ('COMP3297', 'A', 'CYPP2', 'N/A', 'N/A', 'https://moodle.hku.hk/course/view.php?id=96515');
INSERT INTO Subclass (course_id, sub_class_id, classroom_address, teacher_msg, link, notes) 
 VALUES ('ECON2280', 'A', 'KKL 102', 'Instructor: Clement WONG', 'N/A', 'https://moodle.hku.hk/course/view.php?id=101626');
INSERT INTO Subclass (course_id, sub_class_id, classroom_address, teacher_msg, link, notes) 
 VALUES ('ECON2280', 'B', 'KKL 102', 'Instructor: Clement WONG', 'N/A', 'https://moodle.hku.hk/course/view.php?id=101626');
INSERT INTO Subclass (course_id, sub_class_id, classroom_address, teacher_msg, link, notes) 
 VALUES ('ECON2280', 'C', 'KKL 101', 'Instructor: Clement WONG', 'N/A', 'https://moodle.hku.hk/course/view.php?id=101626');

###Take

INSERT INTO Take
VALUES (3035002978, 'COMP3230', 'A'),
(3035638052, 'COMP3234', 'A'),
(3035638052, 'COMP3278', 'A'),
(3035638052, 'ECON2280', 'A'),
(3035638052, 'COMP3230', 'B'),
(3035051891, 'COMP3234', 'A'),
(3035051891, 'COMP3297', 'A'),
(3035051891, 'ECON2280', 'B'),
(3035135394, 'COMP3230', 'A'),
(3035135394, 'COMP3234', 'A'),
(3035135394, 'COMP3278', 'A'),
(3035135394, 'COMP3297', 'A'),
(3035135394, 'ECON2280', 'C'),
(3035233527, 'COMP3278', 'A'),
(3035466731, 'COMP3230', 'A'),
(3035624419, 'COMP3297', 'A'),
(3035633982, 'COMP3234', 'A'),
(3035642392, 'COMP3230', 'A'),
(3035923596, 'COMP3278', 'A'),
(3036001036, 'COMP3230', 'A'),
(3036001036, 'COMP3234', 'A'),
(3036001036, 'COMP3278', 'A');

###ClassTime

INSERT INTO Classtime
VALUES ('COMP3230', 'A', 'Thu', '10:30', '12:20'),
('COMP3230', 'A', 'Tue', '10:30', '12:20'),

('COMP3230', 'B', 'Thu', '10:30', '12:20'),
('COMP3230', 'B', 'Tue', '10:30', '12:20'),

('COMP3234', 'A', 'Fri', '12:30', '14:20'),
('COMP3234', 'A', 'Tue', '12:30', '13:20'),

('COMP3278', 'A', 'Mon', '14:30', '15:20'),
('COMP3278', 'A', 'Thu', '13:30', '15:20'),

('COMP3297', 'A', 'Fri', '09:30', '11:20'),
('COMP3297', 'A', 'Tue', '09:30', '10:20'),

('ECON2280', 'A', 'Mon', '09:30', '12:20'),

('ECON2280', 'B', 'Mon', '14:30', '17:20'),

('ECON2280', 'C', 'Mon', '13:30', '16:20');


