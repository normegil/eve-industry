import typing

from PySide2.QtCore import QAbstractListModel, QModelIndex, Qt, Slot

from controller.general import LocationAbstractModelList
from controller.general import format_real


class BlueprintList(QAbstractListModel):
    NameRole = Qt.UserRole + 1
    LocationsRole = Qt.UserRole + 2

    def __init__(self, model, region_id):
        QAbstractListModel.__init__(self)
        self.__model = model
        self.__internal = []
        self.__region_id = region_id
        self.refresh()

    @Slot(str)
    def setRegion(self, region_id):
        self.beginResetModel()
        self.__region_id = int(region_id)
        self.endResetModel()

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
                return BlueprintIndividualList(self.__model, blueprint.by_locations, self.__region_id)


class BlueprintIndividualList(LocationAbstractModelList):
    RunsRole = Qt.UserRole + 1
    TimeRole = Qt.UserRole + 2
    MaterialsRole = Qt.UserRole + 3
    HighCostRole = Qt.UserRole + 4
    LowCostRole = Qt.UserRole + 5
    HighProductRole = Qt.UserRole + 6
    LowProductRole = Qt.UserRole + 7

    def __init__(self, model, individuals, region_id):
        LocationAbstractModelList.__init__(self)
        self.__model = model
        self.__internal = individuals
        self.__region_id = region_id

    def rowCount(self, parent: QModelIndex = ...) -> int:
        if parent.isValid():
            return 0
        return len(self.__internal)

    def roleNames(self) -> typing.Dict:
        return {**super().roleNames(), **{
            BlueprintIndividualList.RunsRole: b"runs",
            BlueprintIndividualList.TimeRole: b"time",
            BlueprintIndividualList.MaterialsRole: b"mats",
            BlueprintIndividualList.LowCostRole: b"lowcost",
            BlueprintIndividualList.HighCostRole: b"highcost",
            BlueprintIndividualList.LowProductRole: b"lowproduct",
            BlueprintIndividualList.HighProductRole: b"highproduct"
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
            elif role == BlueprintIndividualList.LowCostRole:
                low_cost, high_cost = self.__model.blueprints.total_price(individual, self.__region_id)
                return format_real(low_cost)
            elif role == BlueprintIndividualList.HighCostRole:
                low_cost, high_cost = self.__model.blueprints.total_price(individual, self.__region_id)
                return format_real(high_cost)
            elif role == BlueprintIndividualList.LowProductRole:
                product = individual.parent.manufacturing.products[0]
                products_id = product.type_id
                asset = self.__model.warehouse.asset(products_id)
                price = asset.highest_regional_buy_price(self.__region_id).price_per_unit
                return format_real(product.quantity * price)
            elif role == BlueprintIndividualList.HighProductRole:
                product = individual.parent.manufacturing.products[0]
                products_id = product.type_id
                asset = self.__model.warehouse.asset(products_id)
                price = asset.lowest_regional_sell_price(self.__region_id).price_per_unit
                return format_real(product.quantity * price)
            else:
                return super().data(individual, role)
