from db.run_sql import run_sql

from models.course import Course
from models.student import Student

#save
def save(course):
    sql = "INSERT INTO courses(name, level, days, start_time, duration, length_of_course) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [course.name, course.level, course.days, course.start_time, course.duration, course.length_of_course]
    results = run_sql(sql, values)
    course.id = results[0]['id']
    return course

#select all

def select_all():
    courses =[]

    sql = "SELECT * FROM courses"
    results = run_sql(sql)

    for result in results:
        course = Course(result['name'], result['level'], result['days'], result['start_time'], result['duration'], result['length_of_course'], result['id'])
        courses.append(course)

    return courses

#select one according to id

def select(id):
    course = None
    sql = "SELECT * FROM courses WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        course = Course(result['name'], result['level'], result['days'], result['start_time'], result['duration'], result['length_of_course'], result['id'])
    return course

#delete all
def delete_all():
    sql = "DELETE FROM courses"
    run_sql(sql)

#delete one according to id
def delete(id):
    sql = "DELETE FROM courses WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#update the course
def update(course):
    sql = "UPDATE courses SET (name, level, days, start_time, duration, length_of_course) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [course.name, course.level, course.days, course.start_time, course.duration, course.length_of_course, course.id]
    run_sql(sql, values)

#find the students enrolled on the course
def get_students_on_course(id):
    
    students = []

    sql = "SELECT students.* FROM students INNER JOIN student_courses ON student_courses.student_id = student.id WHERE student_courses.course_id =%s"
    values = [id]
    results = run_sql(sql, values)

    for result in results:
        student = Student(result['first_name'], result['last_name'], result['email'], result['telephone'], result['level'], result['enrolled'], result['id'])
        students.append(student)
    return students

