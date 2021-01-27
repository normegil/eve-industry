import datetime

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
        categories = []
        for asset in assets:
            type_ = self.universe_dao.load_type(asset.type_id)
            asset.merge_with(type_)

            category = self.find_category(categories, type_.group.category)
            group = category.search_or_add_group(type_.group)
            group.search_or_add_asset_type(asset)

        orders = self.market_dao.load_character_order_history(character_id)
        validity = datetime.datetime.now() - relativedelta(years=5)
        for order in orders:
            if not order.is_buy_order:
                continue
            issued_order = datetime.datetime.strptime(order.issued, "%Y-%m-%dT%H:%M:%SZ")
            if validity > issued_order:
                continue
            type_ = self.universe_dao.load_type(order.type_id)
            category = self.find_category(categories, order.type.group.category)
            group = category.search_or_add_group(type_.group)
            asset = Assets(order.type_id, order.type)
            asset = group.search_or_add_asset_type(asset)
            asset.buy_orders.append(order)
        return categories

    def find_category(self, categories, searched_category):
        for category in categories:
            if searched_category.id == category.id:
                return category
        categories.append(searched_category)
        return searched_category
