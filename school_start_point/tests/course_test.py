import unittest
from models.course import Course

class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course = Course("English File", "Upper Intermediate", "Tuesday Thursday", "19:30", 90, "36 weeks")

    def test_course_has_name(self):
        self.assertEqual("English File", self.course.name)