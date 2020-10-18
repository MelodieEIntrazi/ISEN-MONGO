import requests
import json
from pymongo import *
from pprint import pprint
from get_last_data import *

def user(ville, lat, lon):
    list_stations = db.ville.find({"geometry" : {$near : [lon, lat], $maxDistance: 0.10}})
    list_stations_2 = db.ville.find({"geometry": {$near: {$geometry: {type:"Point", coordinates:[lon,lat]}, $maxDistance:500 }}})