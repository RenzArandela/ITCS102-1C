import os

os.system('cls')
print('DLL Student Information system')
print('===================================')

stud_record = {}

while True:
    print("Select from the following options")
    print('A - Adding Student Record')
    print('B - Printing Student Record')
    print('C - Search Student Record')
    print('D - Delete Student Record')
    print('E - Retake')
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

    elif choice == "b":
        os.system("cls")
        print("PRINTING STUDENT RECORD")
        print("====================================")

        for id,info in stud_record.items():
            print(f"STUDENT ID {id} - RECORD - {info}")

            continue

    elif choice == 'c':
        os.system("cls")
        print("SEARCH STUDENT RECORD")

        search_id = input("INPUT STUDENT ID ------- > ").lower()

        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print(f"RECORD FOUND for {search_id}")
                print("====================")
            else:
                print("RECORD NOT FOUND")
            for id, in stud_record[search_id]: 
                print(f" --{id}")
                print("============")
            else:
                print("no record found")
            break
        continue

    elif choice == 'd':
        os.system("cls")
    print("DELETE STUDENT RECORD")

    search_id = input("INPUT STUDENT ID --> ")

    if search_id in stud_record:
        stud_record.pop(search_id)
        print("RECORD DELETED SUCCESSFULLY")
    else:
        print("RECORD NOT FOUND")

    continue

    elif choice == "e"
