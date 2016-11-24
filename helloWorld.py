#HelloWorld.py
import sys
import Tkinter
from Tkinter import*

'''
Além de desenhar um frame na tela, ao clicar no frame faz-se a captura das coordenadas em x e y
'''

root = Tkinter.Tk() # chama a janela de root
root.title( 'Oi' ) # define o titulo da janela
l = Tkinter.Label(root, text="Hello, world!\n\n\nTkinter on PocketPC!\n\n\nSee http://pythonce.sf.net.")
b = Tkinter.Button(root, text='Quit', command=root.destroy) # evento para derrubar a aplicação 
l.pack() # l representa o Label
b.pack() # b representa o Button

def callback(event):
    print "clicked at", event.x, event.y
frame = Frame(root, width=300, height=300)
frame.bind("<Button-1>", callback)
frame.pack()

#root.callback()
root.geometry("300x300+300+300")
root.mainloop()

# alteracoes aqui
'''
def callback(event):
    canvas = event.widget
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    print canvas.find_closest(x, y)
'''
