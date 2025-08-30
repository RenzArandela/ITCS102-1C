name = input("Put your name here -->  ")
fare = eval(input("Fare fee -->  "))
Student = input("are you a student? (yes / no)")

if Student == "yes":
    discount = fare * 0.2
    new_fare = fare - discount
    print ("Hi",name,"Your discount is",discount,"Your new fare is", new_fare)
else:
    print("hi", name,"you're only eligible for regular price")
