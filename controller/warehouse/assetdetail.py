from PySide2.QtCore import QObject, Signal, Property, Slot

from .assetlocations import AssetRegion


# noinspection PyPep8Naming
class AssetDetail(QObject):
    nameChanged = Signal()

    def __init__(self, model, view):
        QObject.__init__(self)
        self.model = model
        self.view = view
        self._asset = self.model.characters.find_asset(34)
        self.view.engine.rootContext().setContextProperty("warehouseItemDetails", self)
        self._asset_region = AssetRegion(self._asset.by_region)
        self.view.engine.rootContext().setContextProperty("warehouseItemDetailsLocations", self._asset_region)

    @Property(str, notify=nameChanged)
    def name(self):
        return self._asset.name

    @Slot()
    def reloadUI(self):
        self.nameChanged.emit()

    def set_asset(self, asset):
        self._asset = asset
        self._asset_region.setModel(self._asset.by_region)
        self.reloadUI()
