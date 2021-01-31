class Universe:
    def __init__(self, universe_dao, character_dao):
        self.universe_dao = universe_dao
        self.character_dao = character_dao

    def region(self, region_id):
        return self.universe_dao.load_region(region_id)

    def constellation(self, constellation_id):
        return self.universe_dao.load_constellation(constellation_id)

    def system(self, system_id):
        return self.universe_dao.load_system(system_id)

    def station(self, station_id):
        return self.universe_dao.load_stations(station_id)

    def all_character_groups(self):
        char = self.character_dao.load()
        categories = self.character_dao.load_assets_by_category(char.id)
        groups = []
        for category in categories:
            groups.extend(category.groups)
        return groups
