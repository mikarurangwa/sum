class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def register_for_course(self, course):
        self.courses_registered.append(course)

    def calculate_GPA(self):
        if not self.courses_registered:
            return
        total_credits = 0
        total_points = 0
        for course in self.courses_registered:
            total_credits += course.credits
            total_points += course.grade * course.credits
        self.GPA = total_points / total_credits

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits
        self.grade = 0  # This will be set when registering grades for the student

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

def main():
    grade_book = GradeBook()
    while True:
        print("\nPlease select an action:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            grade_book.add_student()
        elif choice == '2':
            grade_book.add_course()
        elif choice == '3':
            grade_book.register_student_for_course()
        elif choice == '4':
            grade_book.calculate_ranking()
        elif choice == '5':
            grade_book.search_by_grade()
        elif choice == '6':
            grade_book.generate_transcript()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
