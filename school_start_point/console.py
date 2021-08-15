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
student = Student("Anton", "Artiukov", "aartiukov@gmail.com", "+7911231234", "Upper Intermediate", True)

student_2 = Student("Liza", "Bogdanova", "liza_b@gmail.com", "+7911222333", "Intermediate", True)

course = Course("English File", "Upper Intermediate", "Tuesday Thursday", "19:30", 90, "36 weeks")

course_2 = Course("English File", "Intermediate", "Wednesday Friday", "19:15", 120, "30 weeks")

student_course = Student_Course(student, course, "A")

student_course_2 = Student_Course(student_2, course_2, "B")
#save these instances using a method from the corresponding repository


pdb.set_trace()