import requests
import json
from pymongo import *
import pymongo
from pprint import pprint

try:
    client = MongoClient("mongodb+srv://dbUser:root@cluster0.5j4lv.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
    print("Connection réussie")
except:
    print("Impossible de se connecter")
    
db = client.info_velo

def get_station_by_name(ville):

    name_station = input("Entrer le nom de la station recherchée : ")

    #On créé un dictionnaire des collections de ville : 
    listOfCollection = {"lille" : db.lille, "lyon" : db.lyon, "rennes" : db.rennes, "paris" :  db.paris}
    #On récupère la bonne collection
    collection_ville = listOfCollection[ville]

    list_stations = collection_ville.find({"name": {"$regex" : name_station}}).sort("timestamp", -1)
    list_stations_name = list_stations.distinct("name")
    station = list_stations[0]

    if(len(list_stations_name) > 1) :
        print("Les stations suivantes correspondent à la recherche :")
        i = 0
        for station_name in list_stations_name : 
            print(i , ' ) ' , station_name)
            i += 1
        number_station = int(input("Choissisez le numéro de la station voulue : " ))
        name_station = list_stations_name[number_station]
        station = collection_ville.find({"name": {"$regex" : name_station}}).sort("timestamp", -1)[0]
    
    print(station)

        
    

def delete_station(ville, name):

    #On créé un dictionnaire des collections de ville : 
    listOfCollection = {"lille" : db.lille, "lyon" : db.lyon, "rennes" : db.rennes, "paris" :  db.paris}
    #On récupère la bonne collection
    collection_ville = listOfCollection[ville]

    list_stations = collection_ville.delete_many({"name": {"$regex" : name}})

get_station_by_name('lille')