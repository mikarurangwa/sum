class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0
    
    def calculate_GPA(self):
        total_credits = sum(course['credits'] for course in self.courses_registered)
        if total_credits == 0:
            self.GPA = 0.
