from db.run_sql import run_sql

from models.course import Course
from models.student import Student
from models.student_course import Student_Course

import repositories.course_repository as course_repository
import repositories.student_repository as student_repository

#save - add student to course
def save(student_course):
    sql = "INSERT INTO student_courses(student_id, course_id, student_course.grade) VALUES (%s, %s, %s) RETURNING id"
    results = values = [student_course.student.id, student_course.course.id, student_course.id]
    run_sql(sql, values)
    student_course.id = results[0]['id']

#select all

#select according to id

#delete all
def delete_all():
    sql = "DELETE FROM student_courses"
    run_sql(sql)
#delete according to id

#update