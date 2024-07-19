class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0
    
    def calculate_GPA(self):
        total_credits = sum(course['credits'] for course in self.courses_registered)
        if total_credits == 0:
            self.GPA = 0.0
        else:
            total_points = sum(course['grade'] * course['credits'] for course in self.courses_registered)
            self.GPA = total_points / total_credits
    
    def register_for_course(self, course, grade):
        self.courses_registered.append({'course': course, 'grade': grade, 'credits': course.credits})
    
    def update_info(self, new_email, new_names):
        self.email = new_email
        self.names = new_names
