from pdb import run
from db.run_sql import run_sql

from models.student_course import Student_Course
from models.student import Student
import repositories.student_repository as student_repository
from models.course import Course
import repositories.course_repository as course_repository

#save
def save(student_course):
    sql = "INSERT INTO student_courses(student_id, course_id, grade) VALUES (%s, %s, %s) RETURNING id"
    values = [student_course.student.id, student_course.course.id, student_course.grade]
    results = run_sql(sql, values)
    id = results[0]['id']
    student_course.id = id
    return student_course

# # select all
# def select_all():
#     student_courses = []
#     sql = "SELECT * FROM student_courses"
#     results = run_sql(sql)
#     for result in results:
#         student_course = Student_Course(result['student_id'], result['course_id'], result['grade'], result['id'])
#         student_courses.append(student_course)
#     return student_courses

def select_all():
    student_courses = []

    sql = "SELECT * FROM student_courses"
    results = run_sql(sql)

    for result in results:
        student = student_repository.select(result["student_id"])
        course = course_repository.select(result["course_id"])
        student_course = Student_Course(student, course, result["grade"], result["id"])
        student_courses.append(student_course)
    return student_courses

# select according to id
def select(id):
    student_course = None
    sql = "SELECT * FROM student_courses WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        student = student_repository.select(result["student_id"])
        course = course_repository.select(result["course_id"])
        grade = result['grade']
        student_course = Student_Course(student, course, grade, id)
    return student_course

#delete all
def delete_all():
    sql = "DELETE FROM student_courses"
    run_sql(sql)
    
#delete according to id
def delete(id):
    sql = "DELETE FROM student_courses WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#update
def update(student_course):
    sql = "UPDATE student_courses SET (student_id, course_id, grade) = (%s, %s, %s) WHERE id = %s"
    values = [student_course.student.id, student_course.course.id, student_course.grade, student_course.id]
    run_sql(sql, values)