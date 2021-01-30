from model.entities import Character


class CharacterCache:
    def __init__(self, cache, api):
        self.cache = cache
        self.api = api

    def load(self):
        id_ = self.cache["character.id"]
        if id_ is not None:
            name = self.cache["character.name"]
            return Character(int(id_), name)

        char = self.api.load()
        self.cache["character.id"] = char.id
        self.cache["character.name"] = char.name
        return char

    def load_assets(self, character_id):
        return self.api.load_assets(character_id)
