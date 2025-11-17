import os

os.system('cls')

print('Student Information System')
print('============================')

student_record = {}

while True:
    print('SELECT FROM THE FOLLOWING OPTIONS:')
    print('A - ADD STUDENT RECORD')
    print('B - PRINT ALL STUDENT RECORD')
    print('C - SEARCH STUDENT RECORD')
    print('D - DELETE STUDENT RECORD')
    print('E - EDIT STUDENT RECORD')
    print('F - EXPORT STUDENT RECORD')
    print('G - EXIT SYSTEM')
    
    choice = input('SELECT FROM THE OPTION ABOVE: ').lower()
    
    if choice == 'a':
        os.system('cls')
        print('ADDING STUDENT RECORD')
        id_no = input('Please enter student ID number: ')
        first_name = input('Please enter first name: ')
        last_name = input('Please enter last name: ')
        age = eval(input('Please enter age: '))
        course = input('Please enter course: ').upper()
        section = input('Please enter section: ').upper()
        
        student_record[id_no] = [first_name, last_name, age, course, section]
        print(f'Student record for {first_name} {last_name} added successfully!\n')
        continue
    elif choice == 'b':
        os.system('cls')
        print('PRINTING ALL STUDENT RECORDS')
        print('============================')
        for i, j in student_record.items():
            print(f"CODE - {i}, INFORMATION - {j}")
        continue
    elif choice == 'c':
        os.system('cls')
        print('SEARCHING STUDENT RECORD')
        search_id = input('Enter student ID number to search: ')
        if search_id in student_record:
            print(f"Record found: CODE - {search_id}, INFORMATION - {student_record[search_id]}\n")
        else:
            print('Student record not found.\n')
        continue
    elif choice == 'd':
        os.system('cls')
        print('DELETING STUDENT RECORD')
        delete_id = input('Enter student ID number to delete: ')
        if delete_id in student_record:
            del student_record[delete_id]
            print(f'Student record with ID {delete_id} deleted successfully!\n')
        else:
            print('Student record not found.\n')
        continue
    elif choice == 'e':
        os.system('cls')
        print('EDITING STUDENT RECORD')
        edit_id = input('Enter student ID number to edit: ')
        if edit_id in student_record:
            print('Enter new details (leave blank to keep current value):')
            first_name = input(f'First name ({student_record[edit_id][0]}): ') or student_record[edit_id][0]
            last_name = input(f'Last name ({student_record[edit_id][1]}): ') or student_record[edit_id][1]
            age = input(f'Age ({student_record[edit_id][2]}): ') or student_record[edit_id][2]
            course = input(f'Course ({student_record[edit_id][3]}): ') or student_record[edit_id][3]
            section = input(f'Section ({student_record[edit_id][4]}): ') or student_record[edit_id][4]  
            student_record[edit_id] = [first_name, last_name, age, course, section]
            print(f'Student record for ID {edit_id} updated successfully!\n')
        continue
    elif choice == 'f':
        os.system('cls')
        print('EXPORTING STUDENT RECORDS')
        with open('student_records.txt', 'w') as file:
            for i, j in student_record.items():
                file.write(f"CODE - {i}, INFORMATION - {j}\n")
        continue
    elif choice == 'g':
        os.system('cls')
        print('Exiting the Student Information System. Goodbye!')
        break
    else:
        os.system('cls')
        print('Invalid option selected. Please try again.\n')
        continue
