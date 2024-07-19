from gradebook import GradeBook

def main():
    gradebook = GradeBook()
    while True:
        action = input("Choose an action: add student, add course, update student, update course, delete student, delete course, view all students, view all courses, view students in course, register student for course, edit grade, calculate GPA, calculate ranking, search by grade, generate transcript, exit: ")
        if action == "add student":
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
        elif action == "add course":
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
        elif action == "update student":
            email = input("Enter current student email: ")
            new_email = input("Enter new student email: ")
            new_names = input("Enter new student names: ")
            gradebook.update_student_info(email, new_email, new_names)
        elif action == "update course":
            name = input("Enter current course name: ")
            new_name = input("Enter new course name: ")
            new_trimester = input("Enter new course trimester: ")
            new_credits = int(input("Enter new course credits: "))
            gradebook.update_course_info(name, new_name, new_trimester, new_credits)
        elif action == "delete student":
            email = input("Enter student email: ")
            gradebook.delete_student(email)
        elif action == "delete course":
            name = input("Enter course name: ")
            gradebook.delete_course(name)
        elif action == "view all students":
            students = gradebook.view_all_students()
            for student in students:
                print(f"{student.names} (Email: {student.email}) - GPA: {student.GPA}")
        elif action == "view all courses":
            courses = gradebook.view_all_courses()
            for course in courses:
                print(f"Course: {course.name}, Trimester: {course.trimester}, Credits: {course.credits}")
        elif action == "view students in course":
            course_name = input("Enter course name: ")
            students_in_course = gradebook.view_students_in_course(course_name)
            for student in students_in_course:
                print(f"{student.names} (Email: {student.email})")
        elif action == "register student for course":
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade for the course: "))
            grade
