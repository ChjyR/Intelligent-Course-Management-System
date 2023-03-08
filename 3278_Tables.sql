-- Active: 1663836194151@@127.0.0.1@3306@project3278
DROP DATABASE IF EXISTS `Project3278`;
CREATE DATABASE `Project3278`;
USE `Project3278`;

CREATE TABLE Student (
  student_id BIGINT NOT NULL PRIMARY KEY,
  student_name VARCHAR(80) NOT NULL,
  student_password VARCHAR(80) NOT NULL,
  email_address VARCHAR(80) NOT NULL
);

CREATE TABLE Records (
  record_id BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  student_id BIGINT NOT NULL,
  login_time TIME(0) NOT NULL,
  login_date DATE NOT NULL,
  duration FLOAT NOT NULL,
  FOREIGN KEY (student_id) REFERENCES Student (student_id)
);

CREATE TABLE Course (
  course_id VARCHAR(80) NOT NULL PRIMARY KEY,
  course_name VARCHAR(200) NOT NULL,
  materials VARCHAR(200) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  discription VARCHAR(1000) NOT NULL
);

CREATE TABLE Subclass (
  course_id VARCHAR(80) NOT NULL,
  sub_class_id VARCHAR(80) NOT NULL,
  classroom_address VARCHAR(80) NOT NULL,
  teacher_msg VARCHAR(80) NOT NULL,
  link VARCHAR(80) NOT NULL,
  notes VARCHAR(200) NOT NULL,
  PRIMARY KEY (course_id, sub_class_id),
  FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

CREATE TABLE Take (
  student_id BIGINT NOT NULL ,
  course_id VARCHAR(80) NOT NULL ,
  sub_class_id VARCHAR(80) NOT NULL,
  PRIMARY KEY(student_id, course_id, sub_class_id),
  FOREIGN KEY (student_id) REFERENCES Student(student_id),
  FOREIGN KEY (course_id, sub_class_id) REFERENCES Subclass(course_id, sub_class_id)
);


CREATE TABLE ClassTime (
  course_id VARCHAR(80) NOT NULL,
  sub_class_id VARCHAR(80) NOT NULL,
  week_day VARCHAR(80) NOT NULL,
  start_time TIME(0) NOT NULL,
  end_time TIME(0) NOT NULL,
  PRIMARY KEY (course_id, sub_class_id, week_day),
  FOREIGN KEY (course_id, sub_class_id) REFERENCES Subclass(course_id, sub_class_id)
);


