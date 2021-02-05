import logging

from .asset import find_item

MAX_INT = 2147483647


class AssetLocation:
    def __init__(self, location_type, location_id):
        self.type = location_type
        self.id = location_id

    @property
    def station(self):
        logging.info(f"Could not load station for {self.type} - {self.id}")
        return None


class AssetLocationStation(AssetLocation):
    def __init__(self, location_type, location_id):
        AssetLocation.__init__(self, location_type, location_id)
        self.__universe_dao = None
        self.__station = None

    def set_universe_dao(self, universe_dao):
        self.__universe_dao = universe_dao

    @property
    def station(self):
        if self.__station is None:
            if self.id < MAX_INT:
                self.__station = self.__universe_dao.load_stations(self.id)
            else:
                self.__station = self.__universe_dao.load_structure(self.id)
        return self.__station


class AssetLocationItem(AssetLocation):
    def __init__(self, location_type, location_id):
        AssetLocation.__init__(self, location_type, location_id)
        self.__all_assets = []
        self.__station = None

    def set_assets(self, assets):
        self.__all_assets = assets

    @property
    def station(self):
        if self.__station is None:
            item = find_item(self.__all_assets, self.id)
            self.__station = item.location.station
        return self.__station
