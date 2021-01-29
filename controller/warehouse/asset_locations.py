from PySide2.QtCore import QModelIndex, Qt

from .location_model_list import LocationAbstractModelList


# noinspection PyPep8Naming
class LocationModel(LocationAbstractModelList):
    QuantityRole = Qt.UserRole + 6

    def __init__(self, model=None):
        LocationAbstractModelList.__init__(self, model)

    def roleNames(self):
        return {**super().roleNames(), **{
            LocationModel.QuantityRole: b'quantity',
        }}

    def data(self, index: QModelIndex, role: int = ...):
        if index.isValid():
            row = self.model[index.row()]
            if role == LocationModel.QuantityRole:
                q = row.quantity
                return f"{q:n}"
            else:
                return super().data(index, role)
