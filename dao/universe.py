class UniverseDAO:
    def __init__(self, universe_api):
        self.universe_api = universe_api

    def load_region(self, region_id):
        return self.universe_api.load_region(region_id)

    def load_constellation(self, constellation_id):
        constellation = self.universe_api.load_constellation(constellation_id)
        region = self.load_region(constellation.region_id)
        constellation.region = region
        return constellation

    def load_system(self, system_id):
        system = self.universe_api.load_system(system_id)
        constellation = self.load_constellation(system.constellation_id)
        system.constellation = constellation
        return system

    def load_races(self):
        return self.universe_api.load_races()

    def load_race(self, race_id):
        return self.universe_api.load_race(race_id)

    def load_stations(self, station_id):
        station = self.universe_api.load_stations(station_id)

        system = self.load_system(station.system_id)
        station.system = system

        type_ = self.load_type(station.type_id)
        station.type = type_

        race = self.load_race(station.race_id)
        station.race = race

        return station

    def load_type(self, type_id):
        type_ = self.universe_api.load_type(type_id)
        group = self.load_group(type_.group_id)
        type_.group = group
        return type_

    def load_group(self, group_id):
        group = self.universe_api.load_group(group_id)
        category = self.load_category(group.category_id)
        group.category = category
        return group

    def load_category(self, category_id):
        return self.universe_api.load_category(category_id)
