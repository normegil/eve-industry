from typing import Optional

from model.dao import WarehouseDAO, CharacterDAO, AssetsDAO
from model.entities.assets import Assets
from model.entities.types import Group


class Warehouse:
    def __init__(self, warehouse_dao: WarehouseDAO, character_dao: CharacterDAO, assets_dao: AssetsDAO):
        self.warehouse_dao = warehouse_dao
        self.character_dao = character_dao
        self.assets_dao = assets_dao
        self.current_character = None
        self.owned_categories = []
        self.refresh()

    def refresh(self):
        self.current_character = self.character_dao.load()
        self.owned_categories = self.warehouse_dao.assets(self.current_character.id)

    def groups(self):
        groups = []
        for category in self.owned_categories:
            for group in category.groups:
                groups.append(group)
        return groups

    def displayed_groups(self):
        displayed = []
        displayed_group_ids = self.displayed_groups_ids()
        for group in self.groups():
            if group.id in displayed_group_ids:
                displayed.append(group)
        return displayed

    def not_displayed_groups(self):
        not_displayed = []
        not_displayed_group_ids = self.not_displayed_groups_ids()
        for group in self.groups():
            if group.id in not_displayed_group_ids:
                not_displayed.append(group)
        return not_displayed

    def assets_to_buy(self):
        groups = self.displayed_groups()
        assets = []
        for group in groups:
            for asset in group.assets:
                if asset.minimum_stock - asset.quantity > 0:
                    assets.append(asset)
        return assets

    def asset(self, type_id) -> Optional[Assets]:
        for category in self.owned_categories:
            for group in category.groups:
                for asset in group.assets:
                    if asset.id == type_id:
                        return asset
        return None

    def group(self, id_) -> Optional[Group]:
        for category in self.owned_categories:
            for group in category.groups:
                if group.id == id_:
                    return group
        return None

    def asset_locations(self, asset_id):
        if asset_id is None:
            return []
        asset = self.asset(asset_id)
        return asset.by_locations

    def asset_buy_orders(self, asset_id):
        if asset_id is None:
            return []
        asset = self.asset(asset_id)
        return asset.buy_orders

    def set_asset_minimum_stock(self, asset_id, minimum_stock):
        asset = self.asset(asset_id)
        if asset is not None:
            asset.minimum_stock = minimum_stock
        self.assets_dao.save_minimum_stock(asset_id, minimum_stock)

    def displayed_groups_ids(self):
        return self.warehouse_dao.displayed_groups_ids()

    def not_displayed_groups_ids(self):
        not_displayed_ids = []
        displayed_ids = self.displayed_groups_ids()
        for group in self.groups():
            if group.id not in displayed_ids:
                not_displayed_ids.append(group.id)
        return not_displayed_ids

    def add_displayed_groups_ids(self, group_id: int):
        self.warehouse_dao.add_displayed_groups_ids(group_id)

    def remove_displayed_groups_ids(self, group_id: int):
        self.warehouse_dao.remove_displayed_groups_ids(group_id)

    def buy_list(self):
        buy_list = []
        for group in self.displayed_groups():
            for asset in group.assets:
                if asset.minimum_stock is not None and asset.minimum_stock - asset.quantity > 0:
                    buy_list.append(asset)
        return buy_list


def load_average_price_per_unit(asset):
    avg = asset.average_price_per_unit
    if avg is not None:
        return avg
    return 0
