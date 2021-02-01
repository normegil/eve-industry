from PySide2.QtCore import QObject, Slot

from controller.general import ContextProperties
from .assets_grouped import AssetGroupsModel
from .details import AssetDetails


# noinspection PyPep8Naming
class WarehouseController(QObject):
    def __init__(self, model, view):
        QObject.__init__(self)
        self.model = model
        self.view = view

        self.assets_grouped = AssetGroupsModel()
        self.refreshAssetsGroups()
        self.refreshAssetFilter()

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
        self.refreshAssetsGroups()
        self.refreshAssetFilter()
        self.current_asset.refreshAsset()

    def refreshAssetsGroups(self):
        asset_categories = self.model.character.assets()
        qt_group_format = to_qt_group_format(asset_categories)
        self.assets_grouped.setModel(qt_group_format)

    @Slot()
    def refreshAssetFilter(self):
        displayed_group_ids = self.model.character.load_warehouse_displayed_asset()
        self.assets_grouped.setAcceptedGroupIDs(displayed_group_ids)


def to_qt_group_format(asset_categories):
    groups = []
    for category in asset_categories:
        for group in category.groups:
            groups.append(group)
    return groups
