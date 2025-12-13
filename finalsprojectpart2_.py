import os
import time

# -------------------------- PRINT FUNCTION --------------------------
def print_info():
    os.system("cls")
    print("\n--- PRINT FUNCTION ---")
    print("Print is like your program's voice! It lets you show messages, numbers, or variables on the screen.")
    print("You can say 'Hello World', show scores, or even combine text and numbers like 'You got', 95, 'points!'")
    print("Basically, if you want your program to TALK to the user, print() is your best friend.")
    input("Press Enter to go back...")

def print_run():
    os.system("cls")
    print("Example 1:")
    print('print("Hello world!")')
    print("\nOutput: Hello world!")
    input("\nPress Enter for another example...")
    os.system("cls")
    number = 10
    print("Example 2:")
    print(f'print("The number is", {number})')
    print("Output: The number is", number)
    input("\nPress Enter to go back...")

def print_menu():
    while True:
        os.system("cls")
        print("What do you want to do in PRINT FUNCTION?")
        print("1 --- See information")
        print("2 --- Run examples")
        print("3 --- Go back to main menu")
        choice_input = input("Enter your choice: ")
        if choice_input == '1':
            print_info()
        elif choice_input == '2':
            print_run()
        elif choice_input == '3':
            break
        else:
            input("Invalid choice! Press Enter...")


# -------------------------- INPUT FUNCTION --------------------------
def input_info():
    os.system("cls")
    print("\n--- INPUT FUNCTION ---")
    print("Input() lets your program ask the user to type something.")
    print("You can ask for names, ages, favorite numbers, anything!")
    print("The program saves the user's answer into a variable to use later.")
    print("Think of it like a conversation between the program and the user.")
    input("Press Enter to go back...")

def input_run():
    os.system("cls")
    print("Example:")
    user_name = input("Enter your name: ")
    print("\nOutput:")
    print("Hello,", user_name + "!")
    input("Press Enter to go back...")

def input_menu():
    while True:
        os.system("cls")
        print("What do you want to do in INPUT FUNCTION?")
        print("1 --- See information")
        print("2 --- Run example")
        print("3 --- Compiler Program Activity")
        print("4 --- Go back to main menu")
        choice_input = input("Enter your choice: ")
        if choice_input == '1':
            input_info()
        elif choice_input == '2':
            input_run()
        elif choice_input == '3':
            os.system("cls")
            print("Welcome to my mini compiler!")
            name = input("Hi visitor, what is your name? ")
            print(f"Hi {name}, choose an option:")
            while True:
                print("\nA - Greet with your name")
                print("B - Factorial Calculator")
                print("C - Triangle Printer")
                print("E - Exit Compiler")
                sub_choice = input("Enter choice A-E: ").lower()
                if sub_choice == 'a':
                    n = input("Type your name: ")
                    print(f"Hello {n}, nice to meet you! 😄")
                    input("Press Enter to continue...")
                elif sub_choice == 'b':
                    num = eval(input("Type any number to get factorial: "))
                    factorial = 1
                    for i in range(1, num+1):
                        factorial *= i
                    print(f"The factorial of {num} is {factorial}")
                    input("Press Enter to continue...")
                elif sub_choice == 'c':
                    rows = int(input("How many rows for the triangle? "))
                    for i in range(1, rows+1):
                        print("* " * i)
                    input("Press Enter to continue...")
                elif sub_choice == 'e':
                    print("Exiting Compiler...")
                    time.sleep(1)
                    break
                else:
                    print("Invalid choice! Try again.")
                    input("Press Enter to continue...")
        elif choice_input == '4':
            break
        else:
            input("Invalid choice! Press Enter...")

# -------------------------- EVAL FUNCTION --------------------------
def eval_info():
    os.system("cls")
    print("\n--- EVAL FUNCTION ---")
    print("Eval() calculates math expressions typed as text.")
    print("You can type: 5+3*2 and it will give you the result.")
    print("Be careful, only type safe expressions!")
    input("Press Enter to go back...")

def eval_run():
    os.system("cls")
    expr = input("Type a math expression (like 5+3*2): ")
    try:
        result = eval(expr)
        print("Result:", result)
    except:
        print("Invalid expression ❌")
    input("Press Enter to go back...")

def eval_menu():
    while True:
        os.system("cls")
        print("What do you want to do in EVAL FUNCTION?")
        print("1 --- See information")
        print("2 --- Run example")
        print("3 --- PH Currency Breakdown Activity")
        print("4 --- Go back to main menu")
        choice_input = input("Enter your choice: ")
        if choice_input == '1':
            eval_info()
        elif choice_input == '2':
            eval_run()
        elif choice_input == '3':
            os.system("cls")
            amount = eval(input("Enter any amount to deposit: "))
            denominations = [1000,500,200,100,50,20,10,5,1]
            print("PH currency breakdown:")
            for d in denominations:
                count = amount // d
                amount %= d
                print(f"{count} x {d}")
            input("Press Enter to go back...")
        elif choice_input == '4':
            break
        else:
            input("Invalid choice! Press Enter...")

# -------------------------- INT FUNCTION --------------------------
def int_info():
    os.system("cls")
    print("\n--- INT FUNCTION ---")
    print("Int() converts numbers or strings into whole numbers.")
    print("Useful when you want math without decimals.")
    input("Press Enter to go back...")

def int_run():
    os.system("cls")
    num = int(float(input("Enter a whole number: ")))
    print("You entered:", num)
    input("Press Enter to go back...")

def int_menu():
    while True:
        os.system("cls")
        print("What do you want to do in INT FUNCTION?")
        print("1 --- See information")
        print("2 --- Run example")
        print("3 --- Fare Discount Checker Activity")
        print("4 --- Go back to main menu")
        choice_input = input("Enter your choice: ")
        if choice_input == '1':
            int_info()
        elif choice_input == '2':
            int_run()
        elif choice_input == '3':
            os.system("cls")
            name = input("Put your name: ")
            fare = eval(input("Enter fare: "))
            student = input("Are you a student? (yes/no) ")
            if student.lower() == "yes":
                discount = fare*0.2
                new_fare = fare - discount
                print(f"Hi {name}, your discounted fare is {new_fare}")
            else:
                print(f"Hi {name}, you pay regular fare: {fare}")
            input("Press Enter to go back...")
        elif choice_input == '4':
            break
        else:
            input("Invalid choice! Press Enter...")

# -------------------------- IF / ELSE FUNCTION --------------------------
def if_info():
    os.system("cls")
    print("\n--- IF / ELSE / ELIF ---")
    print("These allow the program to make decisions.")
    print("If some condition is true, do something. Else, do another thing.")
    input("Press Enter to go back...")

def if_run():
    os.system("cls")
    age = int(input("Enter your age: "))
    if age < 13:
        print("You are a child.")
    elif age < 20:
        print("You are a teenager.")
    else:
        print("You are an adult.")
    input("Press Enter to go back...")

def if_menu():
    while True:
        os.system("cls")
        print("What do you want to do in IF / ELSE / ELIF FUNCTION?")
        print("1 --- See information")
        print("2 --- Run example")
        print("3 --- Manga Selector Activity")
        print("4 --- Go back to main menu")
        choice_input = input("Enter your choice: ")
        if choice_input == '1':
            if_info()
        elif choice_input == '2':
            if_run()
        elif choice_input == '3':
            os.system("cls")
            print("Welcome to 1C Manga Selector!")
            print("Genres: 1.Action 2.Horror 3.Romance")
            genre = input("Pick genre 1-3: ")
            print("Year: 1.1990s 2.2000s 3.2010s")
            year = input("Pick year 1-3: ")
            print("Length: 1.Short 2.Medium 3.Long")
            length = input("Pick length 1-3: ")
            if genre=="1" and year=="2" and length=="3":
                print("Recommended: Fullmetal Alchemist, D.Gray-man, Gantz, Air Gear, Eyeshield 21")
            else:
                print("No recommendations available")
            input("Press Enter to go back...")
        elif choice_input == '4':
            break
        else:
            input("Invalid choice! Press Enter...")

# -------------------------- LOOP FUNCTION --------------------------
def loop_info():
    os.system("cls")
    print("\n--- LOOPS ---")
    print("Loops repeat actions automatically many times.")
    input("Press Enter to go back...")

def loop_run():
    os.system("cls")
    num = eval(input("Type a number for factorial calculation: "))
    result = 1
    for i in range(1, num+1):
        result *= i
    print(f"Factorial of {num} is {result}")
    input("Press Enter to go back...")

def loop_menu():
    while True:
        os.system("cls")
        print("What do you want to do in LOOP FUNCTION?")
        print("1 --- See information")
        print("2 --- Run factorial example")
        print("3 --- Odd Number Accumulator")
        print("4 --- Multiplication Table Maker")
        print("5 --- Countdown Timer Simulator")
        print("6 --- Go back to main menu")
        choice_input = input("Enter choice 1-6: ")
        if choice_input == '1':
            loop_info()
        elif choice_input == '2':
            loop_run()
        elif choice_input == '3':
            os.system("cls")
            total = 0
            print("Enter 10 numbers. We'll sum only odd ones.")
            for i in range(10):
                n = eval(input(f"Number {i+1}: "))
                if n % 2 != 0:
                    total += n
            print("Sum of odd numbers:", total)
            input("Press Enter to go back...")
        elif choice_input == '4':
            os.system("cls")
            n = eval(input("Enter a number for multiplication table: "))
            print(f"Multiplication table for {n}:")
            for i in range(1, 11):
                print(n, "x", i, "=", n*i)
            input("Press Enter to go back...")
        elif choice_input == '5':
            os.system("cls")
            start = eval(input("Enter countdown start: "))
            for i in range(start,0,-1):
                print(i)
                time.sleep(0.5)
            print("Liftoff!")
            input("Press Enter to go back...")
        elif choice_input == '6':
            break
        else:
            input("Invalid choice! Press Enter...")

# -------------------------- LIST FUNCTION --------------------------
def list_info():
    os.system("cls")
    print("\n--- LISTS ---")
    print("Lists store multiple values in one variable.")
    print("You can store numbers, words, True/False, even other lists!")
    input("Press Enter to go back...")

def list_run():
    os.system("cls")
    pl = ['java', 'C#', 'C++','C','Perl','Python','JavaScript','Rust','Golang']
    print("Last language in list:", pl[-1])
    dict_pl = {'Medyo Mahirap':'java', 'Tama lang':'C#', 'Mahirap talaga':'C++','luma na':'C',
               'pang matanda':'Perl','ge':'Python','hi':'JavaScript'}
    key = input("Enter a key (ex: 'Tama lang'): ")
    print("Value:", dict_pl.get(key,"Key not found"))
    input("Press Enter to go back...")

def list_menu():
    while True:
        os.system("cls")
        print("What do you want to do in LIST FUNCTION?")
        print("1 --- See information")
        print("2 --- Run example")
        print("3 --- Student Record System")
        print("4 --- Go back to main menu")
        choice_input = input("Enter choice 1-4: ")
        if choice_input == '1':
            list_info()
        elif choice_input == '2':
            list_run()
        elif choice_input == '3':
            os.system("cls")
            stud_record = {}
            while True:
                print("DLL Student Information System")
                print("A - Add Record B - Search C - Edit D - Delete E - Print All F - Export G - Exit")
                choice = input("Choice: ").lower()
                if choice == 'a':
                    sid = input("Student ID: ")
                    fname = input("First Name: ").upper()
                    lname = input("Last Name: ").upper()
                    course = input("Course: ").upper()
                    section = input("Section: ").upper()
                    email = input("Email: ").upper()
                    stud_record[sid] = [fname,lname,course,section,email]
                    print("Saved successfully")
                elif choice == 'b':
                    sid = input("Student ID to search: ")
                    print(stud_record.get(sid,"Record not found"))
                elif choice == 'c':
                    sid = input("Student ID to edit: ")
                    fname = input("First Name: ").upper()
                    lname = input("Last Name: ").upper()
                    course = input("Course: ").upper()
                    section = input("Section: ").upper()
                    email = input("Email: ").upper()
                    stud_record[sid] = [fname,lname,course,section,email]
                    print("Record updated")
                elif choice == 'd':
                    sid = input("Student ID to delete: ")
                    stud_record[sid] = []
                    print("Record deleted")
                elif choice == 'e':
                    print(stud_record)
                elif choice == 'f':
                    print("Export not available")
                elif choice == 'g':
                    break
                else:
                    print("Invalid choice")
                input("Press Enter to continue...")
        elif choice_input == '4':
            break
        else:
            input("Invalid choice! Press Enter...")

# -------------------------- MAIN MENU --------------------------
while True:
    os.system("cls")
    print("Welcome to My Python Beginner-Friendly Functions! ")
    print("Here, you'll learn some cool Python functions step by step.")
    print("Just play around, try the examples, and have fun coding :)")
    print("==========================================")
    print("A - PRINT FUNCTION")
    print("B - INPUT FUNCTION")
    print("C - EVAL FUNCTION")
    print("D - INT FUNCTION")
    print("E - IF ELSE ELIF FUNCTION")
    print("F - LOOP FUNCTION")
    print("G - LIST FUNCTION")
    print("H - EXIT PROGRAM")

    main_choice = input("Enter your choice: ").lower().strip()
    if main_choice == 'a':
        print_menu()
    elif main_choice == 'b':
        input_menu()
    elif main_choice == 'c':
        eval_menu()
    elif main_choice == 'd':
        int_menu()
    elif main_choice == 'e':
        if_menu()
    elif main_choice == 'f':
        loop_menu()
    elif main_choice == 'g':
        list_menu()
    elif main_choice == 'h':
        print("Thanks for using the program! Bye! 👋")
        break
    else:
        input("Invalid choice! Press Enter...")
