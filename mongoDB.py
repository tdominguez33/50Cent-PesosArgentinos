from pymongo import MongoClient
import json

with open('info.json', 'r') as json_file:
	info = json.load(json_file)

cluster = MongoClient(info['mongoDBLogin'])
database = cluster['50Cent']
collection = database['Info']

# Codigo utilziado para cargar los datos en la DB por primera vez
# post = {"_id": 0, "ultimoID": 1549800073625800704, "ultimaCotizacion": 337.0, "ultimaImagen": 2}
# collection.insert_one(post)

def actualizarUltimoID(ID):
    collection.update_one({"_id": 0}, {"$set":{"ultimoID": ID}})

def actualizarUltimaCotizacion(cotizacion):
    collection.update_one({"_id": 0}, {"$set":{"ultimaCotizacion": cotizacion}})

def actualizarUltimaImagen(imagen):
    collection.update_one({"_id": 0}, {"$set":{"ultimaImagen": imagen}})

def actualizarUltimoTiempoSubida(epoch):
    collection.update_one({"_id": 0}, {"$set":{"ultimoTiempoSubida": epoch}})

def obtenerUltimoID():
    id = collection.find_one({"_id": 0})
    return str(id['ultimoID'])

def obtenerUltimaCotizacion():
    id = collection.find_one({"_id": 0})
    return float(id['ultimaCotizacion'])

def obtenerUltimaImagen():
    id = collection.find_one({"_id": 0})
    return int(id['ultimaImagen'])

def obtenerUltimoTiempoSubida():
    id = collection.find_one({"_id": 0})
    return float(id['ultimoTiempoSubida'])
    