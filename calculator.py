from tkinter import *

root = Tk()
root.title("Standard Calculator")

e = Entry(root, width=35, borderwidth=5, bg="grey", fg="white", font=20)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))
    if math == "percentage":
        e.insert(0, f_num / 100)
    if math == "fraction":
        e.insert(0, 1 / f_num)
    if math == "square":
        e.insert(0, f_num**2)
    if math == "square_root":
        e.insert(0, f_num**0.5)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


def button_percentage():
    first_number = e.get()
    global f_num
    global math
    math = "percentage"
    f_num = float(first_number)
    e.delete(0, END)


def button_fraction():
    first_number = e.get()
    global f_num
    global math
    math = "fraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_square():
    first_number = e.get()
    global math
    global f_num
    math = "square"
    f_num = float(first_number)
    e.delete(0, END)


def button_square_root():
    first_number = e.get()
    global f_num
    global math
    math = "square_root"
    f_num = float(first_number)
    e.delete(0, END)


# Define Buttons
button_1 = Button(
    root,
    text="1",
    padx=40,
    pady=20,
    command=lambda: button_click(1),
    bg="grey",
    fg="white",
)
button_2 = Button(
    root,
    text="2",
    padx=75,
    pady=20,
    command=lambda: button_click(2),
    bg="grey",
    fg="white",
)
button_3 = Button(
    root,
    text="3",
    padx=75,
    pady=20,
    command=lambda: button_click(3),
    bg="grey",
    fg="white",
)
button_4 = Button(
    root,
    text="4",
    padx=40,
    pady=20,
    command=lambda: button_click(4),
    bg="grey",
    fg="white",
)
button_5 = Button(
    root,
    text="5",
    padx=75,
    pady=20,
    command=lambda: button_click(5),
    bg="grey",
    fg="white",
)
button_6 = Button(
    root,
    text="6",
    padx=75,
    pady=20,
    command=lambda: button_click(6),
    bg="grey",
    fg="white",
)
button_7 = Button(
    root,
    text="7",
    padx=40,
    pady=20,
    command=lambda: button_click(7),
    bg="grey",
    fg="white",
)
button_8 = Button(
    root,
    text="8",
    padx=75,
    pady=20,
    command=lambda: button_click(8),
    bg="grey",
    fg="white",
)
button_9 = Button(
    root,
    text="9",
    padx=75,
    pady=20,
    command=lambda: button_click(9),
    bg="grey",
    fg="white",
)
button_0 = Button(
    root,
    text="0",
    padx=40,
    pady=20,
    command=lambda: button_click(0),
    bg="grey",
    fg="white",
)
button_add = Button(
    root, text="+", padx=39, pady=20, command=button_add, bg="grey", fg="white"
)
button_equal = Button(
    root, text="=", padx=157, pady=20, command=button_equal, bg="grey", fg="white"
)
button_clear = Button(
    root, text="Clear", padx=147, pady=20, command=button_clear, bg="grey", fg="white"
)
button_subtract = Button(
    root, text="-", padx=41, pady=20, command=button_subtract, bg="grey", fg="white"
)
button_multiply = Button(
    root, text="*", padx=75, pady=20, command=button_multiply, bg="grey", fg="white"
)
button_divide = Button(
    root, text="??", padx=74, pady=20, command=button_divide, bg="grey", fg="white"
)
button_percentage = Button(
    root, text="%", padx=40, pady=20, command=button_percentage, bg="grey", fg="white"
)
button_fraction = Button(
    root, text="1/x", padx=40, pady=20, command=button_fraction, bg="grey", fg="white"
)
button_square = Button(
    root, text="x^2", padx=70, pady=20, command=button_square, bg="grey", fg="white"
)
button_square_root = Button(
    root, text="???x", padx=70, pady=20, command=button_square_root, bg="grey", fg="white"
)

# Place buttons on screen
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_percentage.grid(row=1, column=0)
button_square.grid(row=1, column=1)
button_square_root.grid(row=1, column=2)
button_fraction.grid(row=1, column=3)

button_0.grid(row=5, column=0)
button_clear.grid(row=5, column=1, columnspan=2)
button_add.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2)

button_subtract.grid(row=7, column=0)
button_multiply.grid(row=7, column=1)
button_divide.grid(row=7, column=2)

root.mainloop()
