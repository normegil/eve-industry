import datetime
from dateutil.relativedelta import relativedelta


class Order:
    def __init__(self, order_id, issued, location_id, price_per_unit, duration, type_id, volume_remain, volume_total,
                 is_buy_order=False):
        self.id = order_id
        self.is_buy_order = is_buy_order
        self.issued = issued
        self.location_id = location_id
        self.price_per_unit = price_per_unit
        self.duration = duration
        self.type_id = type_id
        self.volume_remain = volume_remain
        self.volume_total = volume_total
        self.station = None

    def volume_acted(self):
        return self.volume_total - self.volume_remain

    def total_price_acted(self):
        return self.price_per_unit * self.volume_acted()

    def __validity(self):
        return self.issued + relativedelta(days=self.duration)

    def expired(self) -> bool:
        return datetime.datetime.now(datetime.timezone.utc) > self.__validity()
