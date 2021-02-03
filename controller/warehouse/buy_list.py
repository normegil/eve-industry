from PySide2.QtCore import Qt, QModelIndex

from controller.general import ResetableModelList, format_integer, format_real


class AssetGroupsModel(ResetableModelList):
    NameRole = Qt.UserRole + 1
    QuantityRole = Qt.UserRole + 2

    def __init__(self, model=None):
        ResetableModelList.__init__(self, model)
        self.filteredModel = []
        self.__refreshFilteredData()

    def roleNames(self):
        return {
            AssetGroupsModel.NameRole: b'name',
            AssetGroupsModel.QuantityRole: b'quantity'
        }

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            item = self.filteredModel[index.row()]
            if role == AssetGroupsModel.NameRole:
                return item.name
            elif role == AssetGroupsModel.QuantityRole:
                return self.__missing_quantity(item)

    def __missing_quantity(self, item):
        return item.minimumStock - item.quantity

    def setModel(self, model):
        self.model = model
        self.__refreshFilteredData()

    def __refreshFilteredData(self):
        self.beginResetModel()
        self.filteredModel = []
        for item in self.model:
            if self.__missing_quantity(item) > 0:
                self.filteredModel.append(item)
        self.endResetModel()

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.filteredModel)
