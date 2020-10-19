import requests
import json
from get_Api_Url import getApi
from pymongo import *
from pprint import pprint
from set_data_ville import *

def get_vVille(ville):

    #On tente de se connecter à la base de donnée
    try:
        client = MongoClient("mongodb+srv://dbUser:root@cluster0.5j4lv.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
        print("Connection réussie")
    except:
        print("Impossible de se connecter")

    db = client.history_data
    #On récupère la bonne collection
    collection_ville = db.data_velo

    #On récupère la bonne adresse api pour la ville passée en paramètre
    url = getApi(ville)
    reponse = requests.request("GET", url)
    reponse_json = json.loads(reponse.text.encode('utf8'))
    if ville == "lyon":
        data = reponse_json.get("values", [])
    else : 
        data = reponse_json.get("records", [])  
    
    if ville == 'lille' : 
        data_to_insert = set_data_lille(data)
    elif ville == 'paris' : 
        data_to_insert = set_data_paris(data)
    elif ville == 'lyon' :
        data_to_insert = set_data_lyon(data)
    else :
        data_to_insert = set_data_rennes(data)

    collection_ville.insert_many(data_to_insert)


get_vVille('paris')
get_vVille('rennes')
get_vVille('lyon')
get_vVille('lille')