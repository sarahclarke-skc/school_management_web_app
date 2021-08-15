from db.run_sql import run_sql

from models.course import Course
from models.student import Student

def save(course):
    sql = "INSERT INTO courses(name, level, days, start_time, duration, length_of_course) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [course.name, course.level, course.days, course.start_time, course.duration, course.length_of_course]
    results = run_sql(sql, values)
    return course
#select all

def select_all():
    course =[]
    sql = "SELECT * FROM courses"
    results = run_sql

    for row in results:
        course = Course(results['name'], results['level'], results['days'], results['start_time'], results['duration'], results['length_of_course'], results['id'])
        results.append(course)
        
    return course

#select one according to id

#delete all

#delete one according to id

#update the course

#find the students enrolled on the course
