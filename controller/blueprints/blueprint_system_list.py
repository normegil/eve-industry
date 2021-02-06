import locale
import typing

from PySide2.QtCore import QAbstractListModel, QModelIndex, Qt, Slot, QSortFilterProxyModel


class BlueprintSystemsList(QAbstractListModel):
    IDRole = Qt.UserRole + 1
    NameRole = Qt.UserRole + 2
    ManufacturingCostRole = Qt.UserRole + 2

    def __init__(self, model, region_id):
        QAbstractListModel.__init__(self)
        self.__model = model
        self.__internal = []
        self.__region_id = region_id
        self.setRegion(region_id)

    @Slot(str)
    def setRegion(self, region_id):
        self.__region_id = int(region_id)
        self.refresh()

    def refresh(self):
        systems = self.__model.universe.systems_from_region(self.__region_id)
        self.beginResetModel()
        self.__internal = systems
        self.endResetModel()

    def rowCount(self, parent: QModelIndex = ...) -> int:
        if parent.isValid():
            return 0
        i = len(self.__internal)
        return i

    def roleNames(self) -> typing.Dict:
        return {
            BlueprintSystemsList.IDRole: b'identifier',
            BlueprintSystemsList.NameRole: b'name',
        }

    def data(self, index: QModelIndex, role: int = ...):
        if index.isValid():
            system = self.__internal[index.row()]
            if role == BlueprintSystemsList.IDRole:
                return system.id
            elif role == BlueprintSystemsList.NameRole:
                manu = locale.format_string("%.4f", system.manufacturing, True)
                return manu + "\t\t" + system.name
            elif role == BlueprintSystemsList.ManufacturingCostRole:
                return system.manufacturing


class BlueprintSystemsSorter(QSortFilterProxyModel):
    def __init__(self, model):
        QSortFilterProxyModel.__init__(self)
        self.setSortRole(BlueprintSystemsList.NameRole)
        self.setSourceModel(model)
        self.sort(0)

    @Slot(str)
    def setRegion(self, region_id):
        self.sourceModel().setRegion(int(region_id))
        self.refresh()

    def refresh(self):
        self.beginResetModel()
        self.sourceModel().refresh()
        self.endResetModel()
