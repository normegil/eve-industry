from PySide2.QtCore import Qt, QModelIndex, QAbstractListModel, Slot


class BuyList(QAbstractListModel):
    NameRole = Qt.UserRole + 1
    QuantityRole = Qt.UserRole + 2

    def __init__(self, model):
        QAbstractListModel.__init__(self)
        self.__model = model
        self.__internal = []
        self.refresh()

    @Slot()
    def refresh(self):
        self.beginResetModel()
        self.__internal = self.__model.character.asset_buy_list()
        self.endResetModel()

    def roleNames(self):
        return {
            BuyList.NameRole: b'name',
            BuyList.QuantityRole: b'quantity'
        }

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            asset = self.__internal[index.row()]
            if role == BuyList.NameRole:
                return asset.name
            elif role == BuyList.QuantityRole:
                return missing_quantity(asset)

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.__internal)


def missing_quantity(asset):
    return asset.minimum_stock - asset.quantity
