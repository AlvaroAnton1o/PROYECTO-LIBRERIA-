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
    
    
def delete():
    collection.delete_many({})

def show():
    data = collection.find({})
    return data

def getUser(value,val):
    data = collection.find_one({value:val})
    return data

def showby2(value,val):
    data = collection.find({value:val})
    return data

def getDataUser(userValue):
    # data = collection.find()
    data = collection.find({},{userValue:1,"_id":0})

    return data



def updateOne(value, val):
    collection.update_one(value,val)

connection('Libreria','Usuarios')
correo = getUser('correo','adolfo@gmail.com')

print(correo['contra'])