import requests
import json
from pymongo import *
from pprint import pprint
from bson.son import SON

def user(ville, lat, lon, max_dist):

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

    collection_ville.create_index([("geometry", "2dsphere")])
    query = collection_ville.find({'geometry': {'$near': SON([('$geometry', SON([('type', 'Point'), ('coordinates', [lon, lat])])), ('$maxDistance', max_dist)])}} )

    for i in query.sort("timestamp", -1):
        print(i)

user("lille", 50.62486, 3.116677, 500)