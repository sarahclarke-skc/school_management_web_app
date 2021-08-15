import pdb
from models.course import Course
from models.student_course import Student_Course
from models.student import Student

import repositories.course_repository as course_repository
import repositories.student_course_repository as student_course_repository
import repositories.student_repository as student_repository

#once created add student_repository.delete_all()
#then course_repository.delete_all()
#then student_repository.delete_all()
student_repository.delete_all()
course_repository.delete_all()
student_course_repository.delete_all()

#create instances of Course, Student, and Student_Course classes
#save these instances using a method from the corresponding repository


pdb.set_trace()