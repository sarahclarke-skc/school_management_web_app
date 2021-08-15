import unittest
from models.student_course import Student_Course

class TestStudent_Course(unittest.TestCase):
    def setUp(self):
        self.student_course = Student_Course("Anton Artiukov", "English File", "A")