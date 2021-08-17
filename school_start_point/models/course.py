class Course:
    def __init__(self, name, level, days, start_time, duration, length_of_course, id=None):
        self.name = name
        self.level = level
        self.days = days
        self.start_time = start_time
        self.duration = duration
        self.length_of_course = length_of_course
        self.id = id

#add capacity parameter
#add number of students booked onto course
# def check_capacity(self):
#     return booked =< capacity
