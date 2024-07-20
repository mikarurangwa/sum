class Student:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.courses_registered = []
        self.grades = {}
        self.GPA = 0.0

    def register_for_course(self, course):
        if course in self.courses_registered:
            print("Student is already registered for this course.")
            return True
        else:
            self.courses_registered.append(course)
            self.grades[course.name] = 0  # Initialize grade to 0
            print(f"{self.full_name} has been registered for the course: {course.name}")
            return False

    def register_grade(self, course, grade):
        if course in self.courses_registered:
            self.grades[course.name] = grade
            self.calculate_GPA()
            print(f"Grade for {course.name} updated to {grade}.")
        else:
            print("Student is not registered for this course.")

    def calculate_GPA(self):
        total_credits = 0
        total_grade_points = 0
        for course in self.courses_registered:
            grade = self.grades[course.name]
            total_credits += course.credits
            total_grade_points += grade * course.credits
        self.GPA = total_grade_points / total_credits if total_credits > 0 else 0

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

class GradeBook:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self):
        while True:
            email = input("Enter student email: ")
            if any(student.email == email for student in self.students):
                print("Student already added. Please try another email.")
            else:
                first_name = input("Enter student's first name: ")
                last_name = input("Enter student's last name: ")
                new_student = Student(email, first_name, last_name)
                self.students.append(new_student)
                print(f"Student {new_student.full_name} added successfully.")
                break

    def add_course(self):
        while True:
            name = input("Enter course name: ")
            if any(course.name == name for course in self.courses):
                print("Course already added. Please try another course name.")
            else:
                trimester = input("Enter trimester: ")
                credits = int(input("Enter credits: "))
                new_course = Course(name, trimester, credits)
                self.courses.append(new_course)
                print(f"Course {name} added successfully.")
                break

    def register_student_for_course(self):
        while True:
            email = input("Enter student email: ")
            student = next((student for student in self.students if student.email == email), None)
            if not student:
                print("Student not found. Please enter a correct email.")
                continue
            course_name = input("Enter course name: ")
            course = next((course for course in self.courses if course.name == course_name), None)
            if not course:
                print("Course not found. Please enter a correct course name.")
                continue
            if not student.register_for_course(course):
                break

    def register_grade_for_student(self):
        while True:
            email = input("Enter student email: ")
            student = next((student for student in self.students if student.email == email), None)
            if not student:
                print("Student not found. Please enter a correct email.")
                continue
            course_name = input("Enter course name: ")
            course = next((course for course in self.courses if course.name == course_name), None)
            if not course:
                print("Course not found. Please enter a correct course name.")
                continue
            while True:
                grade = float(input("Enter the grade (0-4): "))
                if 0 <= grade <= 4:
                    student.register_grade(course, grade)
                    break
                else:
                    print("Invalid grade. Please enter a grade between 0 and 4.")
            break

    def calculate_ranking(self):
        sorted_students = sorted(self.students, key=lambda x: x.GPA, reverse=True)
        for student in sorted_students:
            print(f"{student.full_name} with GPA: {student.GPA:.2f}")

    def search_by_grade(self):
        min_grade = float(input("Enter minimum GPA: "))
        max_grade = float(input("Enter maximum GPA: "))
        found_students = [s for s in self.students if min_grade <= s.GPA <= max_grade]
        if not found_students:
            print("No students found within that GPA range.")
        else:
            for student in found_students:
                print(f"{student.full_name} with GPA: {student.GPA:.2f}")

    def generate_transcript(self):
        email = input("Enter student email: ")
        student = next((s for s in self.students if s.email == email), None)
        if not student:
            print("Student not found.")
        else:
            print(f"Transcript for {student.full_name}:")
            for course in student.courses_registered:
                grade = student.grades[course.name]
                print(f"Course: {course.name}, Grade: {grade}")
            print(f"Overall GPA: {student.GPA:.2f}")

    def display_menu(self):
        print("\nWelcome to the Grade Book Application!")
        print("Please select an action:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Register Student's Grades")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Exit")

    def main_loop(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_course()
            elif choice == '3':
                self.register_student_for_course()
            elif choice == '4':
                self.register_grade_for_student()
            elif choice == '5':
                self.calculate_ranking()
            elif choice == '6':
                self.search_by_grade()
            elif choice == '7':
                self.generate_transcript()
            elif choice == '8':
                print("Exiting application.")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    grade_book = GradeBook()
    grade_book.main_loop()
