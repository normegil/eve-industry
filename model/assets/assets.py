class Assets:
    def __init__(self, type_id, is_blueprint_copy=False, by_locations=None):
        if by_locations is None:
            by_locations = []
        self.type_id = type_id
        self.is_blueprint_copy = is_blueprint_copy
        self.by_locations = by_locations
        self.buy_orders = []

    @property
    def quantity(self):
        quantity = 0
        for location in self.by_locations:
            quantity += location.quantity
        return quantity

    def quantity_buyed(self):
        quantity = 0
        for order in self.buy_orders:
            quantity += order.volume_acted()
        return quantity

    def total_price_buyed(self):
        price = 0
        for order in self.buy_orders:
            price += order.total_price_acted()
        return price

    def average_price_per_unit(self):
        quantity_buyed = self.quantity_buyed()
        if quantity_buyed == 0:
            return None
        return self.total_price_buyed() / quantity_buyed


class AssetLocation:
    def __init__(self, asset_id, location_id, location_type, quantity=0):
        self.asset_id = asset_id
        self.location_type = location_type
        self.location_id = location_id
        self.quantity = quantity
