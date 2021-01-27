class Assets:
    def __init__(self, type_id, type_=None, is_blueprint_copy=False, by_locations=None):
        if by_locations is None:
            by_locations = []
        self.type_id = type_id
        self.is_blueprint_copy = is_blueprint_copy
        self.by_locations = by_locations
        self.buy_orders = []
        if type_ is None:
            self.id = None
            self.name = None
            self.description = None
            self.volume = None
            self.packaged_volume = None
            self.group = None
        else:
            self.merge_with(type_)

    def merge_with(self, type_):
        self.id = type_.id
        self.name = type_.name
        self.description = type_.description
        self.volume = type_.volume
        self.packaged_volume = type_.packaged_volume
        self.group = type_.group

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

    @property
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
