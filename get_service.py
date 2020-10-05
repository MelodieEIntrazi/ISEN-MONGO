import requests
import json
from pymongo import *
from pprint import pprint

#Il faut installer ça : python3 -m pip install 'mongo[srv]' dnspython

def get_vLille():

    #On tente de se connecter à la base de donnée
    try:
        client = MongoClient("mongodb+srv://dbUser:root@cluster0.5j4lv.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
        print("Connection réussie")
    except:
        print("Impossible de se connecter")
    db = client.info_velo
    lille = db.lille

    #On récupère les infos de l'api
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=10&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion&refine.commune=LILLE"
    reponse = requests.request("GET", url)
    reponse_json = json.loads(reponse.text.encode('utf8'))
    lille.insert_one(reponse_json)
    cursor = lille.find({})
    #for document in cursor: 
    #    pprint(document)

get_vLille()