from models.student_course import Student_Course
from pdb import run
from db.run_sql import run_sql
from models.student import Student
from models.course import Course

#save
def save(student):
    sql = "INSERT INTO students(first_name, last_name, email, telephone, level, enrolled) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [student.first_name, student.last_name, student.email, student.telephone, student.level, student.enrolled]
    results = run_sql(sql, values)
    student.id = results[0]['id']
    return student

#select all - might be nice to put them in alphabetical order

def select_all():
    students =[]

    sql = "SELECT * FROM students ORDER BY last_name ASC"
    results = run_sql(sql)

    for result in results:
        student = Student(result['first_name'], result['last_name'], result['email'], result['telephone'], result['level'], result['enrolled'], result['id'])
        students.append(student)

    return students

#select one according to id
def select(id):
    student = None

    sql = "SELECT * FROM students WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        student = Student(result["first_name"], result["last_name"], result["email"], result["telephone"], result["level"], result["enrolled"], result["id"])
    return student

#delete all
def delete_all():
    sql = "DELETE FROM students"
    run_sql(sql)

#delete one according to id
def delete(id):
    sql = "DELETE FROM students WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#update student
def update(student):
    sql = "UPDATE student SET (first_name, last_name, email, telephone, level, enrolled) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [student.first_name, student.last_name, student.email, student.telephone, student.level, student.enrolled, student.id]
    run_sql(sql, values)

#find the courses a student is enrolled on
def courses(student):
    courses = []
    
    sql = "SELECT courses.* FROM courses INNER JOIN student_courses ON student_courses.course_id = course.id WHERE student_courses.student_id = %s"
    values = [student.id]
    results = run_sql(sql, values)

    for result in results:
        course = Course(result['name'], result['level'], result['days'], result['start_time'], result['duration'], result['length_of_course'], result['id'])
        courses.append(course)

    return courses