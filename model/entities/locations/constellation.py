class Constellation:
    def __init__(self, character_id=None, name=None, region=None):
        self.id = character_id
        self.name = name
        self.region = region
        self.systems = []

    def add_system(self, system):
        self.systems.append(system)

    def system(self, system_id):
        for system in self.systems:
            if system.id == system_id:
                return system
        return None
