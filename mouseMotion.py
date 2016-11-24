from Tkinter import *

def motion(event):# metodo de captura das coordenadas
    print("Mouse position: (%s %s)" % (event.x, event.y))
    return

master = Tk() # instancia do frame, or something like that
whatever_you_do = "Whatever you do will be insignificant,\nbut it is very important that you do it.\n (Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('ubuntu mono', 24, 'italic'))
msg.bind('<Motion>',motion)
msg.pack()
mainloop()
