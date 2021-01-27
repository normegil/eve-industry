class Characters:
    def __init__(self, character_dao):
        self.character_dao = character_dao
        self.current_character = self.character_dao.load()

    def assets(self):
        return self.character_dao.load_assets_by_category(self.current_character.id)
