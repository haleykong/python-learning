class Student:
    '''
    def __init__(self, name, major, gpa, is_on_probation): # Map out what 
    attributes the class should have
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    '''

    def __init__(self, name, major, gpa):  # Map out what attributes
        # the class should have
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
