class Region:
    def __init__(self, character_id=None, name=None, description=None):
        self.id = character_id
        self.name = name
        self.description = description
        self.constellations = []

    def add_constellation(self, constellation):
        self.constellations.append(constellation)

    def constellation(self, constellation_id):
        for constellation in self.constellations:
            if constellation.id == constellation_id:
                return constellation
        return None
