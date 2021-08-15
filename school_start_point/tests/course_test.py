import unittest
from models.course import Course

class TestSession(unittest.TestCase):
    def setUp(self):
        self.course = Course("English File", "Upper Intermediate", "Tuesday Thursday", "19:30", 90, "36 weeks")
