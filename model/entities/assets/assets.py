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

    def by_region(self):
        regions = self.__assets_by_region()
        return self.__buy_orders_by_region(regions)

    def __assets_by_region(self):
        regions = []
        for asset_by_location in self.by_locations:
            found_station = find_station(regions, asset_by_location.station)
            if None is found_station.asset(asset_by_location.asset_id):
                found_station.add_asset(asset_by_location)
        return regions

    def __buy_orders_by_region(self, regions=None):
        if regions is None:
            regions = []
        for buy_order in self.buy_orders:
            found_station = find_station(regions, buy_order.station)
            if None is found_station.buy_order(buy_order.id):
                found_station.add_buy_order(buy_order)
        return regions


def find_station(regions, station):
    region = find_region(regions, station.system.constellation.region)
    if region is None:
        region = station.system.constellation.region
        regions.append(region)
    constellation = region.constellation(station.system.constellation.id)
    if constellation is None:
        constellation = station.system.constellation
        region.add_constellation(constellation)
    system = constellation.system(station.system.id)
    if system is None:
        system = station.system
        constellation.add_system(system)
    station = system.station(station.id)
    if station is None:
        station = station
        system.add_station(station)
    return station


def find_region(regions, region_id):
    for region in regions:
        if region.id == region_id:
            return region
    return None


class AssetLocation:
    def __init__(self, asset_id, location_id, location_type, quantity=0):
        self.asset_id = asset_id
        self.location_type = location_type
        self.location_id = location_id
        self.quantity = quantity
        self.station = None
