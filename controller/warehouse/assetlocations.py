from PySide2.QtCore import QAbstractListModel, Qt, QModelIndex


# noinspection PyPep8Naming
class LocationModel(QAbstractListModel):
    RegionRole = Qt.UserRole + 2
    ConstellationRole = Qt.UserRole + 3
    SystemRole = Qt.UserRole + 4
    StationRole = Qt.UserRole + 5
    QuantityRole = Qt.UserRole + 6
    RegionIDRole = Qt.UserRole + 7
    ConstellationIDRole = Qt.UserRole + 8
    SystemIDRole = Qt.UserRole + 9
    StationIDRole = Qt.UserRole + 10

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
            LocationModel.RegionIDRole: b'regionIdentifier',
            LocationModel.ConstellationRole: b'constellation',
            LocationModel.ConstellationIDRole: b'constellationIdentifier',
            LocationModel.SystemRole: b'system',
            LocationModel.SystemIDRole: b'systemIdentifier',
            LocationModel.StationRole: b'station',
            LocationModel.StationIDRole: b'stationIdentifier',
            LocationModel.QuantityRole: b'quantity',
        }

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            row = self.model[index.row()]
            if role == LocationModel.QuantityRole:
                q = row.quantity
                return f"{q:n}"
            elif row.station is None:
                return None

            if role == LocationModel.StationRole:
                return row.station.name
            elif role == LocationModel.SystemRole:
                return row.station.system.name
            elif role == LocationModel.ConstellationRole:
                return row.station.system.constellation.name
            elif role == LocationModel.RegionRole:
                return row.station.system.constellation.region.name
            elif role == LocationModel.StationIDRole:
                return row.station.id
            elif role == LocationModel.SystemIDRole:
                return row.station.system.id
            elif role == LocationModel.ConstellationIDRole:
                return row.station.system.constellation.id
            elif role == LocationModel.RegionIDRole:
                return row.station.system.constellation.region.id
