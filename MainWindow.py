from Tkinter import *


class Kanvas:
    def __init__(self, raiz):
        self.canvas1 = Canvas(raiz, width=400, height=400,
                              cursor='fleur', bd=10,
                              bg='red')
        self.canvas1.create_line(200, 200, 230, 230, 100, 150, fill='black')
        self.canvas1.pack()

    instancia = Tk()
    Kanvas(instancia)
    instancia.mainloop()
