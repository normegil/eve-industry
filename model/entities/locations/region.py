class Region:
    def __init__(self, id_: int, name: str, description=None, constellation_ids=None):
        self.id = id_
        self.name = name
        self.description = description
        if constellation_ids is None:
            self.constellation_ids = []
        else:
            self.constellation_ids = constellation_ids
        self.__constellations = None
        self.__universe_dao = None

    def set_universe_dao(self, universe_dao):
        self.__universe_dao = universe_dao

    @property
    def constellations(self):
        if self.__constellations is None:
            self.__constellations = []
            for cons_id in self.constellation_ids:
                constellation = self.__universe_dao.load_constellation(cons_id)
                self.__constellations.append(constellation)
        return self.__constellations

    def constellation(self, constellation_id):
        for constellation in self.__constellations:
            if constellation.id == constellation_id:
                return constellation
        return None
