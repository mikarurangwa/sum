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
        self.credits = int(credits)

    def __str__(self):
        return f"{self.name};{self.trimester};{self.credits}"

class GradeBook:
    def __init__(self):
        self.students = self.load_students()
        self.courses = self.load_courses()
        self.registrations = self.load_registrations()
        self.grades = self.load_grades()

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

    def load_grades(self):
        try:
            with open('grades.txt', 'r') as file:
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

    def save_grades(self):
        with open('grades.txt', 'w') as file:
            for grade in self.grades:
                file.write(f"{';'.join(grade)}\n")

    def add_student(self):
        while True:
            email = input("Enter student email: ")
            if any(student.email == email for student in self.students):
                print("Student already added.")
                action = input("Press 1 to enter another email or press 2 to return to the main menu: ").strip()
                while action not in ['1', '2']:
                    action = input("Invalid choice. Press 1 to enter another email or press 2 to return to the main menu: ").strip()
                if action == '2':
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
                print("Course already added.")
                action = input("Press 1 to enter another course or press 2 to return to the main menu: ").strip()
                while action not in ['1', '2']:
                    action = input("Invalid choice. Press 1 to enter another course or press 2 to return to the main menu: ").strip()
                if action == '2':
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
            student = next((student for student in self.students if student.email == email), None)
            if not student:
                print("Student not found.")
                action = input("Press 1 to enter another email or press 2 to return to the main menu: ").strip()
                while action not in ['1', '2']:
                    action = input("Invalid choice. Press 1 to enter another email or press 2 to return to the main menu: ").strip()
                if action == '2':
                    return
                continue
            while True:
                course_name = input("Enter course name: ")
                course = next((course for course in self.courses if course.name == course_name), None)
                if not course:
                    print("Course not found.")
                    action = input("Press 1 to enter another course name or press 2 to return to the main menu: ").strip()
                    while action not in ['1', '2']:
                        action = input("Invalid choice. Press 1 to enter another course name or press 2 to return to the main menu: ").strip()
                    if action == '2':
                        return
                    continue
                if any(reg == [email, course_name] for reg in self.registrations):
                    print("Student already registered for this course.")
                    return
                self.registrations.append([email, course_name])
                self.save_registrations()
                print(f"Student {email} registered for {course_name} successfully.")
                return

    def register_grade_for_student(self):
        while True:
            email = input("Enter student email: ")
            student = next((student for student in self.students if student.email == email), None)
            if not student:
                print("Student not found.")
                action = input("Press 1 to enter another email or press 2 to return to the main menu: ").strip()
                while action not in ['1', '2']:
                    action = input("Invalid choice. Press 1 to enter another email or press 2 to return to the main menu: ").strip()
                if action == '2':
                    return
                continue
            while True:
                course_name = input("Enter course name: ")
                registration = next((reg for reg in self.registrations if reg[0] == email and reg[1] == course_name), None)
                if not registration:
                    print("Course not found or student not registered for the course.")
                    action = input("Press 1 to enter another course name or press 2 to return to the main menu: ").strip()
                    while action not in ['1', '2']:
                        action = input("Invalid choice. Press 1 to enter another course name or press 2 to return to the main menu: ").strip()
                    if action == '2':
                        return
                    continue
                course = next((course for course in self.courses if course.name == course_name), None)
                while True:
                    try:
                        grade = float(input("Enter the grade (0-4): "))
                        if 0 <= grade <= 4:
                            credits_earned = float(input(f"Enter the credits earned (max {course.credits}): "))
                            if 0 <= credits_earned <= course.credits:
                                self.grades.append([email, course_name, str(grade), str(credits_earned)])
                                self.save_grades()
                                print(f"Grade for {course_name} updated to {grade} with {credits_earned} credits earned.")
                                return
                            else:
                                print(f"Invalid credits earned. Please enter a value between 0 and {course.credits}.")
                        else:
                            print("Invalid grade. Please enter a grade between 0 and 4.")
                    except ValueError:
                        print("Invalid input. Please enter numeric values for grade and credits earned.")
                    action = input("Press 1 to enter the grade and credits again or press 2 to return to the main menu: ").strip()
                    while action not in ['1', '2']:
                        action = input("Invalid choice. Press 1 to enter the grade and credits again or press 2 to return to the main menu: ").strip()
                    if action == '2':
                        return

    def calculate_gpa(self, email):
        student_grades = [grade for grade in self.grades if grade[0] == email]
        total_credits = 0
        total_grade_points = 0
        for grade in student_grades:
            grade_value = float(grade[2])
            credits_earned = float(grade[3])
            total_credits += credits_earned
            total_grade_points += grade_value * credits_earned
        return total_grade_points / total_credits if total_credits > 0 else 0

    def calculate_ranking(self):
        student_gpas = [(student, self.calculate_gpa(student.email)) for student in self.students]
        student_gpas.sort(key=lambda x: x[1], reverse=True)
        for student, gpa in student_gpas:
            print(f"{student.full_name} with GPA: {gpa:.2f}")

    def search_by_grade(self):
        min_grade = float(input("Enter minimum GPA: "))
        max_grade = float(input("Enter maximum GPA: "))
        student_gpas = [(student, self.calculate_gpa(student.email)) for student in self.students]
        filtered_students = [(student, gpa) for student, gpa in student_gpas if min_grade <= gpa <= max_grade]

        # Sort the filtered students by GPA in descending order
        filtered_students.sort(key=lambda x: x[1], reverse=True)

        if filtered_students:
            for student, gpa in filtered_students:
                print(f"{student.full_name} with GPA: {gpa:.2f}")
        else:
            print("No students found within that GPA range.")

    def generate_transcript(self):
        while True:
            email = input("Enter student email: ")
            student = next((s for s in self.students if s.email == email), None)
            if not student:
                print("Student not found.")
                while True:
                    action = input("Press 1 to enter another email or press 2 to return to the main menu: ").strip()
                    if action == '1':
                        break  # Breaks the inner loop and asks for email again
                    elif action == '2':
                        return  # Exits the function and goes back to the main menu
                    else:
                        print("Invalid choice. Please press 1 or 2.")
                        continue  # Continues the outer loop to ask for the email again
                        # If the student is found, print the transcript details
        print(f"Transcript for {student.full_name}:")
        for grade in self.grades:
            if grade[0] == email:
                course_name = grade[1]
                credits_earned = grade[3]
                print(f"Course: {course_name}, Credits Earned: {credits_earned}")
                print(f"Overall GPA: {self.calculate_gpa(email):.2f}")
                return  # Exit the function after printing the transcript




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
