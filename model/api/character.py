class Characters:
    def __init__(self, character_dao):
        self.character_dao = character_dao
        self.current_character = self.character_dao.load()
        self.assets_category = []

    def assets(self):
        self.load_assets()
        for category in self.assets_category:
            for group in category.groups:
                group.assets.sort(key=lambda asset: load_average_price_per_unit(asset))

        return self.assets_category

    def find_asset(self, type_id):
        if not self.assets_category:
            self.load_assets()

        for category in self.assets_category:
            for group in category.groups:
                for asset in group.assets:
                    if asset.id == type_id:
                        return asset
        return None

    def load_assets(self):
        self.assets_category = self.character_dao.load_assets_by_category(self.current_character.id)

    def save_asset_minimum_stock(self, asset_id, minimum_stock):
        self.character_dao.save_asset_minimum_stock(asset_id, minimum_stock)

    def load_warehouse_displayed_asset(self):
        return self.character_dao.load_warehouse_displayed_asset()

    def add_warehouse_displayed_asset(self, group_id: int):
        self.character_dao.add_warehouse_displayed_asset(group_id)

    def remove_warehouse_displayed_asset(self, group_id: int):
        self.character_dao.remove_warehouse_displayed_asset(group_id)


def load_average_price_per_unit(asset):
    avg = asset.average_price_per_unit
    if avg is not None:
        return avg
    return 0
