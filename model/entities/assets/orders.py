class Order:
    def __init__(self, order_id, issued, location_id, price_per_unit, state, type_id, volume_remain, volume_total,
                 is_buy_order=False):
        self.id = order_id
        self.is_buy_order = is_buy_order
        self.issued = issued
        self.location_id = location_id
        self.price_per_unit = price_per_unit
        self.state = state
        self.type_id = type_id
        self.volume_remain = volume_remain
        self.volume_total = volume_total
        self.type = None

    def volume_acted(self):
        return self.volume_total - self.volume_remain

    def total_price_acted(self):
        return self.price_per_unit * self.volume_acted()