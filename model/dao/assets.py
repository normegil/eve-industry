import datetime
import logging

from dateutil.relativedelta import relativedelta

from model.dao.database import AssetsDB
from model.dao.eveapi import AssetsAPI
from model.entities.assets import Assets, find_asset


class AssetsDAO:
    def __init__(self, assets_db: AssetsDB, assets_api: AssetsAPI, market_dao, universe_dao):
        self.assets_api = assets_api
        self.assets_db = assets_db
        self.market_dao = market_dao
        self.universe_dao = universe_dao

    def owned(self, character_id):
        assets = self.assets_api.owned(character_id)

        for asset in assets:
            self.__load_type(asset)

        orders = self.market_dao.load_character_order_history(character_id)
        buy_order_in_assets(assets, orders)

        for asset in assets:
            self.__load_type(asset)
            self.__load_locations(asset.by_locations)
            self.__load_locations(asset.buy_orders)
            self.__load_minimum_stock(asset)

        return assets

    def owned_in_categories(self, character_id):
        assets = self.owned(character_id)
        categories = []
        for asset in assets:
            found_category = find_category(categories, asset.group.category.id)
            if found_category is None:
                found_category = asset.group.category
                categories.append(found_category)
            found_group = found_category.group(asset.group.id)
            if found_group is None:
                found_group = asset.group
                found_category.groups.append(found_group)
            found_asset = found_group.asset(asset.id)
            if found_asset is None:
                found_asset = asset
                found_group.add_asset(found_asset)
        return categories

    def __load_minimum_stock(self, asset: Assets):
        asset.minimum_stock = self.assets_db.load_minimum_stock(asset.id)

    def __load_type(self, asset: Assets):
        type_ = self.universe_dao.load_type(asset.type_id)
        asset.merge_with(type_)

    def __load_locations(self, asset_locations):
        for asset_location in asset_locations:
            if asset_location.location_type == "station":
                asset_location.station = self.universe_dao.load_stations(asset_location.location_id)
            else:
                logging.info(f"Unsupported location type: {asset_location.location_type}")

    def save_minimum_stock(self, asset_id: int, minimum_stock: int):
        self.assets_db.save_minimum_stock(asset_id, minimum_stock)


def buy_order_in_assets(assets, orders: []) -> []:
    validity = datetime.datetime.now(datetime.timezone.utc) - relativedelta(years=5)
    for order in orders:
        if not order.is_buy_order:
            continue
        if validity > order.issued:
            continue

        found_asset = find_asset(assets, order.type_id)
        if found_asset is None:
            found_asset = Assets(order.type_id)
            assets.append(found_asset)
        found_asset.buy_orders.append(order)
    return assets


def find_category(categories, category_id):
    for category in categories:
        if category_id == category.id:
            return category
    return None
