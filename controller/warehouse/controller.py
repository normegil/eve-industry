from PySide2.QtCore import QObject, Slot, Signal, Property

from controller.general import ContextProperties
from .assets_grouped import AssetGroupsModel
from .details import AssetDetails

pageSources = {
    "details": "./ItemDetails.qml",
    "buylist": "./BuyList.qml"
}


# noinspection PyPep8Naming
class WarehouseController(QObject):
    detailsPageSourceChanged = Signal()

    def __init__(self, model, view):
        QObject.__init__(self)
        self.model = model
        self.view = view

        self.__details_page_source = pageSources["buylist"]

        self.assets_grouped = AssetGroupsModel(self.model)
        self.current_asset = AssetDetails(self.model)

        self.view.engine.rootContext().setContextProperty(ContextProperties.WAREHOUSE_CONTROLLER.value,
                                                          self)
        self.view.engine.rootContext().setContextProperty(ContextProperties.WAREHOUSE_ASSETS_GROUPS.value,
                                                          self.assets_grouped)
        self.view.engine.rootContext().setContextProperty(ContextProperties.WAREHOUSE_ASSET_DETAILS.value,
                                                          self.current_asset)
        self.view.engine.rootContext().setContextProperty(ContextProperties.WAREHOUSE_ASSET_DETAILS_LOCATIONS.value,
                                                          self.current_asset.asset_locations)
        self.view.engine.rootContext().setContextProperty(ContextProperties.WAREHOUSE_ASSET_DETAILS_BUY_ORDERS.value,
                                                          self.current_asset.asset_buy_orders)

    @Slot()
    def refresh(self):
        self.assets_grouped.refresh()
        self.current_asset.refreshAsset()

    @Property(str, notify=detailsPageSourceChanged)
    def detailsPageSource(self):
        return self.__details_page_source

    @Slot(str)
    def changePage(self, page):
        source = pageSources[page]
        if source is not None:
            self.__details_page_source = source
            self.detailsPageSourceChanged.emit()

    @Slot(int)
    def set_displayed_asset_id(self, asset_id):
        self.current_asset.set_displayed_asset_id(asset_id)
        self.current_asset.refresh()
        self.changePage("details")
