class CharacterDAO:
    def __init__(self, character_api, location_api):
        self.__character_api = character_api
        self.__location_api = location_api

    def load(self):
        return self.__character_api.load()

    def load_current_system_id(self):
        char = self.load()
        return self.__location_api.load_current_system_id(char.id)
