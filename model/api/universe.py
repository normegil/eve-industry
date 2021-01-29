class Universe:
    def __init__(self, universe_dao):
        self.universe_dao = universe_dao

    def region(self, region_id):
        return self.universe_dao.load_region(region_id)

    def constellation(self, constellation_id):
        return self.universe_dao.load_constellation(constellation_id)

    def system(self, system_id):
        return self.universe_dao.load_system(system_id)

    def station(self, station_id):
        return self.universe_dao.load_stations(station_id)