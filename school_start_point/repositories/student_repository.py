from db.run_sql import run_sql
from models.student import Student
from models.course import Course

#save

#select all

#select one according to id

#delete all
def delete_all():
    sql = "DELETE FROM students"
    run_sql(sql)

#delete one according to id

#update student

#find the courses a student is enrolled on