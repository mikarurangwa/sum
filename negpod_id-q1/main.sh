#!/bin/bash

# File to store student records
FILE="students-list_1023.txt"
SELECT_EMAILS_SCRIPT="select-emails.sh"
STUDENT_EMAILS_FILE="student-emails.txt"

# Check if the file exists, otherwise create it
if [ ! -f $FILE ]; then
    touch $FILE
fi

# Display the menu
display_menu() {
    echo "----------------------------
ALU REGISTRATION SYSTEM
----------------------------"
    echo "1. Create student record"
    echo "2. View all student records"
    echo "3. Delete a student record"
    echo "4. Update a student record"
    echo "5. Select email"
    echo "6. Exit"
}

# Create a new student record
create_student() {
    echo "Enter student's email:"
    read email
    echo "Enter student's age:"
    read age
    echo "Enter student's ID:"
    read id
    echo "$email, $age, $id" >> $FILE
    echo "Student record created successfully!"
}
# View all student records
view_students() {
    echo "List of student records:"
    cat $FILE
}

# Function to delete a student record
delete_student_record() {
    echo "Enter student ID to delete:"
    read id
    if [ -f $FILE ]; then
        grep -v ",$id\$" $FILE > temp.txt && mv temp.txt $FILE
        echo "Student record deleted successfully."
    else
        echo "No student records found."
    fi
}



#update the student record by id
update_student() {
    echo "Enter the student ID to update:"
    read id
    grep -v ", $id\$" $FILE > temp.txt
    mv temp.txt $FILE
    echo "Enter the new student's email:"
    read new_email
    echo "Enter the new student's age:"
    read new_age
    echo "$new_email, $new_age, $id" >> $FILE
    echo "Student record updated successfully!"
}

#select email 
select_email() {
     ./"$SELECT_EMAILS_SCRIPT" "$FILE" > "$STUDENT_EMAILS_FILE"
            echo "Student emails saved to $STUDENT_EMAILS_FILE"
    }

# Main loop to display menu and handle user input
while true; do
    display_menu
    echo "Select an option:"
    read option
    case $option in
        1) create_student ;;
        2) view_students ;;
        3) delete_student ;;
        4) update_student ;;
        5) select_email ;;
	6) exit ;;
        *) echo "Invalid option, please try again." ;;
    esac
done
