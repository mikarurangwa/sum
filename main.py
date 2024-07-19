from gradebook import GradeBook

def main():
    gradebook = GradeBook()
    while True:
        print("\nWelcome to the Grade Book Application!\n")
        print("Please select an action:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Exit")

        action = input("\nEnter your choice: ")

        if action == "1":
            print("\nAdd Student")
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
            print("\nStudent record created successfully!")
        elif action == "2":
            print("\nAdd Course")
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
            print("\nCourse record created successfully!")
        elif action == "3":
            print("\nRegister Student for Course")
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade for the course: "))
            gradebook.register_student_for_course(student_email, course_name, grade)
            print("\nStudent registered for course successfully!")
        elif action == "4":
            print("\nCalculate Ranking")
            ranking = gradebook.calculate_ranking()
            for rank, student in enumerate(ranking, 1):
                print(f"{rank}. {student.names} - GPA: {student.GPA}")
        elif action == "5":
            print("\nSearch by Grade")
            min_grade = float(input("Enter minimum grade: "))
            max_grade = float(input("Enter maximum grade: "))
            filtered_students = gradebook.search_by_grade(min_grade, max_grade)
            for student in filtered_students:
                print(f"{student.names} - GPA: {student.GPA}")
        elif action == "6":
            print("\nGenerate Transcript")
            student_email = input("Enter student email: ")
            transcript = gradebook.generate_transcript(student_email)
            if transcript:
                print(f"\nTranscript for {transcript['names']} (Email: {transcript['email']}):")
                print(f"GPA: {transcript['GPA']}")
                for course in transcript['courses']:
                    print(f"Course: {course['course'].name}, Grade: {course['grade']}, Credits: {course['credits']}")
        elif action == "7":
            print("\nExiting the application. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
