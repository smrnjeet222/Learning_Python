from tkinter import *

window = Tk()

c = Canvas(window , width = 300, height = 200)
c.pack()

c.create_line(0, 0 , 300, 200, fill ='red')
c.create_line(0, 200, 300, 0,fill = 'green')

c.create_rectangle(75,50, 225 ,150, fill ='grey')
c.create_oval(75,50, 225 ,150 ,fill ='yellow')
c.create_oval(149,99,151,101, fill ='black')

window.mainloop()

