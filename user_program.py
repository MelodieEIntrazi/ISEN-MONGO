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

    #On crée un index et on cherche toutes les stations proches du user
    collection_ville.create_index([("geometry", "2dsphere")])
    query = collection_ville.find({'geometry': {'$near': SON([('$geometry', SON([('type', 'Point'), ('coordinates', [lon, lat])])), ('$maxDistance', max_dist)])}}).sort("timestamp", -1)
    list_stations_name = query.distinct("name")
    station = query[0]
    print("\n", ville, "/ Latitude :", lat, "- Longitude :", lon, "/ Distance max :", max_dist, "mètres")
    
    #S'il y a plusieurs stations qui sont proches :
    if(len(list_stations_name) > 1) :
        print("Les stations suivantes se situent près de vous :")
        i = 0
        for station_name in list_stations_name : 
            print(i , ' ) ' , station_name)
            i += 1
        number_station = int(input("Choissisez le numéro de la station voulue : " ))
        name_station = list_stations_name[number_station]
        station = collection_ville.find({"name": {"$regex" : name_station}}).sort("timestamp", -1)[0]
    
    elif (len(list_stations_name) == 1):
        print("La station proche de vous est ", list_stations_name[0])
        print("\n Ses informations :")
        station = collection_ville.find({"name": {"$regex" : list_stations_name[0]}}).sort("timestamp", -1)[0]
    print(station)

user("lille", 50.634272, 3.04876, 1000)