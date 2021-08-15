import unittest
from models.student import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Anton", "Artiukov", "aartiukov@gmail.com", "+7911231234", "Upper Intermediate", True)
    
    def test_student_has_first_name(self):
        self.assertEqual("Anton", self.student.first_name)
    
    def test_student_has_last_name(self):
        self.assertEqual("Artiukov", self.student.last_name)

    #write method to join first and last name