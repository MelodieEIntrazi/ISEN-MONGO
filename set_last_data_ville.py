def set_data_lille(data):
    vlille = [
        {
            'name' : station.get('fields', {}).get('nom').title(),
            'geometry' : station.get('geometry'),
            'nbvelosdispo' : station.get('fields', {}).get('nbvelosdispo'),
            'nbplacesdispo' : station.get('fields', {}).get('nbplacesdispo'),
            'source': {
                'dataset': 'Lille',
                'id_ext': station.get('fields', {}).get('libelle')
            },
            'tpe': station.get('fields', {}).get('type', '') == 'AVEC TPE',
            'en service' : True, 
            'timestamp' : station.get('record_timestamp')
        }
        for station in data
    ]
    return vlille

def set_data_paris(data):
    vlille = [
        {
            'name' : station.get('fields', {}).get('name').title(),
            'geometry' : station.get('geometry'),
            'nbvelosdispo' : station.get('fields', {}).get('numbikesavailable'),
            'nbplacesdispo' : station.get('fields', {}).get('numdocksavailable'),
            'source': {
                'dataset': 'Paris',
                'id_ext': int(station.get('fields', {}).get('stationcode'))
            },
            'tpe': station.get('fields', {}).get('type', '') == 'is_renting',
            'en service' :  True, 
            'timestamp' : station.get('record_timestamp')
        }
        for station in data
    ]
    return vlille

def set_data_rennes(data):
    vlille = [
        {
            'name' : station.get('fields', {}).get('nom').title(),
            'geometry' : station.get('geometry'),
            'nbvelosdispo' : station.get('fields', {}).get('nombrevelosdisponibles'),
            'nbplacesdispo' : station.get('fields', {}).get('nombreemplacementsdisponibles'),
            'source': {
                'dataset': 'Rennes',
                'id_ext': int(station.get('fields', {}).get('idstation')), 
            },
            'en service': True,
            'timestamp': station.get('record_timestamp')
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
            'nbvelosdispo' : station.get('available_bikes'),
            'nbplacesdispo' : station.get('available_bike_stands'),
            'source': {
                'dataset': 'Lyon',
                'id_ext': station.get('number')
            },
            'tpe': station.get('banking'), 
            'en service' :  True,
            'timestamp': station.get('last_update')
        }
        for station in data
    ]
    return vlille