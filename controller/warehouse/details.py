import logging
import webbrowser

from PySide2.QtCore import QObject, Signal, Property, Slot

from model.entities.locations import LocationType
from .asset_locations import LocationModel
from .buy_orders import BuyOrdersModel

dotlan_base_url = "https://evemaps.dotlan.net/"

measurementPrefixesPower = {
    "k": 3,
    "K": 3,
    "m": 6,
    "M": 6,
    "g": 9,
    "G": 9
}


# noinspection PyPep8Naming
class AssetDetails(QObject):
    nameChanged = Signal()
    minimumStockChanged = Signal()

    def __init__(self, model):
        QObject.__init__(self)
        self.model = model
        self._asset = self.model.character.find_asset(34)
        self.asset_locations = LocationModel(self._asset.by_locations)
        self.asset_buy_orders = BuyOrdersModel(self._asset.buy_orders)

    @Property(str, notify=nameChanged)
    def name(self):
        return self._asset.name

    @Property(str, notify=minimumStockChanged)
    def minimumStock(self):
        try:
            mStock = self._asset.minimum_stock
            if mStock is None:
                return "0"
            return str(mStock)
        except AttributeError:
            return "0"

    @Slot(str)
    def setMinimumStock(self, minimum_stock):
        if not minimum_stock:
            self.model.character.save_asset_minimum_stock(self._asset.id, 0)
            return
        last_char = minimum_stock[-1:]
        power = 0
        numberStr = minimum_stock
        if not last_char.isnumeric():
            power = measurementPrefixesPower[last_char]
            numberStr = minimum_stock[:-1]
            if power is None:
                power = 0
        final_minimum_stock = int(numberStr) * 10 ** power
        self._asset.minimum_stock = final_minimum_stock
        self.model.character.save_asset_minimum_stock(self._asset.id, final_minimum_stock)

    @Slot()
    def reloadUI(self):
        self.nameChanged.emit()
        self.minimumStockChanged.emit()

    def refreshAsset(self):
        self.loadAsset(self._asset.id)

    @Slot(int)
    def loadAsset(self, asset_id):
        logging.info(f"Reload asset details: {asset_id}")
        asset = self.model.character.find_asset(asset_id)
        self.setAsset(asset)

    def setAsset(self, asset):
        self._asset = asset
        self.asset_locations.setModel(self._asset.by_locations)
        self.asset_buy_orders.setModel(self._asset.buy_orders)
        self.reloadUI()

    @Slot(int, int)
    def showInBrowser(self, location_type, location_id):
        logging.info(f"Opening DOTLAN [type:{location_type};id:{location_id}]")
        if location_id < 0:
            return
        url = dotlan_base_url
        if location_type == LocationType.REGION.value:
            region = self.model.universe.region(location_id)
            url_region_name = region.name.replace(" ", "_")
            url += f"region/{url_region_name}"
        elif location_type == LocationType.CONSTELLATION.value:
            constellation = self.model.universe.constellation(location_id)
            url_constellation_name = constellation.name.replace(" ", "_")
            url_region_name = constellation.region.name.replace(" ", "_")
            url += f"map/{url_region_name}/{url_constellation_name}"
        elif location_type == LocationType.SYSTEM.value:
            system = self.model.universe.system(location_id)
            url_system_name = system.name.replace(" ", "_")
            url += f"system/{url_system_name}"
        elif location_type == LocationType.STATION.value:
            station = self.model.universe.station(location_id)
            url_station_name = station.name.replace(" ", "_")
            url += f"station/{url_station_name}"
        webbrowser.open(url, new=2)
