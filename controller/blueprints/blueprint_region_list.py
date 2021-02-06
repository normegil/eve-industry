import re
import typing

from PySide2.QtCore import QAbstractListModel, QModelIndex, Qt, Property, Signal


class BlueprintRegionList(QAbstractListModel):
    IDRole = Qt.UserRole + 1
    NameRole = Qt.UserRole + 2

    def __init__(self, model, initial_value):
        QAbstractListModel.__init__(self)
        self.__model = model
        self.__internal = []
        self.__initial_value = initial_value
        self.refresh()

    def refresh(self):
        regions = self.__model.universe.regions()
        self.beginResetModel()
        self.__internal = []
        for region in regions:
            if re.search("^[A-Za-z ]*$", region.name):
                self.__internal.append(region)
        self.endResetModel()

    def initialIndex(self):
        for index, region in enumerate(self.__internal):
            if region.id == self.__initial_value:
                return index
        return None

    def rowCount(self, parent: QModelIndex = ...) -> int:
        if parent.isValid():
            return 0
        i = len(self.__internal)
        return i

    def roleNames(self) -> typing.Dict:
        return {
            BlueprintRegionList.IDRole: b'identifier',
            BlueprintRegionList.NameRole: b'name'
        }

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if index.isValid():
            region = self.__internal[index.row()]
            if role == BlueprintRegionList.IDRole:
                return region.id
            elif role == BlueprintRegionList.NameRole:
                return region.name
