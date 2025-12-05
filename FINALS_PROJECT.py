import os

def print_info():
    os.system("cls")
    print("\n--- PRINT FUNCTION ---")
    print("Print is like your program's voice! It lets you show messages, numbers, or variables on the screen.")
    print("You can say 'Hello World', show scores, or even combine text and numbers like 'You got', 95, 'points!'")
    print("Basically, if you want your program to TALK to the user, print() is your best friend.")
    input("Press Enter to go back...")

def print_run():
    os.system("cls")
    print("Example:")
    print('print("Hello world!")')
    print("\nOutput:")
    print("Hello world!")
    print("\nAnother example:")
    number = 10
    print(f'print("The number is", {number})')
    print("Output:")
    print("The number is", number)
    input("\nPress Enter to go back...")

def print_menu():
    os.system("cls")
    print("What do you want to do?")
    print("1 --- See information")
    print("2 --- Run example")
    choice_input = input("Enter your choice: ")
    if choice_input == '1':
        print_info()
    elif choice_input == '2':
        print_run()
    else:
        input("Invalid choice! Press Enter...")

def input_info():
    os.system("cls")
    print("\n--- INPUT FUNCTION ---")
    print("Input() is how your program asks the user to tell it something.")
    print("You can ask for names, ages, or even secret codes!")
    print("Whatever the user types gets stored in a variable, so you can use it later.")
    print("It’s basically how your program starts a conversation with the player/user.")
    input("Press Enter to go back...")

def input_run():
    os.system("cls")
    print("Example:")
    print('name = input("Enter your name: ")')
    print('print("Hello,", name + "!")\n')
    user_name = input("Enter your name: ")
    print("\nOutput:")
    print("Hello,", user_name + "!")
    input("\nPress Enter to go back...")

def input_menu():
    os.system("cls")
    print("What do you want to do?")
    print("1 --- See information")
    print("2 --- Run example")
    choice_input = input("Enter your choice: ")
    if choice_input == '1':
        input_info()
    elif choice_input == '2':
        input_run()
    else:
        input("Invalid choice! Press Enter...")

def eval_info():
    os.system("cls")
    print("\n--- EVAL FUNCTION ---")
    print("Eval() is like a magic brain for your program.")
    print("You can type an expression like '5+3*2', and eval() will calculate it for you.")
    print("It’s super powerful because it can understand any Python code you type, but BE CAREFUL!")
    print("If you give it bad code, it might cause problems, so only use it safely.")
    input("Press Enter to go back...")

def eval_run():
    os.system("cls")
    print("Example:")
    print('result = eval(input("Type a math expression: "))')
    print('print("The result is:", result)\n')
    result = eval(input("Type a math expression (like 5+3*2): "))
    print("\nOutput:")
    print("The result is:", result)
    input("\nPress Enter to go back...")

def eval_menu():
    os.system("cls")
    print("What do you want to do?")
    print("1 --- See information")
    print("2 --- Run example")
    choice_input = input("Enter your choice: ")
    if choice_input == '1':
        eval_info()
    elif choice_input == '2':
        eval_run()
    else:
        input("Invalid choice! Press Enter...")

def int_info():
    os.system("cls")
    print("\n--- INT FUNCTION ---")
    print("Int() is like a filter that turns whatever the user types into a whole number.")
    print("If you type '5', it stays 5. If you type '5.6', it becomes 5.")
    print("It’s super handy when you want to do math with user inputs.")
    input("Press Enter to go back...")

def int_run():
    os.system("cls")
    print("Example:")
    print('number = int(input("Enter a whole number: "))')
    print('print("You entered:", number)\n')
    whole_number = int(input("Enter a whole number: "))
    print("\nOutput:")
    print("You entered:", whole_number)
    input("\nPress Enter to go back...")

def int_menu():
    os.system("cls")
    print("What do you want to do?")
    print("1 --- See information")
    print("2 --- Run example")
    choice_input = input("Enter your choice: ")
    if choice_input == '1':
        int_info()
    elif choice_input == '2':
        int_run()
    else:
        input("Invalid choice! Press Enter...")

def if_info():
    os.system("cls")
    print("\n--- IF / ELIF / ELSE ---")
    print("These are like decision gates in your program.")
    print("If something is true, do this. If not, check something else. Otherwise, do another thing.")
    print("It helps your program think and make choices based on conditions.")
    input("Press Enter to go back...")

def if_run():
    os.system("cls")
    print("Example:")
    print('age = int(input("Enter your age: "))')
    print('if age < 13:')
    print('    print("You are a child.")')
    print('elif age < 20:')
    print('    print("You are a teenager.")')
    print('else:')
    print('    print("You are an adult.")\n')
    
    age_input = int(input("Enter your age: "))
    print("\nOutput:")
    if age_input < 13:
        print("You are a child.")
    elif age_input < 20:
        print("You are a teenager.")
    else:
        print("You are an adult.")
    input("\nPress Enter to go back...")

def if_menu():
    os.system("cls")
    print("What do you want to do?")
    print("1 --- See information")
    print("2 --- Run example")
    choice_input = input("Enter your choice: ")
    if choice_input == '1':
        if_info()
    elif choice_input == '2':
        if_run()
    else:
        input("Invalid choice! Press Enter...")

def loop_info():
    os.system("cls")
    print("\n--- LOOPS ---")
    print("Loops repeat actions automatically many times.")
    print("A for loop in Python can go through numbers or items in a list.")
    print("This makes your program do repetitive tasks without typing them over and over.")
    input("Press Enter to go back...")

def loop_run():
    os.system("cls")
    print("Example:")
    print('for num in range(10, 0, -1):')
    print('    print(num)\n')
    print("Output:")
    for num in range(10, 0, -1):
        print(num)
    input("\nPress Enter to go back...")

def loop_menu():
    os.system("cls")
    print("What do you want to do?")
    print("1 --- See information")
    print("2 --- Run example")
    choice_input = input("Enter your choice: ")
    if choice_input == '1':
        loop_info()
    elif choice_input == '2':
        loop_run()
    else:
        input("Invalid choice! Press Enter...")

def list_info():
    os.system("cls")
    print("\n--- LISTS ---")
    print("Lists let you store a bunch of items in a single variable.")
    print("You can put numbers, words, True/False, or even other lists inside a list.")
    print("Lists are awesome for keeping things organized!")
    input("Press Enter to go back...")

def list_run():
    os.system("cls")
    print("Example:")
    print('colors = ["Red", "Green", "Blue", "Yellow"]')
    print('colors.reverse()')
    print('colors.sort()')
    print('print(colors)\n')
    colors = ['Red', 'Green', 'Blue', 'Yellow']
    colors.reverse()
    colors.sort()
    print("Output:")
    print(colors)
    input("\nPress Enter to go back...")

def list_menu():
    os.system("cls")
    print("What do you want to do?")
    print("1 --- See information")
    print("2 --- Run example")
    choice_input = input("Enter your choice: ")
    if choice_input == '1':
        list_info()
    elif choice_input == '2':
        list_run()
    else:
        input("Invalid choice! Press Enter...")

while True:
    os.system("cls")
    print("==========================================")
    print(" Welcome to My Python Beginner-Friendly Functions! ")
    print("Here, you'll learn some cool Python functions step by step.")
    print("Just play around, try the examples, and have fun coding :)")
    print("==========================================\n")
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
        break
    else:
        input("Invalid choice! Press Enter...")
