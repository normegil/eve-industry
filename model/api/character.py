class Characters:
    def __init__(self, character_dao):
        self.character_dao = character_dao
        self.current_character = self.character_dao.load()
        self.categories = []
        self.refresh()

    def refresh(self):
        self.categories = self.character_dao.load_assets_by_category(self.current_character.id)

    def all_groups(self):
        groups = []
        for category in self.categories:
            for group in category.groups:
                groups.append(group)
        return groups

    def all_displayed_groups(self):
        displayed = []
        displayed_group_ids = self.load_warehouse_displayed_asset()
        for group in self.all_groups():
            if group.id in displayed_group_ids:
                displayed.append(group)
        return displayed

    def all_not_displayed_groups(self):
        not_displayed = []
        displayed_group_ids = self.load_warehouse_displayed_asset()
        for group in self.all_groups():
            if group.id not in displayed_group_ids:
                not_displayed.append(group)
        return not_displayed

    def all_assets_to_buy(self):
        groups = self.all_displayed_groups()
        assets = []
        for group in groups:
            for asset in group.assets:
                if asset.minimum_stock - asset.quantity > 0:
                    assets.append(asset)
        return assets

    def find_asset(self, type_id):
        for category in self.categories:
            for group in category.groups:
                for asset in group.assets:
                    if asset.id == type_id:
                        return asset
        return None

    def asset_locations(self, asset_id):
        asset = self.find_asset(asset_id)
        return asset.by_locations

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
