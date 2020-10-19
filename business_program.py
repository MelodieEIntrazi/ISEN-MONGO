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

    #On recherche la station en fonction du nom et on recupère les informations les plus récentes dans station : 
    list_stations = collection_ville.find({"name": {"$regex" : name_station}}).sort("timestamp", -1)
    station = list_stations[0]

    #Si plusieurs stations correspondent au nom donné on les récupère et on les stocke dans la liste list_station_name 
    list_stations_name = list_stations.distinct("name")

    if(len(list_stations_name) > 1) :
        print("Les stations suivantes correspondent à la recherche :")
        i = 0
        for station_name in list_stations_name : 
            print(i , ' ) ' , station_name)
            i += 1
        number_station = int(input("Choissisez le numéro de la station voulue : " ))
        #On effectue une nouvelle recherche pour garder la station correspondant à celle selectionné par l'utlisateur
        name_station = list_stations_name[number_station]
        station = collection_ville.find({"name": {"$regex" : name_station}}).sort("timestamp", -1)[0]
    
    print("Vous avez choisi la station ", station.get('name'))
    return station


def delete_station(ville):

    #On créé un dictionnaire des collections de ville : 
    listOfCollection = {"lille" : db.lille, "lyon" : db.lyon, "rennes" : db.rennes, "paris" :  db.paris}
    #On récupère la bonne collection
    collection_ville = listOfCollection[ville]

    #On récupère le nom de la station
    station = get_station_by_name(ville)
    station_name = station.get('name')

    #On supprime toutes les stations avec ce nom
    collection_ville.delete_many({"name": station_name})
    print("Toutes les données concernant ", station_name, " ont été supprimés")



def update_station(ville):

    #On créé un dictionnaire des collections de ville : 
    listOfCollection = {"lille" : db.lille, "lyon" : db.lyon, "rennes" : db.rennes, "paris" :  db.paris}
    #On récupère la bonne collection
    collection_ville = listOfCollection[ville]

    #On récupère le nom de la station
    station = get_station_by_name(ville)
    station_name = station.get('name')

    #On affiche la station et on récupère les clés dans une liste
    i = 0 
    liste_cle = []
    for cle, valeur in station.items() :
        liste_cle.append(cle)
        if(i != 0 and i!=2 and i!=5 and i!=8):
            print(i, " ) ", cle, " : ", valeur)
        i += 1

    #On récupère le champ à modifier
    numero_cle = int(input("Quel champ voulez-vous modifier : "))
    nom_cle = liste_cle[numero_cle]
    print(nom_cle)

    #On récupère la valeur à modifier : 
    nouvelle_valeur = input("Par quelle valeur voulez-vous modifier le champ : ")

    #On update la station
    collection_ville.update_many({nom_cle : station.get(nom_cle)}, {"$set" : {nom_cle : nouvelle_valeur}})

    #On récupère la station mise à jour par son nom :
    if(numero_cle == 1):
        update_list = collection_ville.find({'name' : nouvelle_valeur}).sort("timestamp", -1)[0]
    else :
        update_list = collection_ville.find({'name': station.get('name')}).sort("timestamp", -1)[0]
    print("Voici la station après modification : ", update_list)

#get_station_by_name('rennes')
#update_station('rennes')
#delete_station('lyon')