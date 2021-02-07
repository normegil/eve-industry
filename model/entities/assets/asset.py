class Asset:
    def __init__(self, type_id, is_blueprint_copy=False, asset_db=None, market_dao=None, universe_dao=None):
        self.id = type_id
        self.is_blueprint_copy = is_blueprint_copy
        self.by_locations = []
        self.buy_orders = []
        self.__type = None
        self.__minimum_stock = None
        self.__region_orders = None
        self.__asset_db = asset_db
        self.__universe_dao = universe_dao
        self.__market_dao = market_dao

    def set_universe_dao(self, universe_dao):
        self.__universe_dao = universe_dao

    def set_market_dao(self, market_dao):
        self.__market_dao = market_dao

    def set_asset_db(self, asset_db):
        self.__asset_db = asset_db

    @property
    def name(self):
        if self.__type is None:
            type_ = self.__universe_dao.load_type(self.id)
            self.__type = type_
        return self.__type.name

    @property
    def description(self):
        if self.__type is None:
            type_ = self.__universe_dao.load_type(self.id)
            self.__type = type_
        return self.__type.description

    @property
    def volume(self):
        if self.__type is None:
            type_ = self.__universe_dao.load_type(self.id)
            self.__type = type_
        return self.__type.volume

    @property
    def packaged_volume(self):
        if self.__type is None:
            type_ = self.__universe_dao.load_type(self.id)
            self.__type = type_
        return self.__type.packaged_volume

    @property
    def group(self):
        if self.__type is None:
            type_ = self.__universe_dao.load_type(self.id)
            self.__type = type_
        return self.__type.group

    @property
    def quantity(self):
        quantity = 0
        for location in self.by_locations:
            quantity += location.quantity
        return quantity

    @property
    def quantity_buyed(self):
        quantity = 0
        for order in self.buy_orders:
            quantity += order.volume_acted()
        return quantity

    @property
    def total_price_buyed(self):
        price = 0
        for order in self.buy_orders:
            price += order.total_price_acted()
        return price

    @property
    def average_price_per_unit(self):
        quantity_buyed = self.quantity_buyed
        if quantity_buyed == 0:
            return None
        return self.total_price_buyed / quantity_buyed

    @property
    def minimum_stock(self):
        if self.__minimum_stock is None:
            self.__minimum_stock = self.__asset_db.load_minimum_stock(self.id)
            if self.__minimum_stock is None:
                self.__minimum_stock = 0
        return self.__minimum_stock

    def region_orders(self, region_id, include_buy_orders=True, include_sell_orders=True):
        if self.__region_orders is None:
            self.__region_orders = self.__market_dao.load_orders(region_id, self.id)
        orders = []
        for order in self.__region_orders:
            if order.is_buy_order and include_buy_orders:
                orders.append(order)
            elif include_sell_orders:
                orders.append(order)
        return orders


class IndividualAsset:
    def __init__(self, asset_id, location, quantity=0):
        self.asset_id = asset_id
        self.location = location
        self.quantity = quantity
        self.__all_assets = []
        self.__location = None
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


def find_asset(assets, searched_id):
    for asset in assets:
        if asset.id == searched_id:
            return asset
    return None


def find_item(assets, searched_id):
    for asset in assets:
        for assloc in asset.by_locations:
            if assloc.asset_id == searched_id:
                return assloc
    return None
