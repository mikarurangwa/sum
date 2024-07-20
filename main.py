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
