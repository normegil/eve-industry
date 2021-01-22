from model.entities.assets import Assets
import datetime
from dateutil.relativedelta import relativedelta


class CharacterDAO:
    def __init__(self, character_api, market_dao):
        self.character_api = character_api
        self.market_dao = market_dao

    def load(self):
        char = self.character_api.load()
        assets = self.load_assets(char)
        char.assets = assets
        return char

    def load_assets(self, character):
        assets = self.character_api.load_assets(character.id)
        orders = self.market_dao.load_character_order_history(character.id)

        validity = datetime.datetime.now() - relativedelta(years=5)

        for order in orders:
            if not order.is_buy_order:
                continue
            issued_order = datetime.datetime.strptime(order.issued, "%Y-%m-%dT%H:%M:%SZ")
            if validity > issued_order:
                continue
            if order.type_id not in assets:
                assets[order.type_id] = Assets(order.type_id)
            assets[order.type_id].buy_orders.append(order)

        return assets
