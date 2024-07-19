from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []
        self.load_records()

    def load_records(self):
        try:
            with open('Record.txt', mode='r') as file:
                section = None
                for line in file:
                    line = line.strip()
                    if line == "# Students":
                        section = "students"
                    elif line == "# Courses":
                        section = "courses"
                    elif line == "# Grades":
                        section = "grades"
                    elif section == "students" and line:
                        parts = line.split(',')
                        email = parts[0]
                        names = parts[1]
                        courses = parts[2:]
                        student = Student(email, names)
                        for course_info in courses:
                            course_name, grade, credits = course_info.split('|')
                            course = self.find_course(course_name)
                            if course:
                                student.register_for_course(course, float(grade))
                        self.student_list.append(student)
                    elif section == "courses" and line:
                        name, trimester, credits = line.split(',')
                        course = Course(name, trimester, int(credits))
                        self.course_list.append(course)
                    elif section == "grades" and line:
                        email, course_name, grade = line.split(',')
                        student = self.find_student(email)
                        course = self.find_course(course_name)
                        if student and course:
                            student.register_for_course(course, float(grade))
        except FileNotFoundError:
            pass  # Handle file not found

    def save_records(self):
        with open('Record.txt', mode='w') as file:
            file.write("# Students\n")
            for student in self.student_list:
                courses_info = ','.join(f"{course['course'].name}|{course['grade']}|{course['credits']}" for course in student.courses_registered)
                file.write(f"{student.email},{student.names},{courses_info}\n")

            file.write("# Courses\n")
            for course in self.course_list:
                file.write(f"{course.name},{course.trimester},{course.credits}\n")

            file.write("# Grades\n")
            for student in self.student_list:
                for course in student.courses_registered:
                    file.write(f"{student.email},{course['course'].name},{course['grade']}\n")

    def find_student(self, email):
        return next((s for s in self.student_list if s.email == email), None)

    def find_course(self, name):
        return next((c for c in self.course_list if c.name == name), None)

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)
        self.save_records()
    
    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        self.save_records()

    def delete_student(self, email):
        student = self.find_student(email)
        if student:
            self.student_list.remove(student)
            self.save_records()

    def delete_course(self, name):
        course = self.find_course(name)
        if course:
            self.course_list.remove(course)
            self.save_records()

    def update_student_info(self, email, new_email, new_names):
        student = self.find_student(email)
        if student:
            student.update_info(new_email, new_names)
            self.save_records()

    def update_course_info(self, name, new_name, new_trimester, new_credits):
        course = self.find_course(name)
        if course:
            course.update_info(new_name, new_trimester, new_credits)
            self.save_records()

    def register_student_for_course(self, student_email, course_name, grade):
        student = self.find_student(student_email)
        course = self.find_course(course_name)
        if student and course:
            student.register_for_course(course, grade)
            self.save_records()

    def edit_grade(self, student_email, course_name, new_grade):
        student = self.find_student(student_email)
        if student:
            for course in student.courses_registered:
                if course['course'].name == course_name:
                    course['grade'] = new_grade
                    student.calculate_GPA()
                    self.save_records()
                    return True
        return False

    def calculate_GPA(self, student_email):
        student = self.find_student(student_email)
        if student:
            student.calculate_GPA()
            self.save_records()

    def calculate_ranking(self):
        self.student_list.sort(key=lambda x: x.GPA, reverse=True)
        return self.student_list

    def search_by_grade(self, min_grade, max_grade):
        filtered_students = []
        for student in self.student_list:
            if any(min_grade <= course['grade'] <= max_grade for course in student.courses_registered):
                filtered_students.append(student)
        return filtered_students

    def generate_transcript(self, student_email):
        student = self.find_student(student_email)
        if student:
            transcript = {
                'email': student.email,
                'names': student.names,
                'GPA': student.GPA,
                'courses': student.courses_registered
            }
            return transcript
        return None

    def view_all_students(self):
        return self.student_list

    def view_all_courses(self):
        return self.course_list

    def view_students_in_course(self, course_name):
        students_in_course = []
        for student in self.student_list:
            if any(course['course'].name == course_name for course in student.courses_registered):
                students_in_course.append(student)
        return students_in_course
