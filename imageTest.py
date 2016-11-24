import os,sys
# import Image o interpretador no consegue importar esta classe
from Tkinter import *
from PIL import Image
filePath = os.path.join()
img = Image.open('Eu1.jpg')
rgb = img.convert('RGB')
fileImage.load()
r, g, b = rgb.getpixel((200, 200))

print r, g, b
#for pixel in rgb.getdata():

# outro exemplo de abertura de imagem
'''
from PIL import Image
im = Image.open("dead_parrot.jpg") #Can be many different formats.
pix = im.load()
print im.size #Get the width and hight of the image for iterating over
print pix[x,y] #Get the RGBA Value of the a pixel of an image
pix[x,y] = value # Set the RGBA Value of the image (tuple)

'''
