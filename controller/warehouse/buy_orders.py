from PySide2.QtCore import QModelIndex, Qt

from controller.general import format_integer, format_real, format_datetime
from .location_model_list import LocationAbstractModelList


class BuyOrdersModel(LocationAbstractModelList):
    IssuedRole = Qt.UserRole + 1
    ExpiredRole = Qt.UserRole + 2
    PricePerUnitRole = Qt.UserRole + 4
    VolumeRemainingRole = Qt.UserRole + 5
    VolumeTotalRole = Qt.UserRole + 6

    def __init__(self, model=None):
        LocationAbstractModelList.__init__(self, model)

    def roleNames(self):
        return {**super().roleNames(), **{
            BuyOrdersModel.IssuedRole: b'issued',
            BuyOrdersModel.ExpiredRole: b'expired',
            BuyOrdersModel.PricePerUnitRole: b'pricePerUnit',
            BuyOrdersModel.VolumeRemainingRole: b'volumeRem',
            BuyOrdersModel.VolumeTotalRole: b'volumeTot',
        }}

    def data(self, index: QModelIndex, role: int = ...):
        if index.isValid():
            order = self.model[index.row()]
            if role == BuyOrdersModel.IssuedRole:
                return format_datetime(order.issued)
            elif role == BuyOrdersModel.ExpiredRole:
                return order.expired()
            elif role == BuyOrdersModel.PricePerUnitRole:
                return format_real(order.price_per_unit)
            elif role == BuyOrdersModel.VolumeRemainingRole:
                return format_integer(order.volume_remain)
            elif role == BuyOrdersModel.VolumeTotalRole:
                return format_integer(order.volume_total)
            else:
                return super().data(index, role)
