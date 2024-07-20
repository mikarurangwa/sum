class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.grades = {}  # Dictionary to hold course grades
        self.GPA = 0.0

    def register_for_course(self, course):
        if course not in self.courses_registered:
            self.courses_registered.append(course)
            self.grades[course.name] = 0  # Initialize grade to 0
            print(f"{self.names} has been registered for the course: {course.name}")
        else:
            print("Student is already registered for this course.")

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
        if total_credits > 0:
            self.GPA = total_grade_points / total_credits
        print(f"New GPA for {self.names} is {self.GPA:.2f}")

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

class GradeBook:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, email, names):
        if any(student.email == email for student in self.students):
            print("Student already added.")
            return
        new_student = Student(email, names)
        self.students.append(new_student)
        print(f"Student {names} added successfully.")

    def add_course(self, name, trimester, credits):
        if any(course.name == name for course in self.courses):
            print("Course already added.")
            return
        new_course = Course(name, trimester, credits)
        self.courses.append(new_course)
        print(f"Course {name} added successfully.")

    def register_student_for_course(self, email, course_name):
        student = next((student for student in self.students if student.email == email), None)
        course = next((course for course in self.courses if course.name == course_name), None)
        if student and course:
            student.register_for_course(course)
        else:
            print("Student or course not found.")

    def register_grade_for_student(self, email, course_name, grade):
        student = next((student for student in self.students if student.email == email), None)
        course = next((course for course in self.courses if course.name == course_name), None)
        if student and course:
            student.register_grade(course, grade)
        else:
            print("Student or course not found.")

    def display_menu(self):
        print("\nWelcome to the Grade Book Application!")
        print("Please select an action:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Register Student's Grades")
        print("8. Exit")

    def main_loop(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                email = input("Enter student email: ")
                names = input("Enter student names: ")
                self.add_student(email, names)
            elif choice == '2':
                name = input("Enter course name: ")
                trimester = input("Enter trimester: ")
                credits = int(input("Enter credits: "))
                self.add_course(name, trimester, credits)
            elif choice == '3':
                email = input("Enter student email: ")
                course_name = input("Enter course name: ")
                self.register_student_for_course(email, course_name)
            elif choice == '4':
                # Implement ranking calculation
                pass
            elif choice == '5':
                # Implement search by grade
                pass
            elif choice == '6':
                # Implement transcript generation
                pass
            elif choice == '7':
                email = input("Enter student email: ")
                course_name = input("Enter course name: ")
                grade = float(input("Enter the grade: "))
                self.register_grade_for_student(email, course_name, grade)
            elif choice == '8':
                print("Exiting application.")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    grade_book = GradeBook()
    grade_book.main_loop()
