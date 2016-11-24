from Tkinter import *
class Kanvas:
    def __init__(self,raiz):
        self.canvas1 = Canvas(raiz, width=400, height=400,
        cursor='fleur', bd=10,
             bg='white')
        # self.canvas1.create_line(coord,fill='black') # proposta original
        # self.canvas1.pack()

coord = [] # define coord como uma variavel global
def callback(event):
    print "clicked at", event.x, event.y
    x1 = event.x
    y1 = event.y
    print x1, y1
    coord.append(x1) # guarda o valor da coordenada em x
    coord.append(y1) # guarda o valor da coordenada em y
    print coord
    instancia.canvas1.create_line(coord, fill='black')
    instancia.canvas1.pack()

instancia=Tk()
Kanvas(instancia)
instancia.bind("<Button-1>", callback)
instancia.canvas1 = Canvas(instancia, width=400, height=400,
    cursor='fleur', bd=10,
    bg='white')
instancia.mainloop()
