import os

os.system('cls')
print('DLL Student Information system')
print('===================================')

stud_record = {}

while True:
    print("Select from the following options")
    print('A - Adding Student Record')
    print('B - Search Student')
    print('C - Edit Student Record')
    print('D - Delete Student Record')
    print('E - Print All Record')
    print('F - Export Data')
    print('G - Exit System')

    choice = input("Input your choice --> ").lower().strip()

    if choice == 'a':
        print("ADD STUDENT RECORD")
        student_id = input("Input Student ID number: ")
        first_name = input("Input Student First Name: ").upper()
        last_name = input("Input Student Last Name: ").upper()
        course = input("Input Student Course: ").upper()
        section = input("Input Student Section: ").upper()
        email = input("Input Student Email: ").upper()
        stud_record[student_id] = [first_name, last_name, course, section, email]
        print("Data saved Successfully")
        os.system('cls')
        continue

    elif choice == 'b':
        print("SEARCH STUDENT")
        student_id = input("Input Student ID: ")
        if student_id in stud_record:
            print(stud_record[student_id])
        else:
            print("Record Not Found")
        continue

    elif choice == 'c':
        print("EDIT STUDENT RECORD")
        student_id = input("Input Student ID: ")
        first_name = input("Input Student First Name: ").upper()
        last_name = input("Input Student Last Name: ").upper()
        course = input("Input Student Course: ").upper()
        section = input("Input Student Section: ").upper()
        email = input("Input Student Email: ").upper()
        stud_record[student_id] = [first_name, last_name, course, section, email]
        print("Record Updated")
        continue

    elif choice == 'd':
        print("DELETE STUDENT RECORD")
        student_id = input("Input Student ID: ")
        stud_record[student_id] = []  
        print("Record Deleted")
        continue

    elif choice == 'e':
        print("PRINT ALL RECORDS")
        print(stud_record)
        continue

    elif choice == 'f':
        print("EXPORT DATA")
        print("Exporting data is not available in your lesson") 
        continue

    elif choice == 'g':
        print("System Exit")
        break

    else:
        print("Invalid Choice")
