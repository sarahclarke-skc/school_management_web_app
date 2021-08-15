import unittest
from models.student import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Anton", "Artiukov", "aartiukov@gmail.com", "+7911231234", "Upper Intermediate", True)
    
    def test_student_has_first_name(self):
        self.assertEqual("Anton", self.student.first_name)
    
    def test_student_has_last_name(self):
        self.assertEqual("Artiukov", self.student.last_name)

    def test_student_has_email(self):
        self.assertEqual("aartiukov@gmail.com", self.student.email)
    
    def test_student_has_telephone(self):
        self.assertEqual("+7911231234", self.student.telephone)
    
    def test_student_has_level(self):
        self.assertEqual("Upper Intermediate", self.student.level)
    
    def test_student_has_id(self):
        self.assertEqual(None, self.student.id)

    #write method to join first and last name

    def test_get_full_name(self):
        student = self.student
        self.assertEqual("Anton Artiukov", self.student.get_full_name(student))