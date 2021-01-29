from PySide2.QtCore import QAbstractListModel, Qt, QModelIndex


# noinspection PyPep8Naming
class LocationModel(QAbstractListModel):
    RegionRole = Qt.UserRole + 2
    ConstellationRole = Qt.UserRole + 3
    SystemRole = Qt.UserRole + 4
    StationRole = Qt.UserRole + 5
    QuantityRole = Qt.UserRole + 6

    def __init__(self, model=None):
        QAbstractListModel.__init__(self)
        if model is None:
            model = []
        self.setModel(model)

    def setModel(self, model):
        self.beginResetModel()
        self.model = model
        self.endResetModel()

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.model)

    def roleNames(self):
        return {
            LocationModel.RegionRole: b'region',
            LocationModel.ConstellationRole: b'constellation',
            LocationModel.SystemRole: b'system',
            LocationModel.StationRole: b'station',
            LocationModel.QuantityRole: b'quantity',
        }

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            row = index.row()
            if role == LocationModel.QuantityRole:
                return self.model[row].quantity
            elif self.model[row].station is None:
                return "???"

            if role == LocationModel.StationRole:
                return self.model[row].station.name
            elif role == LocationModel.SystemRole:
                return self.model[row].station.system.name
            elif role == LocationModel.ConstellationsRole:
                return self.model[row].station.system.constellation.name
            elif role == LocationModel.RegionRole:
                return self.model[row].station.system.constellation.region.name
