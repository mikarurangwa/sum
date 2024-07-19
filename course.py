class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits
    
    def update_info(self, new_name, new_trimester, new_credits):
        self.name = new_name
        self.trimester = new_trimester
        self.credits = new_credits
