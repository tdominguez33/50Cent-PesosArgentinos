from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from random import randint

CANTIDAD_IMAGENES = 11

def elegirNroImagen(ultimoNroImagen):
    # Elegimos un número random para abrir una imagen
    nroImagen = randint(1, CANTIDAD_IMAGENES)

    # Si el número elegido es igual que el ultimo elegimos otro hasta que sea diferente
    while(ultimoNroImagen == nroImagen):
        nroImagen = randint(1, CANTIDAD_IMAGENES)
    
    print("Elegimos un número, numero elegido: " + str(nroImagen))

    return nroImagen

def crearImagen(valor, nroImagen):
    # Chequeamos si el número es entero o no para ver si lo guardamos como un int o como float
    if (valor % 2 == 0):
        textoNumero = int(valor/2)
    else:
        textoNumero = float(valor/2)

    texto = str(textoNumero) + " pesos"

    colorOutline = (0,0,0,255)

    # Abrimos la Imagen
    img = Image.open('img/50cent-' + str(nroImagen) + '.png')

    # Detallamos fuente y tamaño
    fuente = ImageFont.truetype('impact.ttf', 1)

    # Porcentaje de Imagen que va a ocupar el texto
    fraccion = 0.80
    
    # Tamaño inicial de la fuente
    fontsize = 1

    # Aumentamos el tamaño de la fuente hasta que el tamaño sea mayor a la fracción deseada
    while fuente.getsize(texto)[0] < fraccion*img.size[0]:
        fontsize += 1
        fuente = ImageFont.truetype('impact.ttf', fontsize)

    # Coordenadas de la imagen donde se coloca el texto
    x = (img.width - fuente.getsize(texto)[0]) / 2
    y = img.height / 1.4

    # Nos aseguramos que el texto no quede cortado por debajo de la imagen
    while img.height - y < fuente.getsize(texto)[1] + 10:
        y -= 1

    # Llamamos el método para agregar graficos 2D a imagenes
    I1 = ImageDraw.Draw(img)
    
    # Añadimos texto a la imagen
    I1.text((x-1, y-1), texto, font=fuente, fill=colorOutline)
    I1.text((x+1, y-1), texto, font=fuente, fill=colorOutline)
    I1.text((x-1, y+1), texto, font=fuente, fill=colorOutline)
    I1.text((x+1, y+1), texto, font=fuente, fill=colorOutline)
    I1.text((x-2, y-2), texto, font=fuente, fill=colorOutline)
    I1.text((x+2, y-2), texto, font=fuente, fill=colorOutline)
    I1.text((x-2, y+2), texto, font=fuente, fill=colorOutline)
    I1.text((x+2, y+2), texto, font=fuente, fill=colorOutline)
    I1.text((x, y), texto, font=fuente, fill=(255,255,255,255))
    I1.text((x, y), texto, font=fuente, fill=(255,255,255,255))
    
    # Guardamos la imagen
    img.save('img/50cent-dolar.png')
