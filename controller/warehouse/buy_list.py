from PySide2.QtCore import Slot, Property, Signal, QObject


def missing_quantity(asset):
    return asset.minimum_stock - asset.quantity


class BuyList(QObject):
    listChanged = Signal()

    def __init__(self, model):
        QObject.__init__(self)
        self.__model = model
        self.refresh()

    @Slot()
    def refresh(self):
        self.listChanged.emit()

    @Property(str, notify=listChanged)
    def buylist(self):
        assets = self.__model.warehouse.buy_list()
        list_ = ""
        for asset in assets:
            list_ += asset.name + " " + str(missing_quantity(asset)) + "\n"
        return list_
