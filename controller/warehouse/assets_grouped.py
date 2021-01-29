import locale

from PySide2.QtCore import Qt, QModelIndex

from controller.general import ResetableModelList, format_integer, format_real


class AssetGroupsModel(ResetableModelList):
    NameRole = Qt.UserRole + 1
    AssetsRole = Qt.UserRole + 2

    def __init__(self, model=None):
        ResetableModelList.__init__(self, model)

    def roleNames(self):
        return {
            AssetGroupsModel.NameRole: b'groupName',
            AssetGroupsModel.AssetsRole: b'groupAssets',
        }

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            row = self.groups[index.row()]
            if role == AssetGroupsModel.NameRole:
                return row.name
            elif role == AssetGroupsModel.AssetsRole:
                return ItemsModel(row.assets)


class ItemsModel(ResetableModelList):
    NameRole = Qt.UserRole + 1
    QuantityRole = Qt.UserRole + 2
    PriceRole = Qt.UserRole + 3
    IDRole = Qt.UserRole + 4

    def __init__(self, model=None):
        ResetableModelList.__init__(self, model)

    def roleNames(self):
        return {
            ItemsModel.IDRole: b'typeID',
            ItemsModel.NameRole: b'name',
            ItemsModel.QuantityRole: b'quantity',
            ItemsModel.PriceRole: b'price',
        }

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            row = self.items[index.row()]
            if role == ItemsModel.IDRole:
                return row.id
            elif role == ItemsModel.NameRole:
                return row.name
            elif role == ItemsModel.QuantityRole:
                return format_integer(row.quantity)
            elif role == ItemsModel.PriceRole:
                avg = row.average_price_per_unit
                if avg is None:
                    return "???"
                return format_real(avg)
