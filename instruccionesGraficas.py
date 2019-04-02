#**************************************
# Produce una imagen con las isntrucciones para balancear las cargas
#
#******************************************

from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import itertools
import balanceoMinimizado as bm

#nuevas_pastillas = list(itertools.chain.from_iterable(bm.balance()))

filename_in = 'prueba.png'
filename_out = 'prueba1.png'

img = Image.new('RGB', (600,600), color = (200,200,200))
img.save(filename_in)

source_img = Image.open(filename_in)

fnt = ImageFont.truetype('D:/Python Scripts/Fonts/OpenSans-Regular.ttf', 20)

titulo_x = 200
titulo_y = 30

x_inicio = 150
ancho = 60
x_final = x_inicio + ancho

y_inicio = 80
alto = 20
y_final = y_inicio + alto 

separacion = 30
horizontal = 200
no_de_cargas = 24

diferencia_x = 35
diferencia_y = 15

pico_alto = 5
pico_base = 5

draw = ImageDraw.Draw(source_img)

draw.text((titulo_x, titulo_y), 'Balance de cargas', font=fnt,fill="black")

k=0
for j in range(1,round(no_de_cargas/2)+1):
    draw.line(((x_inicio, y_inicio+separacion*j+separacion*k),( x_final, y_inicio+separacion*j+separacion*k)), fill="black")
    draw.text(((x_inicio-diferencia_x, y_inicio+separacion*j+separacion*k-diferencia_y)),f'{j*2-1}',font=fnt,fill="black")
    draw.text(((x_final+diferencia_x-15 , y_inicio+separacion*j+separacion*k-diferencia_y)), f'{nuevas_pastillas[j-1+k*3]}',font=fnt,fill="black")
    draw.polygon([(x_final+pico_alto,y_inicio+separacion*j+separacion*k), (x_final, y_inicio+separacion*j+separacion*k+pico_base), (x_final,y_inicio+separacion*j+separacion*k-pico_base)],fill = "black")
    if j%3==0:
        k+=1

k=0
for j in range(1,round(no_de_cargas/2)+1):
    draw.line(((x_inicio+horizontal, y_inicio+separacion*j+separacion*k),( x_final+horizontal, y_inicio+separacion*j+separacion*k)), fill="black")
    draw.text(((x_inicio+horizontal-diferencia_x, y_inicio+separacion*j+separacion*k-diferencia_y)),f'{j*2}',font=fnt,fill="black")
    draw.text(((x_final+horizontal+diferencia_x-15 , y_inicio+separacion*j+separacion*k-diferencia_y)), f'{nuevas_pastillas[j+2+k*3]}',font=fnt,fill="black")
    draw.polygon([(x_final+horizontal+pico_alto,y_inicio+separacion*j+separacion*k), (x_final+horizontal, y_inicio+separacion*j+separacion*k+pico_base), (x_final+horizontal,y_inicio+separacion*j+separacion*k-pico_base)],fill = "black")
    if j%3==0:
        k+=1

#draw.line(((0, 00), (100, 100)), fill="black")
#draw.text((20, 70), "#####################", font=fnt,fill="black")

source_img.save(filename_out, "JPEG")