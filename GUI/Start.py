from tkinter import *

def HandleButton():
    print('Button Clicked !!!!! ')

def PrintValue():
    print(userinput.get())

window = Tk()

fTop = Frame(window)
fTop.pack()
fBot = Frame(window)
fBot.pack(side = BOTTOM)


lbl1 = Label(fTop, text = 'Top')
lbl2 = Label(fTop, text = 'NEWTOP')
lbl3 = Label(fBot, text = 'Bottom')

lbl1.pack(side = LEFT)
lbl2.pack(side = RIGHT)
lbl3.pack()
    


userinput = StringVar()
userinput.trace('w', lambda name, index , mode : PrintValue())
e = Entry(window, fg = 'White', bd = 2, bg = 'grey', textvariable = userinput)
e.pack()

btn = Button(window, bd = 5, bg = 'black', fg = 'white', text = 'Log In',
            padx = 50, pady = 10, command = HandleButton)

btn.pack()

window.mainloop()
