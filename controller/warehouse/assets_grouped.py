from PySide2.QtCore import Qt, QModelIndex, QAbstractListModel, QSortFilterProxyModel

from controller.general import format_integer, format_real


# noinspection PyPep8Naming
class AssetGroupsModel(QAbstractListModel):
    NameRole = Qt.UserRole + 1
    AssetsRole = Qt.UserRole + 2
    IDRole = Qt.UserRole + 3

    def __init__(self, model):
        QAbstractListModel.__init__(self)
        self.__model = model
        self.__internal = []
        self.refresh()

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.__internal)

    def roleNames(self):
        return {
            AssetGroupsModel.NameRole: b'groupName',
            AssetGroupsModel.AssetsRole: b'groupAssets',
            AssetGroupsModel.IDRole: b'identifier'
        }

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            group = self.__internal[index.row()]
            if role == AssetGroupsModel.IDRole:
                return group.id
            if role == AssetGroupsModel.NameRole:
                return group.name
            elif role == AssetGroupsModel.AssetsRole:
                model = QSortFilterProxyModel()
                model.setSourceModel(ItemsModel(group.assets))
                model.setSortRole(ItemsModel.PriceAsIntRole)
                model.sort(0)
                return model

    def refresh(self):
        groups = self.__model.character.all_displayed_groups()
        self.beginResetModel()
        self.__internal = groups
        self.endResetModel()


class ItemsModel(QAbstractListModel):
    NameRole = Qt.UserRole + 1
    QuantityRole = Qt.UserRole + 2
    PriceRole = Qt.UserRole + 3
    IDRole = Qt.UserRole + 4
    PriceAsIntRole = Qt.UserRole + 11

    def __init__(self, model):
        QAbstractListModel.__init__(self)
        self.__internal = model

    def roleNames(self):
        return {
            ItemsModel.IDRole: b'typeID',
            ItemsModel.NameRole: b'name',
            ItemsModel.QuantityRole: b'quantity',
            ItemsModel.PriceRole: b'price',
            ItemsModel.PriceAsIntRole: b'priceAsInt',
        }

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.__internal)

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            item = self.__internal[index.row()]
            if role == ItemsModel.IDRole:
                return item.id
            elif role == ItemsModel.NameRole:
                return item.name
            elif role == ItemsModel.QuantityRole:
                return format_integer(item.quantity)
            elif role == ItemsModel.PriceRole:
                avg = item.average_price_per_unit
                if avg is None:
                    return "???"
                return format_real(avg)
            elif role == ItemsModel.PriceAsIntRole:
                return item.average_price_per_unit
