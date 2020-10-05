import requests
import json
from pymongo import MongoClient
from pprint import pprint


client = MongoClient('localhost', 27017)
db = client.test_velo
lille = db.lille

def get_vLille():
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=10&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion&refine.commune=LILLE"
    reponse = requests.request("GET", url)
    reponse_json = json.loads(reponse.text.encode('utf8'))
    lille.insert_one(reponse_json)
    cursor = lille.find({})
    for document in cursor: 
        pprint(document)

get_vLille()

#mongodb+srv://admin:<password>@cluster0.5j4lv.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority
#lien pour se co à la bdd
#id  = admin mdp = root