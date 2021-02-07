class MarketDAO:
    def __init__(self, market_api):
        self.market_api = market_api

    def load_character_order_history(self, character_id):
        return self.market_api.load_character_order_history(character_id)

    def load_orders(self, region_id, type_id):
        return self.market_api.load_orders(region_id, type_id)

    def load_price(self, type_id):
        return self.market_api.load_price(type_id)
