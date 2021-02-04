import datetime
import logging

from dateutil.relativedelta import relativedelta

from model.entities.assets import Assets
from .assets import AssetsDAO


class WarehouseDAO:
    def __init__(self, warehouse_db, assets_dao: AssetsDAO, market_dao, universe_dao):
        self.warehouse_db = warehouse_db
        self.assets_dao = assets_dao
        self.market_dao = market_dao
        self.universe_dao = universe_dao

    def assets(self, character_id):
        assets = self.assets_dao.owned(character_id)
        categories = self.__asset_in_categories(assets)

        orders = self.market_dao.load_character_order_history(character_id)
        categories = self.__order_in_categories(categories, orders)

        self.assets_dao.load_minimum_stocks(categories)
        self.__load_locations(categories)

        return categories

    def __asset_in_categories(self, assets: []) -> []:
        categories = []
        for current_asset in assets:
            type_ = self.universe_dao.load_type(current_asset.type_id)
            current_asset.merge_with(type_)
            find_asset(categories, current_asset)

        return categories

    def __order_in_categories(self, categories, orders: []) -> []:
        validity = datetime.datetime.now(datetime.timezone.utc) - relativedelta(years=5)
        for order in orders:
            if not order.is_buy_order:
                continue
            if validity > order.issued:
                continue
            type_ = self.universe_dao.load_type(order.type_id)
            current_asset = Assets(order.type_id, type_)
            found_asset = find_asset(categories, current_asset)
            found_asset.buy_orders.append(order)
        return categories

    def __load_locations(self, categories):
        for category in categories:
            for group in category.groups:
                for asset in group.assets:
                    for location in asset.by_locations:
                        if location.location_type == "station":
                            location.station = self.universe_dao.load_stations(location.location_id)
                    for buy_order in asset.buy_orders:
                        try:
                            buy_order.station = self.universe_dao.load_stations(buy_order.location_id)
                        except RuntimeError as err:
                            logging.info(
                                f"Could not load station[{buy_order.location_id}] from buy order[{buy_order.id}]: {err}")

    def displayed_groups_ids(self):
        return self.warehouse_db.displayed_groups_ids()

    def add_displayed_groups_ids(self, group_id: int):
        self.warehouse_db.add_displayed_groups_ids(group_id)

    def remove_displayed_groups_ids(self, group_id: int):
        self.warehouse_db.remove_displayed_groups_ids(group_id)


def find_asset(categories, asset):
    category = find_category(categories, asset.group.category.id)
    if category is None:
        category = asset.group.category
        categories.append(category)
    group = category.group(asset.group.id)
    if group is None:
        group = asset.group
        category.add_group(group)
    found_asset = group.asset(asset.id)
    if found_asset is None:
        found_asset = asset
        group.add_asset(found_asset)
    return found_asset


def find_category(categories, category_id):
    for category in categories:
        if category_id == category.id:
            return category
    return None
