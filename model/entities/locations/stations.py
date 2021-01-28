class Station:
    def __init__(self, character_id=None, name=None, services=None, system=None, type=None, race=None):
        self.id = character_id
        self.name = name
        self.services = services
        self.system = system
        self.type = type
        self.race = race
        self.asset = None
        self.buy_orders = []

    def add_buy_order(self, buy_order):
        self.buy_orders.append(buy_order)

    def buy_order(self, buy_order_id):
        for buy_order in self.buy_orders:
            if buy_order.id == buy_order_id:
                return buy_order
        return None
