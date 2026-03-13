import tkinter as tk

window = tk.Tk()
window.title("Simple Calculator")

result = tk.Label(window, text="")
result.pack(pady=10)

frame = tk.Frame(window, bg="lightblue", padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Enter 1st Number:").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Enter 2nd Number:").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1, padx=5, pady=5)

def add():
    result.config(text="The sum of " + entry1.get() + " + " + entry2.get() + " is " + str(int(entry1.get()) + int(entry2.get())))

def subtract():
    result.config(text="The difference of " + entry1.get() + " - " + entry2.get() + " is " + str(int(entry1.get()) - int(entry2.get())))

def multiply():
    result.config(text="The product of " + entry1.get() + " * " + entry2.get() + " is " + str(int(entry1.get()) * int(entry2.get())))

def divide():
    result.config(text="The division of " + entry1.get() + " / " + entry2.get() + " is " + str(int(entry1.get()) / int(entry2.get())))

tk.Button(frame, text="Add", width=10, command=add).grid(row=2, column=0, pady=5)
tk.Button(frame, text="Subtract", width=10, command=subtract).grid(row=2, column=1, pady=5)
tk.Button(frame, text="Multiply", width=10, command=multiply).grid(row=3, column=0, pady=5)
tk.Button(frame, text="Division", width=10, command=divide).grid(row=3, column=1, pady=5)

window.mainloop()
