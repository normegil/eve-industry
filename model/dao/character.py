import datetime
import logging

from dateutil.relativedelta import relativedelta

from model.entities.assets import Assets


class CharacterDAO:
    def __init__(self, character_api, market_dao, universe_dao):
        self.character_api = character_api
        self.market_dao = market_dao
        self.universe_dao = universe_dao

    def load(self):
        return self.character_api.load()

    def load_assets_by_category(self, character_id):
        assets = self.character_api.load_assets(character_id)
        categories = self.__asset_in_categories(assets)
        orders = self.market_dao.load_character_order_history(character_id)
        categories = self.__order_in_categories(categories, orders)
        self.__load_locations(categories)
        return categories

    def __asset_in_categories(self, assets: []) -> []:
        categories = []
        for index in assets:
            current_asset = assets[index]
            type_ = self.universe_dao.load_type(current_asset.type_id)
            current_asset.merge_with(type_)
            find_asset(categories, current_asset)

        return categories

    def __order_in_categories(self, categories, orders: []) -> []:
        validity = datetime.datetime.now() - relativedelta(years=5)
        for order in orders:
            if not order.is_buy_order:
                continue
            issued_order = datetime.datetime.strptime(order.issued, "%Y-%m-%dT%H:%M:%SZ")
            if validity > issued_order:
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
                            logging.info(f"Could not load station[{buy_order.location_id}] from buy order[{buy_order.id}]: {err}")


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
        group.add_asset(asset)
    return asset


def find_category(categories, category_id):
    for category in categories:
        if category_id == category.id:
            return category
    return None
