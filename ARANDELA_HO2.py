import tkinter as renz

window = renz.Tk()

window.title("Simple Profile App")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg="lightblue",cursor="hand2")

title = renz.Label(window,text="MY PROFILE",font=("League Spartan",35,"bold"),bg="lightblue")
title.pack(pady=(20,10))

fullname = renz.Label(window,text="Full Name: Renz Darrel Arandela",font=("Arial",20),bg="lightblue")
fullname.pack(pady=(10,0))

age = renz.Label(window,text="Age: 18",font=("Arial",20),bg="lightblue")
age.pack(pady=(10,0))

course = renz.Label(window,text="Course & Section: BSIT-1C",font=("Arial",20),bg="lightblue")
course.pack(pady=(10,0))

birthday = renz.Label(window,text="Birthday: June 17, 2007",font=("Arial",20),bg="lightblue")
birthday.pack(pady=(10,0))

motto = renz.Label(window,text="Personal Motto: Stay real, stay kind, and enjoy the little things in life.",font=("Arial",20,"italic"),bg="lightblue",wraplength=500,justify="center")

motto.pack(pady=(20,0))

window.mainloop()
