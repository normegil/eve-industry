class Constellation:
    def __init__(self, id_, name, region_id, system_ids):
        self.id = id_
        self.name = name
        self.region_id = region_id
        self.__region = None
        self.system_ids = system_ids
        self.__systems = None
        self.__universe_dao = None

    def set_universe_dao(self, universe_dao):
        self.__universe_dao = universe_dao

    @property
    def region(self):
        if self.__region is None:
            self.__region = self.__universe_dao.load_region(self.region_id)
        return self.__region

    @property
    def systems(self):
        if self.__systems is None:
            self.__systems = []
            for sys_id in self.system_ids:
                system = self.__universe_dao.load_system(sys_id)
                self.__systems.append(system)
        return self.__systems

    def system(self, system_id):
        for system in self.systems:
            if system.id == system_id:
                return system
        return None
