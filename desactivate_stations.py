import requests
import json
from pymongo import *
from pprint import pprint
from bson.son import SON

def descativate(ville):
    #Tableau de coordonnées :
    # 2 stations dans le polygone 
    tab = [[[3.04876, 50.634272], [3.0530628, 50.6357694,], [3.066667, 50.633333], [3.051335, 50.62767], [3.04876, 50.634272]]]
    # 1 station dans le polygone
    tab2 = [[[3.04876, 50.634272], [3.0530628, 50.6357694,], [3.066667, 50.633333], [3.049479, 50.631634], [3.04876, 50.634272]]]
    
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

    #On crée l'index et on liste les stations présentes dans le polygone
    collection_ville.create_index([("geometry", "2dsphere")])
    find_in_polygon = collection_ville.find({'geometry': {'$geoWithin': SON([('$geometry', SON([('type', 'Polygon'), ('coordinates', tab)]))])}}).sort("timestamp", -1)
    list_stations_name = find_in_polygon.distinct("name")
    station = find_in_polygon[0]

    if(len(list_stations_name) > 1) :
        print("Les stations suivantes se situent dans le polygone et ont été désactivées:")
        i = 0
        for station_name in list_stations_name : 
            print("\n")
            print(i , ' ) ' , station_name)
            i += 1
            #On désactive la station
            collection_ville.update_many({"name" : station_name}, {"$set" : {"en service" : False}})
            #On affiche ses informations les plus récentes
            station = collection_ville.find({"name": {"$regex" : station_name}}).sort("timestamp", -1)[0]
            print(station)
    else:
        print("dans else")
        collection_ville.update_many({"name" : list_stations_name[0]}, {"$set" : {"en service" : False}})
        print("Une station est dans le polygone : ", list_stations_name[0])
        print("Elle a été désactivée : \n" , station)


descativate("lille")