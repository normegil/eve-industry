class System:
    def __init__(self, character_id=None, name=None, constellation=None):
        self.id = character_id
        self.name = name
        self.constellation = constellation
        self.stations = []

    def add_station(self, station):
        self.stations.append(station)

    def station(self, station_id):
        for station in self.stations:
            if station.id == station_id:
                return station
        return None
