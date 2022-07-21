import requests

def obtenerValorDolar():
    # Obtenemos el JSON con los valores del dolar
    respuestaAPI = requests.get("https://api.bluelytics.com.ar/v2/latest").json()

    # Parseamos el JSON
    dolarBlue = respuestaAPI['blue']['value_sell']
    return float(dolarBlue)
