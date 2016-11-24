#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
ZetCode Tkinter tutorial
This script shows a simple window
on the screen.
author: Jan Bodnar
last modified: January 2011
website: www.zetcode.com
"""
from Tkinter import *
from ttk import Frame, Button, Style

class Example(Frame):
    def __init__(self, parent): # construtor da classe/frame

        #Frame.__init__(self, parent, background="white") # devido ao uso do style.theme não pude escolher o background aqui
        #self.parent = parent
        #self.initUI()

        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Computação Gráfica - UFT")
        self.style = Style()
        self.style.theme_use("default")
        self.pack() # apenas um teste

        # botao para tracar a reta
        okButton = Button(self, text="OK")
        okButton.place(x=300, y=430)
        okButton.pack()

        # botao para fechar a aplicação
        quitButton = Button(self, text="Fechar", command=self.quit) # o titulo do botao deveria ser Sair
        quitButton.place(x=300, y=460) # posiciona o botão nas coordenadas aqui especificadas
        quitButton.pack()

    # função usada para centralizar a janela, de acordo com a tela do notebook
    # por alguma razão, isso não está funcionando
    # claro, não estava sendo chamada na main
def centerWindow(self):
        w = 290
        h = 250
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

# função para captura das coordenadas, em pixels
coord = [] # melhorar isso aqui, não está legal assim
# a ideia de usar uma lista aqui, pode ser o diferencial para o desenho da polilinha
def callback(event):
    print "clicked at", event.x, event.y
    coord.append(event.x) # guarda o valor da coordenada em x
    coord.append(event.y) # guarda o valor da coordenada em y
    print coord # apenas para teste

    # tentativa de insercao de imagem junto ao frame
    filename = PhotoImage(file = "Eu1.jpg")
    image = canvas.create_image(50, 50, anchor=NE, image=filename)
    image.pack()

def main(): # método principal, chama outros métodos e os instancia
    root = Tk()
    #root.geometry("700x500+500+500") # define os parâmetros de lagura, altura e comprimento da janela
    app = Example(root)

    # trocar o uso do Frame pelo Canvas
    frame = Frame(root, width=700, height=500) # nesse caso, o tamanho do frame sobre o root é do msm tamanho do root
    frame.bind(centerWindow) # tentativa de chamada do metodo centerWindow
    frame.bind("<Button-1>", callback)
    frame.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
