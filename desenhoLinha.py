'''
Por enquanto ainda nao esta pronto
mas com um pouco de trabalho chegarei ao desenho da linha conforme
o requerimento do professor
'''
#https://www.youtube.com/watch?v=4Ok9CIHlI2U

from Tkinter import*
master = Tk()

canvas_width = 80
canvas_height = 40
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")

mainloop()
