import logging
import webbrowser

from PySide2.QtCore import QObject, Signal, Property, Slot

from model.entities.locations import LocationType
from .assetlocations import LocationModel

dotlan_base_url = "https://evemaps.dotlan.net/"


# noinspection PyPep8Naming
class AssetDetail(QObject):
    nameChanged = Signal()

    def __init__(self, model, view):
        QObject.__init__(self)
        self.model = model
        self.view = view
        self._asset = self.model.character.find_asset(34)
        self.view.engine.rootContext().setContextProperty("warehouseItemDetails", self)
        self._assets_locations = LocationModel(self._asset.by_locations)
        self.view.engine.rootContext().setContextProperty("warehouseItemDetailsLocations", self._assets_locations)

    @Property(str, notify=nameChanged)
    def name(self):
        return self._asset.name

    @Slot()
    def reloadUI(self):
        self.nameChanged.emit()

    @Slot(int)
    def loadAsset(self, asset_id):
        logging.info(f"Reload asset details: {asset_id}")
        asset = self.model.character.find_asset(asset_id)
        self.set_asset(asset)

    def set_asset(self, asset):
        self._asset = asset
        self._assets_locations.setModel(self._asset.by_locations)
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
