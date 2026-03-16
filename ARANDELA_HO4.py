import tkinter as  tk


window = tk.Tk

window.title("Profile Builder ")
window.geometry("600x600")
window.resizable(False, True)

window.configure(bg="lightblue")

frame =tk.frame(window, bg = "light blue"  )

label = tk.Label(window,text="profile Builder",font ="Times New Roman",fg = "blue",bg = "lightblue")
label.pack()

entry = tk.Entry
entry.pack()


label = tk.Label(window,text="First name",font ="Times New Roman",fg = "blue",bg = "lightblue")
label.pack()

entry = tk.Entry
entry.pack()


label = tk.Label(window,text="Last Name",font ="Times New Roman",fg = "blue",bg = "lightblue")
label.pack()

entry = tk.Entry
entry.pack()


label = tk.Label(window,text="Age",font ="Times New Roman",fg = "blue",bg = "lightblue")
label.pack()

entry = tk.Entry
entry.pack()




entry = tk.Entry
entry.pack()


def compute():
    
    







