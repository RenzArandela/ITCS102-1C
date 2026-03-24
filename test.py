from tkinter import *

app = Tk()
app.title("Simple Account System")
app.geometry("300x400")

stored_username = ""
stored_password = ""


Label(app, text="REGISTER").pack()

Label(app, text="Username").pack()
reg_user = Entry(app)
reg_user.pack()

Label(app, text="Password").pack()
reg_pass = Entry(app)
reg_pass.pack()

Button(app, text="Register").pack()


Label(app, text="LOGIN").pack()

Label(app, text="Username").pack()
log_user = Entry(app)
log_user.pack()

Label(app, text="Password").pack()
log_pass = Entry(app)
log_pass.pack()

Button(app, text="Log In").pack()

app.mainloop()  
