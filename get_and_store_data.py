import requests
import json
from get_Api_Url import getApi
from pymongo import *
from pprint import pprint
import time

def get_and_store_data(ville):

    #On tente de se connecter à la base de donnée
    try:
        client = MongoClient("mongodb+srv://dbUser:root@cluster0.5j4lv.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
        print("Connection réussie")
    except:
        print("Impossible de se connecter")
    db = client.history_data
    #On créé un dictionnaire des collections de ville : 
    listOfCollection = {"lille" : db.lille, "lyon" : db.lyon, "rennes" : db.rennes, "paris" :  db.paris}
    #On récupère la bonne collection
    collection_ville = listOfCollection[ville]

    #On récupère la bonne adresse api pour la ville passée en paramètre
    url = getApi(ville)
    reponse = requests.request("GET", url)
    reponse_json = json.loads(reponse.text.encode('utf8'))
    collection_ville.insert_one(reponse_json)

get_and_store_data("lille")
get_and_store_data("rennes")
get_and_store_data("paris")
get_and_store_data("lyon")