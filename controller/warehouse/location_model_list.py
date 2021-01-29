from PySide2.QtCore import Qt, QModelIndex

from controller.general import ResetableModelList


class LocationAbstractModelList(ResetableModelList):
    StationRole = Qt.UserRole + 1011
    StationIDRole = Qt.UserRole + 1012
    SystemRole = Qt.UserRole + 1013
    SystemIDRole = Qt.UserRole + 1014
    ConstellationRole = Qt.UserRole + 1015
    ConstellationIDRole = Qt.UserRole + 1016
    RegionRole = Qt.UserRole + 1017
    RegionIDRole = Qt.UserRole + 1018

    def __init__(self, model: [] = None):
        ResetableModelList.__init__(self, model)

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

    def data(self, index: QModelIndex, role: int = ...):
        if index.isValid():
            item = self.model[index.row()]
            if item.station is None:
                return None
            if role == LocationAbstractModelList.StationRole:
                return item.station.name
            elif role == LocationAbstractModelList.SystemRole:
                return item.station.system.name
            elif role == LocationAbstractModelList.ConstellationRole:
                return item.station.system.constellation.name
            elif role == LocationAbstractModelList.RegionRole:
                return item.station.system.constellation.region.name
            elif role == LocationAbstractModelList.StationIDRole:
                return item.station.id
            elif role == LocationAbstractModelList.SystemIDRole:
                return item.station.system.id
            elif role == LocationAbstractModelList.ConstellationIDRole:
                return item.station.system.constellation.id
            elif role == LocationAbstractModelList.RegionIDRole:
                return item.station.system.constellation.region.id
