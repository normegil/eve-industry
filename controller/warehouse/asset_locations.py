from PySide2.QtCore import QModelIndex, Qt

from controller.general import LocationAbstractModelList


# noinspection PyPep8Naming
class LocationModel(LocationAbstractModelList):
    QuantityRole = Qt.UserRole + 6

    def __init__(self, model):
        LocationAbstractModelList.__init__(self)
        self.__model = model
        self.__displayed_asset_id = None
        self.__internal = None

    def set_displayed_asset_id(self, asset_id):
        self.__displayed_asset_id = asset_id
        self.refresh()

    def refresh(self):
        self.beginResetModel()
        self.__internal = self.__model.warehouse.asset_locations(self.__displayed_asset_id)
        self.endResetModel()

    def roleNames(self):
        return {**super().roleNames(), **{
            LocationModel.QuantityRole: b'quantity',
        }}

    def data(self, index: QModelIndex, role: int = ...):
        if index.isValid():
            location = self.__internal[index.row()]
            if role == LocationModel.QuantityRole:
                q = location.quantity
                return f"{q:n}"
            else:
                return super().data(location, role)

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.__internal)
