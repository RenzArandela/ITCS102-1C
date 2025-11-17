from activity23_1 import *

print("Welcome to my compiler program")
name = input("hi Visitor, what is your name -->")

print(f"hi{name}, select from the options below")
print("A - Great name\nB - Greet with Name, Age, Location\nC- Traingle\nE- Exit")

isCont= True

while isCont == True:
    choice = input ("Select from A = E --> ").lower()

    if choice == 'a':
        name = input("Please state your name")
        Greetwithname(name)
        continue
    elif choice == 'b':
        number = eval(input("Input Any number --> "))
        print(f"factorial of {number} us {Factorial(number)}")
        continue
    elif choice == 'c':
        GetTriangle()
        continue 
    elif choice == 'e':
        print("program terminated ....")
        break
    else:
        print("invalid choice")
        continue
