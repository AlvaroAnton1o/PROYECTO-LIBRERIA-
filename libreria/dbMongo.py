from flask import jsonify
from matplotlib.font_manager import json_load
from pymongo import MongoClient
import json

from requests import PreparedRequest

def connection (dbs,collection_name):
    
    global client 
    global db
    global collection 
    
    client = MongoClient('mongodb://localhost')
    db = client[dbs]
    collection = db[collection_name]
    
    

def save(data):
    collection.insert_one(data)
    
    
def update(data):
    collection.update_many(data)
    
def delete(filter):
    collection.delete_many(filter)

def show(nombreValor):
    data = collection.find({})
    libros = []
    cursor = data
    for i in cursor:
        libros.append(i[nombreValor])
    return libros

def getUser(value,val):
    data = collection.find_one({value:val})
    return data

def showby2(value,val,mostrar):
    data = collection.find({value:val})
    dataCategoria = []
    cursor = data
    for i in cursor:
        dataCategoria.append(i[mostrar])
    return dataCategoria

def getDataUser(userValue):
    # data = collection.find()
    data = collection.find({},{userValue:1,"_id":0})

    return data



def updateOne(value, val):
    collection.update_one(value,val)

connection('Libreria','Usuarios')
correo = getUser('correo','adolfo@gmail.com')

print(correo)

