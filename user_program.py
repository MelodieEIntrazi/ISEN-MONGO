import requests
import json
from pymongo import *
from pprint import pprint

def user(ville, lat, lon):

    try:
        client = MongoClient("mongodb+srv://dbUser:root@cluster0.5j4lv.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
        print("Connection réussie")
    except:
        print("Impossible de se connecter")
    
    db = client.info_velo

    #On créé un dictionnaire des collections de ville : 
    listOfCollection = {"lille" : db.lille, "lyon" : db.lyon, "rennes" : db.rennes, "paris" :  db.paris}
    #On récupère la bonne collection
    collection_ville = listOfCollection[ville]

    list_stations = collection_ville.find({"geometry" : {'$near' : [lon, lat], '$maxDistance': 0.10}})
    list_stations_2 = collection_ville.find({"geometry": {'$near': {'$geometry': {type:"Point", "coordinates":[lon,lat]}, '$maxDistance':500 }}})
    
