import typing

from PySide2.QtCore import QAbstractListModel, QModelIndex, Qt


class BlueprintSystemsList(QAbstractListModel):
    IDRole = Qt.UserRole + 1
    NameRole = Qt.UserRole + 2
    ManufacturingCostRole = Qt.UserRole + 2

    def __init__(self, model, region_id):
        QAbstractListModel.__init__(self)
        self.__model = model
        self.__region_id = region_id
        self.__internal = []
        self.refresh()

    def set_region(self, region_id):
        self.__region_id = region_id
        self.refresh()

    def refresh(self):
        systems = self.__model.universe.systems_from_region(self.__region_id)
        self.beginResetModel()
        self.__internal = systems
        self.endResetModel()

    def rowCount(self, parent: QModelIndex = ...) -> int:
        if parent.isValid():
            return 0
        return len(self.__internal)

    def roleNames(self) -> typing.Dict:
        return {
            BlueprintSystemsList.IDRole: b'identifier',
            BlueprintSystemsList.NameRole: b'name',
            BlueprintSystemsList.ManufacturingCostRole: b'manufacturing'
        }

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if index.isValid():
            system = self.__internal[index.row()]
            if role == BlueprintSystemsList.IDRole:
                return system.id
            elif role == BlueprintSystemsList.NameRole:
                return system.name
            elif role == BlueprintSystemsList.ManufacturingCostRole:
                return system.manufacturing
