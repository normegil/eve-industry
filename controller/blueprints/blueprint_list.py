import typing

from PySide2.QtCore import QAbstractListModel, QModelIndex, Qt

from controller.general import LocationAbstractModelList
from controller.general import format_real


class BlueprintList(QAbstractListModel):
    NameRole = Qt.UserRole + 1
    LocationsRole = Qt.UserRole + 2

    def __init__(self, model):
        QAbstractListModel.__init__(self)
        self.__model = model
        self.__internal = []
        self.refresh()

    def refresh(self):
        self.beginResetModel()
        self.__internal = self.__model.warehouse.blueprints()
        self.endResetModel()

    def rowCount(self, parent: QModelIndex = ...) -> int:
        if parent.isValid():
            return 0
        i = len(self.__internal)
        return i

    def roleNames(self) -> typing.Dict:
        return {
            BlueprintList.NameRole: b'name',
            BlueprintList.LocationsRole: b'locations'
        }

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if index.isValid():
            blueprint = self.__internal[index.row()]
            if role == BlueprintList.NameRole:
                return blueprint.name
            elif role == BlueprintList.LocationsRole:
                return BlueprintIndividualList(self.__model, blueprint.by_locations)


class BlueprintIndividualList(LocationAbstractModelList):
    RunsRole = Qt.UserRole + 1
    TimeRole = Qt.UserRole + 2
    MaterialsRole = Qt.UserRole + 3
    CostRole = Qt.UserRole + 4

    def __init__(self, model, individuals):
        LocationAbstractModelList.__init__(self)
        self.__model = model
        self.__internal = individuals

    def rowCount(self, parent: QModelIndex = ...) -> int:
        if parent.isValid():
            return 0
        return len(self.__internal)

    def roleNames(self) -> typing.Dict:
        return {**super().roleNames(), **{
            BlueprintIndividualList.RunsRole: b"runs",
            BlueprintIndividualList.TimeRole: b"time",
            BlueprintIndividualList.MaterialsRole: b"mats",
            BlueprintIndividualList.CostRole: b"cost",
        }}

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if index.isValid():
            individual = self.__internal[index.row()]
            if role == BlueprintIndividualList.RunsRole:
                return individual.runs
            elif role == BlueprintIndividualList.TimeRole:
                return individual.time_efficiency
            elif role == BlueprintIndividualList.MaterialsRole:
                return individual.material_efficiency
            elif role == BlueprintIndividualList.CostRole:
                return format_real(self.__model.blueprints.total_price(individual))
            else:
                return super().data(individual, role)
