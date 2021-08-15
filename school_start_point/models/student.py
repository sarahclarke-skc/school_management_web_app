class Student:

    def __init__(self, first_name, last_name, email, telephone, level, enrolled, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.telephone = telephone
        self.level = level
        self.enrolled = enrolled
        self.id = id
    
    def get_full_name(self, student):
        full_name = self.first_name + " " + self.last_name
        return full_name