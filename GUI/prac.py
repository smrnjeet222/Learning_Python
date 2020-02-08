from tkinter import *

window = Tk()

# mylabel1 = Label(window, text="Python").grid(row=0, column=0)
# mylabel2 = Label(window, text="C++").grid(row=1, column=0)

e = Entry(window, width=20, borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name")


def myclick():
    mesg = "Hello " + e.get() + " !"
    mylabel = Label(window, text=mesg)
    mylabel.pack()


button1 = Button(window, text="click me",
                 padx=10, pady=5,
                 command=myclick,
                 fg="yellow", bg="red")

button1.pack()

window.mainloop()
