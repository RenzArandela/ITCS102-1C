import tkinter as tk

window = tk.Tk()
window.title("Profile Builder")
window.geometry("600x300")
window.configure(bg="lightgray")

tk.Label(window, text="Profile Builder", bg="lightgray").grid(row=0,column=1)

tk.Entry(window).grid(row=1,column=0)
tk.Entry(window).grid(row=1,column=1)
tk.Entry(window).grid(row=1,column=2)

tk.Label(window,text="First").grid(row=2,column=0)
tk.Label(window,text="Middle").grid(row=2,column=1)
tk.Label(window,text="Last").grid(row=2,column=2)

tk.Entry(window).grid(row=3,column=0)
tk.Label(window,text="Birth Year").grid(row=4,column=0)

tk.Label(window,text="Age").grid(row=3,column=1)

tk.Label(window,text="Gender").grid(row=5,column=0)
tk.Radiobutton(window,text="Male").grid(row=5,column=1)
tk.Radiobutton(window,text="Female").grid(row=5,column=2)

tk.Button(window,text="Submit").grid(row=6,column=1)

window.mainloop()
