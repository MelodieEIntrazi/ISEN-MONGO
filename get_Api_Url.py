def getApi(ville):
    listOfUrl = {"lille" : "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=10&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion&refine.commune=LILLE",
    "lyon" : "https://download.data.grandlyon.com/ws/rdata/jcd_jcdecaux.jcdvelov/all.json?maxfeatures=100&start=1",
    "paris" : "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes",
    "rennes" :"https://data.explore.star.fr/api/records/1.0/search/?dataset=vls-stations-etat-tr&q=&facet=nom&facet=etat&facet=nombreemplacementsactuels&facet=nombreemplacementsdisponibles&facet=nombrevelosdisponibles"}

    return listOfUrl[ville]

