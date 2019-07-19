from tkinter import *

window = Tk()

labeluser = Label(window, text = 'Username : ')
labelpass = Label(window, text = 'Pswd : ' )

euser = Entry(window )
epass = Entry(window )

labeluser.grid(row = 0, sticky = E)
labelpass.grid(row = 1, sticky = E)
euser.grid(row = 0, column = 1)
epass.grid(row = 1, column = 1)


window.mainloop()