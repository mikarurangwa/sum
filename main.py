class Student:
    def __init__(self, email, names, courses_registered=None):
        self.email = email
        self.names = names
        self.courses_registered = courses_registered if courses_registered else []
        self.GPA = 0.0

    def register_for_course(self, course):
        if course in self.courses_registered:
            print("Student is already registered to this course.")
        else:
            self.courses_registered.append(course)
            print("Student registered to course successfully.")

    def calculate_GPA(self):
        if not self.courses_registered:
            return
        total_credits = 0
        total_points = 0
        for course in self.courses_registered:
            total_credits += course.credits
            total_points += course.grade * course.credits
        self.GPA = total_points / total_credits if total_credits > 0 else 0

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits
        self.grade = 0

class GradeBook:
    def __init__(self):
        self.student_list, self.course_list = self.load_records()

    def load_records(self):
        try:
            with open('records.txt', 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            return [], []
        
        students = []
        courses = []
        current_type = None
        for line in lines:
            if line.strip() == 'Students':
                current_type = 'students'
            elif line.strip() == 'Courses':
                current_type = 'courses'
            elif line.strip() and current_type:
                if current_type == 'students':
                    email, names, courses_registered_str = line.strip().split(';')
                    courses_registered = courses_registered_str.split(',') if courses_registered_str else []
                    students.append(Student(email, names, courses_registered))
                elif current_type == 'courses':
                    name, trimester, credits = line.strip().split(';')
                    courses.append(Course(name, trimester, int(credits)))
        return students, courses

    def save_records(self):
        with open('records.txt', 'w') as file:
            file.write('Students\n')
            for student in self.student_list:
                courses_str = ','.join([course.name for course in student.courses_registered])
                file.write(f"{student.email};{student.names};{courses_str}\n")
            file.write('Courses\n')
            for course in self.course_list:
                file.write(f"{course.name};{course.trimester};{course.credits}\n")

    def add_student(self):
        email = input("Enter student email: ")
        if any(s.email == email for s in self.student_list):
            print("Student is already added.")
            return
        names = input("Enter student names: ")
        student = Student(email, names)
        self.student_list.append(student)
        self.save_records()
        print("Student record created successfully!")

    def add_course(self):
        name = input("Enter course name: ")
        if any(c.name == name for c in self.course_list):
            print("Course is already added.")
            return
        trimester = input("Enter trimester: ")
        credits = int(input("Enter credits: "))
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        self.save_records()
        print("Course record created successfully!")

    def register_student_for_course(self):
        student_email = input("Enter student email: ")
        course_name = input("Enter course name: ")
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course)
            self.save_records()
        elif not course:
            print("Course not found. Please add the course first.")

    def register_grade(self):
        student_email = input("Enter student email: ")
        course_name = input("Enter course name: ")
        grade = float(input("Enter the grade: "))
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name and c in student.courses_registered), None)
        if student and course:
            course.grade = grade
            student.calculate_GPA()
            self.calculate_ranking()
            self.save_records()
            print("Grade registered and GPA updated successfully.")
        else:
            print("Either student or course not found, or course not registered for this student.")

    def calculate_ranking(self):
        self.student_list.sort(key=lambda x: x.GPA, reverse=True)
        for student in self.student_list:
            print(f"{student.email}: {student.GPA}")

def main():
    grade_book = GradeBook()
    actions = {
        '1': grade_book.add_student,
        '2': grade_book.add_course,
        '3': grade_book.register_student_for_course,
        '4': grade_book.calculate_ranking,
        '5': lambda: print("This feature is not implemented yet."),
        '6': lambda: print("This feature is not implemented yet."),
        '7': grade_book.register_grade
    }
    while True:
        print("\nPlease select an action:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Show Ranking")
        print("5. Search by Grade (Not Implemented)")
        print("6. Generate Transcript (Not Implemented)")
        print("7. Register Grade")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '8':
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
