from tkinter import *

win = Tk()

win.title("Simple Calculator")

e = Entry(win, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=8, pady=10)

# e.insert(0, "Enter Your Name")
def clr_button():
    e.delete(0,END)

def add_button():
    f_number = e.get()
    global f_num
    f_num = int(f_number)
    e.delete(0, END)

def equal_button():
    s_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(s_number))


def click_button(number):
    cur = e.get()
    e.delete(0, END)
    e.insert(0, str(cur) + str(number))
    return


button_1 = Button(win, text="1", padx=40, pady=20, command=lambda: click_button(1))
button_2 = Button(win, text="2", padx=40, pady=20, command=lambda: click_button(2))
button_3 = Button(win, text="3", padx=40, pady=20, command=lambda: click_button(3))
button_4 = Button(win, text="4", padx=40, pady=20, command=lambda: click_button(4))
button_5 = Button(win, text="5", padx=40, pady=20, command=lambda: click_button(5))
button_6 = Button(win, text="6", padx=40, pady=20, command=lambda: click_button(6))
button_7 = Button(win, text="7", padx=40, pady=20, command=lambda: click_button(7))
button_8 = Button(win, text="8", padx=40, pady=20, command=lambda: click_button(8))
button_9 = Button(win, text="9", padx=40, pady=20, command=lambda: click_button(9))
button_0 = Button(win, text="0", padx=40, pady=20, command=lambda: click_button(0))

button_add = Button(win, text="+", padx=40, pady=20, command=add_button)
button_equal = Button(win, text="=", padx=88, pady=20, command=equal_button)
button_clear = Button(win, text="CLR", padx=79, pady=20, command=clr_button)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)


win.mainloop()
