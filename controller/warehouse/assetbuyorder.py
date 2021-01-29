from PySide2.QtCore import QAbstractListModel, QModelIndex, Qt
import locale


class BuyOrdersModel(QAbstractListModel):
    IssuedRole = Qt.UserRole + 1
    ExpiredRole = Qt.UserRole + 2
    PricePerUnitRole = Qt.UserRole + 4
    VolumeRemainingRole = Qt.UserRole + 5
    VolumeTotalRole = Qt.UserRole + 6
    StationRole = Qt.UserRole + 11
    StationIDRole = Qt.UserRole + 12
    SystemRole = Qt.UserRole + 13
    SystemIDRole = Qt.UserRole + 14
    ConstellationRole = Qt.UserRole + 15
    ConstellationIDRole = Qt.UserRole + 16
    RegionRole = Qt.UserRole + 17
    RegionIDRole = Qt.UserRole + 18

    def __init__(self, model=None):
        QAbstractListModel.__init__(self)
        if model is None:
            model = []
        self.setModel(model)

    def setModel(self, model):
        self.beginResetModel()
        self.model = model
        self.endResetModel()

    def roleNames(self):
        return {
            BuyOrdersModel.IssuedRole: b'issued',
            BuyOrdersModel.ExpiredRole: b'expired',
            BuyOrdersModel.PricePerUnitRole: b'pricePerUnit',
            BuyOrdersModel.VolumeRemainingRole: b'volumeRemaining',
            BuyOrdersModel.VolumeTotalRole: b'volumeTotal',
            BuyOrdersModel.RegionRole: b'region',
            BuyOrdersModel.RegionIDRole: b'regionIdentifier',
            BuyOrdersModel.ConstellationRole: b'constellation',
            BuyOrdersModel.ConstellationIDRole: b'constellationIdentifier',
            BuyOrdersModel.SystemRole: b'system',
            BuyOrdersModel.SystemIDRole: b'systemIdentifier',
            BuyOrdersModel.StationRole: b'station',
            BuyOrdersModel.StationIDRole: b'stationIdentifier',
        }

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.model)

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            order = self.model[index.row()]
            if role == BuyOrdersModel.IssuedRole:
                return order.issued.strftime("%y-%m-%d %H:%M:%S")
            elif role == BuyOrdersModel.ExpiredRole:
                return order.expired()
            elif role == BuyOrdersModel.PricePerUnitRole:
                return locale.format_string("%.2f", order.price_per_unit, True)
            elif role == BuyOrdersModel.VolumeRemainingRole:
                return order.volume_remain
            elif role == BuyOrdersModel.VolumeTotalRole:
                return order.volume_total
            else:
                if order.station is None:
                    return None
                if role == BuyOrdersModel.StationRole:
                    return order.station.name
                elif role == BuyOrdersModel.SystemRole:
                    return order.station.system.name
                elif role == BuyOrdersModel.ConstellationRole:
                    return order.station.system.constellation.name
                elif role == BuyOrdersModel.RegionRole:
                    return order.station.system.constellation.region.name
                elif role == BuyOrdersModel.StationIDRole:
                    return order.station.id
                elif role == BuyOrdersModel.SystemIDRole:
                    return order.station.system.id
                elif role == BuyOrdersModel.ConstellationIDRole:
                    return order.station.system.constellation.id
                elif role == BuyOrdersModel.RegionIDRole:
                    return order.station.system.constellation.region.id
