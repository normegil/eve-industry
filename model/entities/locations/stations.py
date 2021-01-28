class Station:
    def __init__(self, character_id=None, name=None, services=None, system=None, type=None, race=None):
        self.id = character_id
        self.name = name
        self.services = services
        self.system = system
        self.type = type
        self.race = race
        self.assets = []
        self.buy_orders = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def asset(self, asset_id):
        for asset in self.assets:
            if asset.asset_id == asset_id:
                return asset
        return None

    def add_buy_order(self, buy_order):
        self.buy_orders.append(buy_order)

    def buy_order(self, buy_order_id):
        for buy_order in self.buy_orders:
            if buy_order.id == buy_order_id:
                return buy_order
        return None
