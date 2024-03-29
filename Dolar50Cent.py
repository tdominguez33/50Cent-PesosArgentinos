# Libreria usada para obtener los datos desde mangoDB
import mongoDB

# Libreria usada para obtener las info del archivo info.json
import json

# Libreria que maneja la programación de la subida
import time
import schedule

# Librerias neesarias para el manejo de las imagenes
from crearImagen import crearImagen, elegirNroImagen
from random import randint
from crearImagen import CANTIDAD_IMAGENES

# Librerias necesarias para comunicarse con las API's
from dolarAPI import obtenerValorDolar

# Libreria usada para comunicarse con twitter
import tweepy

# Abrimos el archivo info.json
with open('info.json', 'r') as json_file:
	info = json.load(json_file)

BEARER_TOKEN        = info['bearer_token']
CONSUMER_KEY        = info['consumer_key']
CONSUMER_SECRET     = info['consumer_secret']
ACCESS_TOKEN        = info['access_token']
ACCESS_TOKEN_SECRET = info['access_token_secret']
USER_ID             = info['userID']

ULTIMAIMAGEN        = mongoDB.obtenerUltimaImagen()
ULTIMACOTIZACION    = mongoDB.obtenerUltimaCotizacion()
ULTIMOID            = mongoDB.obtenerUltimoID()
ULTIMOTIEMPOSUBIDA  = mongoDB.obtenerUltimoTiempoSubida()

# Cantidad de Segundos entre cada imagen que se sube
TIEMPOESPERA = 7200

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

# Funcion utilizada para captar menciones y responder a las que corresponda
def responderTweets():
    global ULTIMOID

    menciones = client.get_users_mentions(id = USER_ID, since_id = ULTIMOID, tweet_fields = ['text'], expansions = ['author_id'])

    if (menciones.data == None):
        print("No hay un tweet para responder")
        return
    
    # Se usa reversed para buscar desde el tweet más viejo al más nuevo
    for mention in reversed(menciones.data):
        id_nuevo = mention.id
        
        print("Usuario: " + str(mention.author_id))
        print("Texto: " + mention.text)
        
        # Solo contestar si en la mención está contenido el mensaje "#dolar"
        if '#dolar' in mention.text.lower():
            try:
                # Creamos la imagen, especificamos la funcion randint así elije una foto sin considerar la anterior que hay en el feed
                crearImagen(obtenerValorDolar(), randint(1, CANTIDAD_IMAGENES))

                # Subimos la imagen (API v1.1)
                media = api.media_upload('img/50cent-dolar.png')
                
                # Damos like al tweet
                client.like(tweet_id = mention.id)

                # Respondemos
                client.create_tweet(in_reply_to_tweet_id = mention.id, media_ids=[media.media_id])
            except:
                print("Ya se contestó a {}".format(mention.id))

    # Cambiamos el ID del último tweet respondido por el nuevo 
    ULTIMOID = str(id_nuevo)
    mongoDB.actualizarUltimoID(ULTIMOID)

def main():
    global ULTIMAIMAGEN
    ULTIMAIMAGEN = elegirNroImagen(ULTIMAIMAGEN)
    # Creamos la imagen con el valor del dolar obtenido
    crearImagen(obtenerValorDolar(), ULTIMAIMAGEN)

    # Subimos la imagen a Twitter
    uploadImage('img/50cent-dolar.png')

while True:
    # Verificamos si hay Tweets para responder
    responderTweets()
    
    # Si el valor del dolar cambia subimos un nuevo post
    if ((ULTIMACOTIZACION != obtenerValorDolar()) and (time.time() > (ULTIMOTIEMPOSUBIDA + TIEMPOESPERA))):
        main()
        ULTIMACOTIZACION = obtenerValorDolar()
        ULTIMOTIEMPOSUBIDA = time.time()
        mongoDB.actualizarUltimaCotizacion(str(obtenerValorDolar()))
        mongoDB.actualizarUltimaImagen(ULTIMAIMAGEN)
        mongoDB.actualizarUltimoTiempoSubida(str(time.time()))

    # Pausamos el programa por 10 segundos
    time.sleep(10)
