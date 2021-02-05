from PySide2.QtCore import Qt, QModelIndex, QAbstractListModel


class LocationAbstractModelList(QAbstractListModel):
    StationRole = Qt.UserRole + 1011
    StationIDRole = Qt.UserRole + 1012
    SystemRole = Qt.UserRole + 1013
    SystemIDRole = Qt.UserRole + 1014
    ConstellationRole = Qt.UserRole + 1015
    ConstellationIDRole = Qt.UserRole + 1016
    RegionRole = Qt.UserRole + 1017
    RegionIDRole = Qt.UserRole + 1018

    def __init__(self):
        QAbstractListModel.__init__(self)

    def roleNames(self):
        return {
            LocationAbstractModelList.RegionRole: b'region',
            LocationAbstractModelList.RegionIDRole: b'regionIdentifier',
            LocationAbstractModelList.ConstellationRole: b'constellation',
            LocationAbstractModelList.ConstellationIDRole: b'constellationIdentifier',
            LocationAbstractModelList.SystemRole: b'system',
            LocationAbstractModelList.SystemIDRole: b'systemIdentifier',
            LocationAbstractModelList.StationRole: b'station',
            LocationAbstractModelList.StationIDRole: b'stationIdentifier',
        }

    def data(self, item, role: int = ...):
        if item.location.station is None:
            return None
        if role == LocationAbstractModelList.StationRole:
            return item.location.station.name
        elif role == LocationAbstractModelList.SystemRole:
            return item.location.station.system.name
        elif role == LocationAbstractModelList.ConstellationRole:
            return item.location.station.system.constellation.name
        elif role == LocationAbstractModelList.RegionRole:
            return item.location.station.system.constellation.region.name
        elif role == LocationAbstractModelList.StationIDRole:
            return item.location.station.id
        elif role == LocationAbstractModelList.SystemIDRole:
            return item.location.station.system.id
        elif role == LocationAbstractModelList.ConstellationIDRole:
            return item.location.station.system.constellation.id
        elif role == LocationAbstractModelList.RegionIDRole:
            return item.location.station.system.constellation.region.id
