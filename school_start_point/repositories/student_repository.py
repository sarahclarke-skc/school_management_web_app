from db.run_sql import run_sql
from models.student import Student
from models.course import Course

#save
def save(student):
    sql = "INSERT INTO students(first_name, last_name, email, telephone, level, enrolled) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [student.first_name, student.last_name, student.email, student.telephone, student.level, student.enrolled]
    results = run_sql(sql, values)
    return student
#select all

#select one according to id

#delete all
def delete_all():
    sql = "DELETE FROM students"
    run_sql(sql)

#delete one according to id

#update student

#find the courses a student is enrolled on