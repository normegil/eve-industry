class Structure:
    def __init__(self, id_, name, system_id, type_id, owner_id):
        self.id = id_
        self.name = name
        self.system_id = system_id
        self.type_id = type_id
        self.owner_id = owner_id
        self.__universe_dao = None
        self.__system = None

    def set_universe_dao(self, universe_dao):
        self.__universe_dao = universe_dao

    @property
    def system(self):
        if self.__system is None:
            self.__system = self.__universe_dao.load_system(self.system_id)
        return self.__system
