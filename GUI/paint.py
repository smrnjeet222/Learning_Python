from tkinter import *

window = Tk()

x1 = 0
y1 = 0

def callback(event):
    c.create_oval(event.x - 5 , event.y - 5 , event.x + 5 ,
                 event.y + 5 , fill= "#000000")

def draw(event):
    c.create_oval(event.x - 5 , event.y - 5 , event.x + 5,
                 event.y + 5 , fill= "#000000")

def DrawRectangle(event):
    global draw ,x1, y1
    if draw:
        c.create_rectangle(x1 , y1 , event.x ,event.y , fill = "Red")
        draw = False
    else:
        x1 = event.x
        y1 = event.y 
        draw = True

c = Canvas(window , width= 800 , height =500)
c.pack()
c.bind("<Button-1>", callback)
c.bind("<B1-Motion>", draw)
c.bind("<Button-3>",DrawRectangle)

draw= False

window.mainloop()