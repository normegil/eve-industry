class Character:
    def __init__(self, character_dao, universe_dao):
        self.__character_dao = character_dao
        self.__universe_dao = universe_dao

    def current_system(self):
        system_id = self.__character_dao.load_current_system_id()
        return self.__universe_dao.load_system(system_id)
