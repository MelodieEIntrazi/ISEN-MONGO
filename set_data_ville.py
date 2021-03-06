def set_data_lille(data):
    vlille = [
        {
            'name' : station.get('fields', {}).get('nom').title(),
            'geometry' : station.get('geometry'),
            'size'  :station.get('fields', {}).get('nbvelosdispo') + station.get('fields', {}).get('nbplacesdispo'),
            'source': {
                'dataset': 'Lille',
                'id_ext': station.get('fields', {}).get('libelle')
            },
            'tpe': station.get('fields', {}).get('type', '') == 'AVEC TPE'
        }
        for station in data
    ]
    return vlille

def set_data_paris(data):
    vlille = [
        {
            'name' : station.get('fields', {}).get('name').title(),
            'geometry' : station.get('geometry'),
            'size'  :station.get('fields', {}).get('capacity'),
            'source': {
                'dataset': 'Paris',
                'id_ext': int(station.get('fields', {}).get('stationcode'))
            },
            'tpe': station.get('fields', {}).get('type', '') == 'is_renting'
        }
        for station in data
    ]
    return vlille

def set_data_rennes(data):
    vlille = [
        {
            'name' : station.get('fields', {}).get('nom').title(),
            'geometry' : station.get('geometry'),
            'size'  :station.get('fields', {}).get('nombreemplacementsactuels'),
            'source': {
                'dataset': 'Rennes',
                'id_ext': int(station.get('fields', {}).get('idstation'))
            },
        }
        for station in data
    ]
    return vlille

def set_data_lyon(data):
    vlille = [
        {
            'name' : station.get('name').title(),
            'geometry' : {
                'type' : "Point",
                'coordinates' : [
                    station.get('lat'),
                    station.get('lng')
                ]
            },
            'size'  :station.get('bike_stands'),
            'source': {
                'dataset': 'Lyon',
                'id_ext': station.get('number')
            },
            'tpe': station.get('type', '') == 'is_renting'
        }
        for station in data
    ]
    return vlille