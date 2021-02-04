import typing
from PySide2.QtCore import QAbstractListModel, QModelIndex, Qt


class BlueprintList(QAbstractListModel):
    NameRole = Qt.UserRole + 1

    def __init__(self, model):
        QAbstractListModel.__init__(self)
        self.__model = model
        self.__internal = []

    def refresh(self):
        self.beginResetModel()
        self.__internal = self.__model.warehouse.blueprints()
        self.endResetModel()

    def rowCount(self, parent: QModelIndex = ...) -> int:
        if parent.isValid():
            return 0
        return len(self.__internal)

    def roleNames(self) -> typing.Dict:
        return {
            BlueprintList.NameRole: b'name'
        }

    def data(self, index:QModelIndex, role:int=...) -> typing.Any:
        if index.isValid():
            blueprint = self.__internal[index.row()]
            if role == BlueprintList.NameRole:
                return blueprint.name
