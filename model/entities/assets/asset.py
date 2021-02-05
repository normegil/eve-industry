class Asset:
    def __init__(self, type_id, is_blueprint_copy=False):
        self.id = type_id
        self.is_blueprint_copy = is_blueprint_copy
        self.__universe_dao = None
        self.by_locations = []
        self.buy_orders = []
        self.__type = None

    def set_universe_dao(self, universe_dao):
        self.__universe_dao = universe_dao

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
