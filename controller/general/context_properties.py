from enum import Enum


class ContextProperties(Enum):
    MAIN_CONTROLLER = "mainController"

    WAREHOUSE_CONTROLLER = "warehouseController"
    WAREHOUSE_ASSETS_GROUPS = "warehouseAssetsGroups"
    WAREHOUSE_ASSET_DETAILS = "warehouseAssetDetails"
    WAREHOUSE_ASSET_DETAILS_LOCATIONS = "warehouseAssetDetailsLocations"
    WAREHOUSE_ASSET_DETAILS_BUY_ORDERS = "warehouseAssetDetailsBuyOrders"

    SETTINGS_WAREHOUSE_GROUPS_NOT_DISPLAYED = "settingsWarehouseGroupsNotDisplayed"
    SETTINGS_WAREHOUSE_GROUPS_DISPLAYED = "settingsWarehouseGroupsDisplayed"
