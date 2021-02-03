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
        displayed_group_ids = self.all_displayed_groups_ids()
        for group in self.all_groups():
            if group.id in displayed_group_ids:
                displayed.append(group)
        return displayed

    def all_not_displayed_groups(self):
        not_displayed = []
        not_displayed_group_ids = self.all_not_displayed_groups_ids()
        for group in self.all_groups():
            if group.id in not_displayed_group_ids:
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

    def load_group(self, id_):
        for category in self.categories:
            for group in category.groups:
                if group.id == id_:
                    return group
        return None

    def asset_locations(self, asset_id):
        if asset_id is None:
            return []
        asset = self.find_asset(asset_id)
        return asset.by_locations

    def asset_buy_orders(self, asset_id):
        if asset_id is None:
            return []
        asset = self.find_asset(asset_id)
        return asset.buy_orders

    def save_asset_minimum_stock(self, asset_id, minimum_stock):
        self.character_dao.save_asset_minimum_stock(asset_id, minimum_stock)

    def all_displayed_groups_ids(self):
        return self.character_dao.all_displayed_groups_ids()

    def all_not_displayed_groups_ids(self):
        not_displayed_ids = []
        displayed_ids = self.character_dao.all_displayed_groups_ids()
        for group in self.all_groups():
            if group.id not in displayed_ids:
                not_displayed_ids.append(group.id)
        return not_displayed_ids

    def add_displayed_groups_ids(self, group_id: int):
        self.character_dao.add_displayed_groups_ids(group_id)

    def remove_displayed_groups_ids(self, group_id: int):
        self.character_dao.remove_displayed_groups_ids(group_id)


def load_average_price_per_unit(asset):
    avg = asset.average_price_per_unit
    if avg is not None:
        return avg
    return 0
