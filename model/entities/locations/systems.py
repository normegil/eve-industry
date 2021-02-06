class System:
    def __init__(self, character_id=None, name=None, constellation=None):
        self.id = character_id
        self.name = name
        self.constellation = constellation
        self.stations = []
        self.manufacturing = None
        self.researching_time_efficiency = None
        self.researching_material_efficiency = None
        self.copying = None
        self.invention = None
        self.reaction = None

    def merge_with(self, cost_indices):
        self.manufacturing = cost_indices.manufacturing
        self.researching_time_efficiency = cost_indices.researching_time_efficiency
        self.researching_material_efficiency = cost_indices.researching_material_efficiency
        self.copying = cost_indices.copying
        self.invention = cost_indices.invention
        self.reaction = cost_indices.reaction

    def add_station(self, station):
        self.stations.append(station)

    def station(self, station_id):
        for station in self.stations:
            if station.id == station_id:
                return station
        return None
