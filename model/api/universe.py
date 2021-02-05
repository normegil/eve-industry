from model.dao import UniverseDAO


class Universe:
    def __init__(self, universe_dao: UniverseDAO):
        self.universe_dao = universe_dao

    def regions(self):
        return self.universe_dao.load_regions()

    def region(self, region_id: int):
        return self.universe_dao.load_region(region_id)

    def constellation(self, constellation_id: int):
        return self.universe_dao.load_constellation(constellation_id)

    def system(self, system_id: int):
        return self.universe_dao.load_system(system_id)

    def station(self, station_id: int):
        return self.universe_dao.load_stations(station_id)
