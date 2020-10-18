import requests
import json
from pymongo import *
from pprint import pprint

try:
    client = MongoClient("mongodb+srv://dbUser:root@cluster0.5j4lv.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
    print("Connection réussie")
except:
    print("Impossible de se connecter")
    
db = client.info_velo

def get_station_by_name(ville, name):

    #On créé un dictionnaire des collections de ville : 
    listOfCollection = {"lille" : db.lille, "lyon" : db.lyon, "rennes" : db.rennes, "paris" :  db.paris}
    #On récupère la bonne collection
    collection_ville = listOfCollection[ville]

    list_stations = collection_ville.find({"name": {"$regex" : name}})
    for i in list_stations : 
        print(i)

def delete_station(ville, name):

    #On créé un dictionnaire des collections de ville : 
    listOfCollection = {"lille" : db.lille, "lyon" : db.lyon, "rennes" : db.rennes, "paris" :  db.paris}
    #On récupère la bonne collection
    collection_ville = listOfCollection[ville]

    list_stations = collection_ville.delete_many({"name": {"$regex" : name}})

get_station_by_name('lille', 'Flers')
delete_station('lille', 'Flers')