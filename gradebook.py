class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self):
        email = input("Enter student email: ")
        names = input("Enter student names: ")
        student = Student(email, names)
        self.student_list.append(student)
        print("Student record created successfully!")

    def add_course(self):
        name = input("Enter course name: ")
        trimester = input("Enter trimester: ")
        credits = int(input("Enter credits: "))
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        print("Course record created successfully!")

    def register_student_for_course(self):
        student_email = input("Enter student email: ")
        course_name = input("Enter course name: ")
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course)
            print("Course registered successfully!")

    def calculate_ranking(self):
        self.student_list.sort(key=lambda x: x.GPA, reverse=True)
        for student in self.student_list:
            print(f"{student.email}: {student.GPA}")

    def search_by_grade(self):
        min_grade = float(input("Enter minimum GPA: "))
        max_grade = float(input("Enter maximum GPA: "))
        filtered_students = [s for s in self.student_list if min_grade <= s.GPA <= max_grade]
        for student in filtered_students:
            print(f"{student.email}: {student.GPA}")

    def generate_transcript(self):
        student_email = input("Enter student email: ")
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            print(f"Transcript for {student.names}")
            for course in student.courses_registered:
                print(f"{course.name}: Grade {course.grade}")
            print(f"Overall GPA: {student.GPA}")



