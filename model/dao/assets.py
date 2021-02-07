import datetime
import logging
import time

from dateutil.relativedelta import relativedelta

from model.dao.database import AssetsDB
from model.dao.eveapi import AssetsAPI
from model.entities.assets import Asset, find_asset


class AssetsDAO:
    def __init__(self, assets_db: AssetsDB, assets_api: AssetsAPI, character_api, blueprint_db, market_dao,
                 universe_dao):
        self.assets_api = assets_api
        self.__assets_db = assets_db
        self.character_api = character_api
        self.__market_dao = market_dao
        self.__universe_dao = universe_dao
        self.__blueprint_db = blueprint_db

    def blueprints(self, character_id):
        assets = self.owned(character_id)
        bps = self.character_api.blueprints(character_id)
        for bp in bps:
            self.__init_asset_properties(bp, assets)
            bp.set_blueprint_db(self.__blueprint_db)
        return bps

    def owned(self, character_id):
        bef = current_milli_time()
        assets = self.assets_api.owned(character_id)
        orders = self.__market_dao.load_character_order_history(character_id)
        buy_order_in_assets(assets, orders)

        for asset in assets:
            self.__init_asset_properties(asset, assets)
        aft = current_milli_time()
        logging.info(f"Owned: {aft - bef}ms")
        return assets

    def asset(self, asset_id):
        asset = Asset(asset_id, universe_dao=self.__universe_dao, asset_db=self.__assets_db)
        self.__init_asset_properties(asset, [])

    def __init_asset_properties(self, asset, assets):
        asset.set_asset_db(self.__assets_db)
        asset.set_universe_dao(self.__universe_dao)
        asset.set_market_dao(self.__market_dao)
        self.__finalise_location_init(asset.by_locations, assets)
        self.__finalise_location_init(asset.buy_orders, assets)

    def __finalise_location_init(self, individuals, assets):
        for individual in individuals:
            if hasattr(individual.location, "set_universe_dao"):
                individual.location.set_universe_dao(self.__universe_dao)
            if hasattr(individual.location, "set_assets"):
                individual.location.set_assets(assets)

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

    def save_minimum_stock(self, asset_id: int, minimum_stock: int):
        self.__assets_db.save_minimum_stock(asset_id, minimum_stock)


def buy_order_in_assets(assets, orders: []) -> []:
    validity = datetime.datetime.now(datetime.timezone.utc) - relativedelta(years=5)
    for order in orders:
        if not order.is_buy_order:
            continue
        if validity > order.issued:
            continue

        found_asset = find_asset(assets, order.type_id)
        if found_asset is None:
            found_asset = Asset(order.type_id)
            assets.append(found_asset)
        found_asset.buy_orders.append(order)
    return assets


def find_category(categories, category_id):
    for category in categories:
        if category_id == category.id:
            return category
    return None


def current_milli_time():
    return round(time.time() * 1000)
