import os

os.system('cls')
print('DLL Student Information system')
print('===================================')

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
     
    stud_record = {}

    if choice == 'a':
        print("ADD STUDENT RECORD")

        student_id = input("Input Student ID number")
        first_name = input("input student First Name").upper()
        last_name = input("Input Student last name").upper()
        course = input("Input Student Course").upper()
        section = input("Input Student Section").upper()  
        email = input("Input Student email").upper()

        stud_record[student_id] = [first_name, last_name, course, section, email]
        print("Data saved Succesfully")
        os.system('cls')
        continue
    elif choice == 'b':
        pass
        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'd':
        pass
        continue
    elif choice == 'e':
        pass
        continue
    elif choice == 'f':
        pass
        continue
    elif choice == 'g':
        print("System Exit")
    else:
        print("Ub")
