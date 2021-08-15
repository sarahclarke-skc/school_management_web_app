import unittest
from models.course import Course

class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course = Course("English File", "Upper Intermediate", "Tuesday Thursday", "19:30", 90, "36 weeks")

    def test_course_has_name(self):
        self.assertEqual("English File", self.course.name)
    
    def test_course_has_level(self):
        self.assertEqual("Upper Intermediate", self.course.level)
    
    def test_course_has_days(self):
        self.assertEqual("Tuesday Thursday", self.course.days)
    
    def test_course_has_start_time(self):
        self.assertEqual("19:30", self.course.start_time)

    def test_course_has_duration(self):
        self.assertEqual(90, self.course.duration)