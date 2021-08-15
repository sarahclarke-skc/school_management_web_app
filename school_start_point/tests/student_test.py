import unittest
from models.student import Student

class TestSession(unittest.TestCase):
    def setUp(self):
        self.student = Student("Anton", "Artiukov", "aartiukov@gmail.com", "+7911231234", "Upper Intermediate", True)