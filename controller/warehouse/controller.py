from PySide2.QtCore import QObject

from controller.general import ContextProperties
from .assets_grouped import AssetGroupsModel
from .details import AssetDetails


class WarehouseController(QObject):
    def __init__(self, model, view):
        QObject.__init__(self)
        self.model = model
        self.view = view

        self.assets_grouped = AssetGroupsModel()
        self.refresh_assets_groups()

        self.current_asset = AssetDetails(self.model)

        self.view.engine.rootContext().setContextProperty(ContextProperties.WAREHOUSE_ASSETS_GROUPS.value,
                                                          self.assets_grouped)
        self.view.engine.rootContext().setContextProperty(ContextProperties.WAREHOUSE_ASSET_DETAILS.value,
                                                          self.current_asset)
        self.view.engine.rootContext().setContextProperty(ContextProperties.WAREHOUSE_ASSET_DETAILS_LOCATIONS.value,
                                                          self.current_asset.asset_locations)
        self.view.engine.rootContext().setContextProperty(ContextProperties.WAREHOUSE_ASSET_DETAILS_BUY_ORDERS.value,
                                                          self.current_asset.asset_buy_orders)

    def refresh_assets_groups(self):
        asset_categories = self.model.character.assets()
        qt_group_format = to_qt_group_format(asset_categories)
        self.assets_grouped.setModel(qt_group_format)


def to_qt_group_format(asset_categories):
    groups = []
    for category in asset_categories:
        for group in category.groups:
            if group.name == "Mineral":
                groups.append(group)
    return groups
