from model.entities import Character


class CharacterCache:
    def __init__(self, conn, api):
        self.conn = conn
        self.api = api

    def load(self):
        id = self.conn.get("character.id")
        if id is not None:
            name = self.conn.get("character.name")
            return Character(int(id), name)

        char = self.api.load()
        self.conn.set("character.id", char.id)
        self.conn.set("character.name", char.name)
        return char

    def load_assets(self, character_id):
        return self.api.load_assets(character_id)
