# Libreria usada para obtener las keys del archivo keys.json
import json

# Libreria que maneja la programación de la subida
import schedule
import time

# Librerias necesarias para el manejo de las imagenes
import os.path
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from random import randint

# Librerias necesarias para comunicarse con las API's
import requests

# Libreria usada para comunicarse con twitter
import tweepy

# Función que devuelve la ruta absoluta
script_dir = os.path.dirname(os.path.abspath(__file__))

# Abrimos el archivo keys.json
with open(os.path.join(script_dir, 'keys.json'), 'r') as json_file:
	keys = json.load(json_file)


BEARER_TOKEN        = keys['bearer_token']
CONSUMER_KEY        = keys['consumer_key']
CONSUMER_SECRET     = keys['consumer_secret']
ACCESS_TOKEN        = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
USER_ID             = keys['userID']

client = tweepy.Client(consumer_key         = CONSUMER_KEY,
                       consumer_secret      = CONSUMER_SECRET,
                       access_token         = ACCESS_TOKEN,
                       access_token_secret  = ACCESS_TOKEN_SECRET,
                       bearer_token         = BEARER_TOKEN)

twitter_auth_keys = {
    "consumer_key"        : CONSUMER_KEY,
    "consumer_secret"     : CONSUMER_SECRET,
    "access_token"        : ACCESS_TOKEN,
    "access_token_secret" : ACCESS_TOKEN_SECRET
}


auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
)

auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
)

api = tweepy.API(auth)

# Función utilizada para subir las imagenes a Twitter
def uploadImage(imagen):
    media = api.media_upload(imagen)
    response = client.create_tweet(media_ids=[media.media_id])
    return response

ultimoNroImagen = 0

def crearImagen(valor):
    if (valor % 2 == 0):
        textoNumero = int(valor/2)
    else:
        textoNumero = float(valor/2)

    texto = str(textoNumero) + " pesos"
    longitud = len(texto)

    colorOutline = (0,0,0,255)

    # Elegimos un número random para abrir una imagen
    nroImagen = randint(0,3)
    print("Elegimos un número, numero elegido: " + str(nroImagen))

    global ultimoNroImagen

    # Si el número elegido es igual que el ultimo elegimos otro hasta que sea diferente.
    while(nroImagen == ultimoNroImagen):
        nroImagen = randint(0,3)
    
    ultimoNroImagen = nroImagen

    # Abrimos la Imagen
    img = Image.open(os.path.join(script_dir, 'img', '50cent-' + str(nroImagen) + '.png'))

    # Coordenadas de la imagen donde se coloca el texto
    x = (img.width - longitud*30) / 2
    y = img.height / 1.3

    # Llamamos el método para agregar graficos 2D a imagenes
    I1 = ImageDraw.Draw(img)

    # Detallamos fuente y tamaño
    fuente = ImageFont.truetype(os.path.join(script_dir, 'impact.ttf'), 65)
    
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
    img.save(os.path.join(script_dir, 'img', '50cent-dolar.png'))


def obtenerValorDolar():
    # Obtenemos el JSON con los valores del dolar
    respuestaAPI = requests.get("https://api.bluelytics.com.ar/v2/latest").json()

    # Parseamos el JSON
    dolarBlue = respuestaAPI['blue']['value_sell']
    dolarBlueFloat = float(dolarBlue)
    return dolarBlueFloat

def main():
    # Creamos la imagen con el valor del dolar obtenido.
    crearImagen(obtenerValorDolar())

    # Subimos la imagen a Twitter
    uploadImage(os.path.join(script_dir, 'img', '50cent-dolar.png'))

def responderTweets():
    # Abrimos el archivo que contiene el ID del último tweet contestado
    archivo_last_id = open(os.path.join(script_dir, 'last_id.txt'), 'r')
    last_id = int(archivo_last_id.read().strip())
    archivo_last_id.close()

    menciones = client.get_users_mentions(id = USER_ID, since_id = last_id, tweet_fields = ['text'], expansions = ['author_id'])

    if (menciones.data == None):
        print("No hay un tweet para responder")
        return
    
    print(menciones)
    # Se usa reversed para buscar desde el tweet más viejo al más nuevo
    for mention in reversed(menciones.data):
        id_nuevo = mention.id
        
        print("Usuario: " + str(mention.author_id))
        print("Texto: " + mention.text)
        
        # Solo contestar si en la mención está contenido el mensaje "#dolar"
        if '#dolar' in mention.text.lower():
            try:
                # Creamos la imagen
                crearImagen(obtenerValorDolar())

                # Subimos la imagen (API v1.1)
                media = api.media_upload(os.path.join(script_dir, 'img', '50cent-dolar.png'))
                
                # Damos like al tweet
                client.like(tweet_id = mention.id)

                # Respondemos
                client.create_tweet(in_reply_to_tweet_id = mention.id, media_ids=[media.media_id])
            except:
                print("Ya se contestó a {}".format(mention.id))

    # Cambiamos el ID del último tweet respondido por el nuevo 
    archivo_last_id = open(os.path.join(script_dir, 'last_id.txt'), 'w')
    archivo_last_id.write(str(id_nuevo))
    archivo_last_id.close()

# Programamos para que la función se ejecute todos los dias a las 20:00(UTC) / 17:00(ARG)
schedule.every().day.at("20:00").do(main)

while True:
    schedule.run_pending()
    responderTweets()

    # Pausamos el programa por 5 segundos
    time.sleep(5)