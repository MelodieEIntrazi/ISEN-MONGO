import requests
import json
from pymongo import *
import pymongo
from pprint import pprint


def calculte_average(ville):
        
    #On tente de se connecter à la base de donnée
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

    liste = collection_ville.aggregate([
        {"$addFields" : {"date":{"$toDate" : "$timestamp"}}},
        {"$addFields" : {"heure":{"$hour" : "$date"}}},
        {"$match" : {"heure" : {"$in" : [8,10]}}},
        {"$group" : {"_id": "$name",
            "total_velo" : {"$sum" : "$nbvelosdispo"}, 
            "total_place" : {"$sum" : "$nbplacesdispo"}
        } },
        {"$addFields" : {"total" : {"$sum" : ["$total_velo", "$total_place"] } } },
        {"$match" : {"total" : {"$gt" : 0} } },
        {"$addFields" : {"ratio" : {"$avg" : {"$divide" : ["$total_velo", "$total"] } } } }, 
    ])

    for i in liste:
        if(i['ratio'] <= 0.2) :
            print('nom de la station : ', i['_id'], ' avec un ratio de : ', i['ratio'])
        #print('nom : ', i['_id'], 'total : ', i['total'], 'moyenne : ', i['ratio'], 'heure : ', i['heure'])

calculte_average('lyon')