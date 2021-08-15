import pdb

from models.course import Course
import repositories.course_repository as course_repository

from models.student import Student
import repositories.student_repository as student_repository

from models.student_course import Student_Course
import repositories.student_course_repository as student_course_repository

#once created add student_repository.delete_all()
#then course_repository.delete_all()
#then student_repository.delete_all()
student_repository.delete_all()
course_repository.delete_all()
student_course_repository.delete_all()

#create instances of Course, Student, and Student_Course classes

#save these instances using a method from the corresponding repository

student = Student("Anton", "Artiukov", "aartiukov@gmail.com", "+7911231234", "Upper Intermediate", True)
student_repository.save(student)

student_2 = Student("Liza", "Bogdanova", "liza_b@gmail.com", "+7911222333", "Intermediate", True)
student_repository.save(student_2)

course = Course("English File", "Upper Intermediate", "Tuesday Thursday", "19:30", 90, "36 weeks")
course_repository.save(course)

course_2 = Course("English File", "Intermediate", "Wednesday Friday", "19:15", 120, "30 weeks")
course_repository.save(course_2)

student_course = Student_Course(student, course, "A")
student_course_repository.save(student_course)

student_course_2 = Student_Course(student_2, course_2, "B")
student_course_repository.save(student_course_2)




pdb.set_trace()