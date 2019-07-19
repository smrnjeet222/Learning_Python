from tkinter import *
from tkinter import filedialog

def CloseWindow():
    window.destroy()


def OpenFile():
    try:
        t = filedialog.askopenfile(mode = 'r', title = "Select File ", filetypes = [("All Files", "*.*")])
        content.insert(END , t.read())
    except:
        print ("can't load the file")
    finally:
        if t:
            t.closse()  

def SaveFile():
    f = filedialog.asksaveasfile(mode='w', defaultextension = '.txt')
    if f is None:
        return
    try:    
        textUserWrote = str(content.get(1.0 , END))
        f.write(textUserWrote)
    except:
        print("Can't Ssave the file. ")
    finally:    
        f.close()

def Help():
    fBot = Frame(window)
    fBot.pack(side = BOTTOM)
    lbl = Label(fBot, text ="Commo'n it's just a simple application" )
    lbl.pack()


window = Tk()

window.title('TEXT EDITOR')

mainmenu = Menu(window)
window.config(menu = mainmenu)


filemenu = Menu(mainmenu)
mainmenu.add_cascade(label = 'File ' , menu = filemenu)
filemenu.add_command(label = 'Open', command = OpenFile )
filemenu.add_command(label = 'Save', command = SaveFile )
filemenu.add_separator()
filemenu.add_command(label = 'Close', command = CloseWindow )

editmenu = Menu(mainmenu)
mainmenu.add_cascade(label = 'Edit', menu = editmenu)

editmenu.add_command(label = "Undo")
editmenu.add_command(label = "Redo")

helpmenu = Menu(mainmenu)
mainmenu.add_cascade(label = 'Help', menu = helpmenu )
helpmenu.add_command(label = "Need Help?", command = Help)

content = Text(window , width = 70)

content.grid(row=0 , column =1 , padx =5, pady = 9)

window.mainloop()