class CharacterDAO:
    def __init__(self, character_api):
        self.character_api = character_api

    def load(self):
        return self.character_api.load()
