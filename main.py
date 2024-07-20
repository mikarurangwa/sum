class Student:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.courses_registered = []

    def __str__(self):
        return f"{self.email};{self.first_name};{self.last_name}"

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

    def __str__(self):
        return f"{self.name};{self.trimester};{self.credits}"

class GradeBook:
    def __init__(self):
        self.students = self.load_students()
        self.courses = self.load_courses()
        self.registrations = self.load_registrations()

    def load_students(self):
        try:
            with open('students.txt', 'r') as file:
                return [Student(*line.strip().split(';')) for line in file.readlines()]
        except FileNotFoundError:
            return []

    def load_courses(self):
        try:
            with open('courses.txt', 'r') as file:
                return [Course(*line.strip().split(';')) for line in file.readlines()]
        except FileNotFoundError:
            return []

    def load_registrations(self):
        try:
            with open('registered.txt', 'r') as file:
                return [line.strip().split(';') for line in file.readlines()]
        except FileNotFoundError:
            return []

    def save_students(self):
        with open('students.txt', 'w') as file:
            for student in self.students:
                file.write(f"{student}\n")

    def save_courses(self):
        with open('courses.txt', 'w') as file:
            for course in self.courses:
                file.write(f"{course}\n")

    def save_registrations(self):
        with open('registered.txt', 'w') as file:
            for registration in self.registrations:
                file.write(f"{';'.join(registration)}\n")

    def add_student(self):
        while True:
            email = input("Enter student email: ")
            if any(student.email == email for student in self.students):
                print("Student already added. Try another email or type '2' to return to the main menu.")
                continue_or_menu = input("Enter email or type '2' to return to the main menu: ").strip()
                if continue_or_menu == '2':
                    return
                continue
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            new_student = Student(email, first_name, last_name)
            self.students.append(new_student)
            self.save_students()
            print(f"Student {new_student.full_name} added successfully.")
            break

    def add_course(self):
        while True:
            name = input("Enter course name: ")
            if any(course.name == name for course in self.courses):
                print("Course already added. Try another course name or type '2' to return to the main menu.")
                continue_or_menu = input("Enter course name or type '2' to return to the main menu: ").strip()
                if continue_or_menu == '2':
                    return
                continue
            trimester = input("Enter trimester: ")
            credits = int(input("Enter credits: "))
            new_course = Course(name, trimester, credits)
            self.courses.append(new_course)
            self.save_courses()
            print(f"Course {name} added successfully.")
            break

    def register_student_for_course(self):
        while True:
            email = input("Enter student email: ")
            if not any(student.email == email for student in self.students):
                print("Student not found. Try another email or type '2' to return to the main menu.")
                continue_or_menu = input("Enter email or type '2' to return to the main menu: ").strip()
                if continue_or_menu == '2':
                    return
                continue
            course_name = input("Enter course name: ")
            if not any(course.name == course_name for course in self.courses):
                print("Course not found. Try another course name or type '2' to return to the main menu.")
                continue_or_menu = input("Enter course name or type '2' to return to the main menu: ").strip()
                if continue_or_menu == '2':
                    return
                continue
            if any(reg == [email, course_name] for reg in self.registrations):
                print("Student already registered for this course.")
                return
            self.registrations.append([email, course_name])
            self.save_registrations()
            print(f"Student {email} registered for {course_name} successfully.")
            break

    def register_grade_for_student(self):
        while True:
            email = input("Enter student email: ")
            student = next((student for student in self.students if student.email == email), None)
            if not student:
                print("Student not found. Try another email or type '2' to return to the main menu.")
                continue_or_menu = input("Enter email or type '2' to return to the main menu: ").strip()
                if continue_or_menu == '2':
                    return
                continue
            course_name = input("Enter course name: ")
            if not any([email, course_name] in reg for reg in self.registrations):
                print("Course not found or student not registered for the course. Try another course name or type '2' to return to the main menu.")
                continue_or_menu = input("Enter course name or type '2' to return to the main menu: ").strip()
                if continue_or_menu == '2':
                    return
                continue
            while True:
                grade = float(input("Enter the grade (0-4): "))
                if 0 <= grade <= 4:
                    # Update grade in registrations
                    for reg in self.registrations:
                        if reg == [email, course_name]:
                            reg.append(str(grade))
                            self.save_registrations()
                            print(f"Grade for {course_name} updated to {grade}.")
                            return
                else:
                    print("Invalid grade. Please enter a grade between 0 and 4 or type '2' to return to the main menu.")
                    continue_or_menu = input("Enter grade or type '2' to return to the main menu: ").strip()
                    if continue_or_menu == '2':
                        return

    def calculate_ranking(self):
        # This assumes GPA calculation is required which isn't yet implemented directly
        # If GPA was stored directly, we would use that; otherwise, compute as needed or modify structure
        print("Ranking functionality is not yet implemented.")

    def search_by_grade(self):
        min_grade = float(input("Enter minimum GPA: "))
        max_grade = float(input("Enter maximum GPA: "))
        # GPA checking not yet implemented, assuming placeholder
        print("Search by grade functionality is not yet implemented.")

    def generate_transcript(self):
        while True:
            email = input("Enter student email: ")
            student = next((s for s in self.students if s.email == email), None)
            if not student:
                print("Student not found. Try another email or type '2' to return to the main menu.")
                continue_or_menu = input("Enter email or type '2' to return to the main menu: ").strip()
                if continue_or_menu == '2':
                    return
            # Assuming GPA and courses from registrations
            print(f"Transcript for {student.full_name}:")
            for reg in self.registrations:
                if reg[0] == email:
                    course_name = reg[1]
                    grade = reg[2] if len(reg) > 2 else "Not graded yet"
                    print(f"Course: {course_name}, Grade: {grade}")
            # Placeholder for GPA
            print("GPA calculation functionality not yet implemented.")
            break

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

