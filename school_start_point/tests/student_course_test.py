import unittest
from models.student_course import Student_Course
from models.student import Student
from models.course import Course

class TestStudent_Course(unittest.TestCase):
    def setUp(self):
        #I don't think this is right
        self.student = Student("Anton", "Artiukov", "aartiukov@gmail.com", "+7911231234", "Upper Intermediate", True)
        self.course = Course("English File", "Upper Intermediate", "Tuesday Thursday", "19:30", 90, "36 weeks")
        self.student_course = Student_Course(self.student, self.course, "A")
    
    def test_student_course_has_student(self):
        student = self.student
        self.assertEqual("Anton Artiukov", self.student_course.student.get_full_name(student))
    
    def test_student_course_has_course(self):
        self.assertEqual(self.course, self.student_course.course)
    
    def test_student_course_has_grade(self):
        self.assertEqual("A", self.student_course.grade)
    
    def test_student_course_has_id(self):
        self.assertEqual(None, self.student_course.id)