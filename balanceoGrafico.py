#************************************
# Produce y guarda una imagen con las instrucciones
#***********************************************

from tkinter import *
from PIL import Image
from PIL import ImageGrab
import pdb
import itertools
import balanceoMinimizado as bm

root = Tk()
root.geometry('300x300')

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb   

c = Canvas(root, height=600, width=600, bg=_from_rgb((200, 200, 200)))


titulo_x = 300
titulo_y = 50

x_inicio = 150
ancho = 60
x_final = x_inicio + ancho

y_inicio = 80
alto = 20
y_final = y_inicio + alto 

separacion = 30
horizontal = 200
no_de_cargas = 24
k=0

#nuevas_pastillas = list(itertools.chain.from_iterable(bm.balance()))

c.create_text(titulo_x, titulo_y, font =('', 12), text = f'Balance de cargas')

for j in range(1,round(no_de_cargas/2)+1):
    c.create_line(x_inicio, y_inicio+separacion*j+separacion*k, x_final, y_inicio+separacion*j+separacion*k, arrow=LAST)
    c.create_text(x_inicio-15, y_inicio+separacion*j+separacion*k,text = f'{j*2-1}')
    c.create_text(x_final+15, y_inicio+separacion*j+separacion*k, text = f'{nuevas_pastillas[j-1+k*3]}')
    if j%3==0:
        k+=1
k=0        
for j in range(1,round(no_de_cargas/2)+1):
    c.create_line(x_inicio+horizontal, y_inicio+separacion*j+separacion*k, x_final+horizontal, y_inicio+separacion*j+separacion*k, arrow=LAST)
    c.create_text(x_inicio-15+horizontal, y_inicio+separacion*j+separacion*k, text = f'{j*2}')
    c.create_text(x_final+15+horizontal, y_inicio+separacion*j+separacion*k, text = f'{nuevas_pastillas[j+2+k*3]}')
    if j%3==0:
        k+=1

#c.create_text(10,10,text = "5")


#for j in range(cargas):
#    l = c.create_polygon(x_inicio,y_inicio+separacion*j,x_inicio,y_final+separacion*j,
#                         x_final,y_final+separacion*j,x_final,y_inicio+separacion*j)

c.pack()

#pdb.set_trace()
#def save_as_png(canvas,fileName):
#    # save postscipt image 
#    canvas.postscript(file = fileName + '.eps') 
#    # use PIL to convert to PNG 
#    img = Image.open(fileName + '.eps') 
#    img.save(fileName + '.png', 'png')
#
#save_as_png(c,'prueba')

#def getter(widget):
#    x=root.winfo_rootx()+widget.winfo_x()
#    y=root.winfo_rooty()+widget.winfo_y()
#    x1=x+widget.winfo_width()
#    y1=y+widget.winfo_height()
#    ImageGrab.grab((x,y,x1,y1)).save("prueba.png")
    
#getter(c)

root.mainloop()