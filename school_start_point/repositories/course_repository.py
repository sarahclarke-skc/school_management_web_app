from db.run_sql import run_sql

from models.course import Course
from models.student import Student

#save
def save(course):
    sql = "INSERT INTO courses(name, level, days, start_time, duration, length_of_course) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [course.name, course.level, course.days, course.start_time, course.duration, course.length_of_course]
    results = run_sql(sql, values)
    id = results[0]['id']
    course.id = id
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
    sql = "SELECT * FROM courses WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    course = Course(result['name'], result['level'], result['days'], result['start_time'], result['duration'], result['length_of_course'], result['id'])
    return course

#delete all
def delete_all():
    sql = "DELETE FROM courses"
    run_sql(sql)

#delete one according to id

#update the course

#find the students enrolled on the course
