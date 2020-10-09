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

def get_vLyon():
    try:
        client = MongoClient("mongodb+srv://dbUser:root@cluster0.5j4lv.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
        print("Connection réussie")
    except:
        print("Impossible de se connecter")
    db = client.info_velo
    lyon = db.lyon

    url = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=station-velov-grand-lyon&q=&facet=name&facet=commune&facet=bonus&facet=status&facet=available&facet=availabl_1&facet=availabili&facet=availabi_1&facet=last_upd_1"
    reponse = requests.request("GET", url)
    reponse_json = json.loads(reponse.text.encode('utf8'))
    lyon.insert_one(reponse_json)
    cursor = lyon.find({})

def get_vParis():
    try:
        client = MongoClient("mongodb+srv://dbUser:root@cluster0.5j4lv.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
        print("Connection réussie")
    except:
        print("Impossible de se connecter")
    db = client.info_velo
    paris = db.paris

    url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes"
    reponse = requests.request("GET", url)
    reponse_json = json.loads(reponse.text.encode('utf8'))
    paris.insert_one(reponse_json)
    cursor = paris.find({})

def get_vRennes():
    try:
        client = MongoClient("mongodb+srv://dbUser:root@cluster0.5j4lv.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
        print("Connection réussie")
    except:
        print("Impossible de se connecter")
    db = client.info_velo
    rennes = db.rennes

    url = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=etat-des-stations-le-velo-star-en-temps-reel&q=&facet=nom&facet=etat&facet=nombreemplacementsactuels&facet=nombreemplacementsdisponibles&facet=nombrevelosdisponibles"
    reponse = requests.request("GET", url)
    reponse_json = json.loads(reponse.text.encode('utf8'))
    rennes.insert_one(reponse_json)
    cursor = rennes.find({})

get_vLille()
get_vLyon()
get_vParis()
get_vRennes()


