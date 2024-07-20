class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits
        self.grade = 0  # This will be set when registering grades for the student
