from PySide2.QtCore import Qt, QModelIndex

from controller.general import ResetableModelList, format_integer, format_real


class AssetGroupsModel(ResetableModelList):
    NameRole = Qt.UserRole + 1
    AssetsRole = Qt.UserRole + 2
    IDRole = Qt.UserRole + 3

    def __init__(self, model=None, accepted_group_ids=None):
        ResetableModelList.__init__(self, model)
        self.filteredModel = []
        if accepted_group_ids is None:
            accepted_group_ids = []
        self.accepted_group_ids = accepted_group_ids
        self.__refreshFilteredData()

    def roleNames(self):
        return {
            AssetGroupsModel.NameRole: b'groupName',
            AssetGroupsModel.AssetsRole: b'groupAssets',
            AssetGroupsModel.IDRole: b'identifier'
        }

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            row = self.filteredModel[index.row()]
            if role == AssetGroupsModel.IDRole:
                return row.id
            if role == AssetGroupsModel.NameRole:
                return row.name
            elif role == AssetGroupsModel.AssetsRole:
                return ItemsModel(row.assets)

    def setModel(self, model):
        self.model = model
        self.__refreshFilteredData()

    def setAcceptedGroupIDs(self, accepted_group_ids):
        self.accepted_group_ids = accepted_group_ids
        self.__refreshFilteredData()

    def __refreshFilteredData(self):
        self.beginResetModel()
        self.filteredModel = []
        for group in self.model:
            if group.id in self.accepted_group_ids:
                self.filteredModel.append(group)
        self.endResetModel()

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.filteredModel)


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
            row = self.model[index.row()]
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
