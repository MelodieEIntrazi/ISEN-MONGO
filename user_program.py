import requests
import json
from pymongo import *
from pprint import pprint
from bson.son import SON

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

    collection_ville.ensure_index([("geometry", GEOSPHERE)])
    query = collection_ville.find({"geometry" : SON([("$near", { "$geometry" : SON([("type", "Point"), ("coordinates", [lon, lat])])})])})
    for i in query:
        print(i)

user("lille", 50.62486, 3.116677)