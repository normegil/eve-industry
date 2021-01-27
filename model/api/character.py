class Characters:
    def __init__(self, character_dao):
        self.character_dao = character_dao
        self.current_character = self.character_dao.load()

    def assets(self):
        assets_category = self.character_dao.load_assets_by_category(self.current_character.id)

        for category in assets_category:
            for group in category.groups:
                group.assets.sort(key=lambda asset: load_average_price_per_unit(asset))

        return assets_category


def load_average_price_per_unit(asset):
    avg = asset.average_price_per_unit
    if avg is not None:
        return avg
    return 0
