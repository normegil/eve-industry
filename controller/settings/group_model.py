from PySide2.QtCore import Qt, QModelIndex, Slot, QSortFilterProxyModel

from controller.general import ResetableModelList


# noinspection PyPep8Naming
class GroupsModel(ResetableModelList):
    IDRole = Qt.UserRole + 1
    NameRole = Qt.UserRole + 2

    def __init__(self, model=None, displayed=None):
        ResetableModelList.__init__(self, model)
        self.onGroupAdded = neutralFunction
        self.onGroupRemoved = neutralFunction
        if displayed is None:
            self.displayed = self.model.copy()
        else:
            self.displayed = displayed

    def setOnGroupAdded(self, onGroupAdded):
        self.onGroupAdded = onGroupAdded

    def setOnGroupRemoved(self, onGroupRemoved):
        self.onGroupRemoved = onGroupRemoved

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.displayed)

    def roleNames(self):
        return {
            GroupsModel.IDRole: b'identifier',
            GroupsModel.NameRole: b'name',
        }

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            row = self.displayed[index.row()]
            if role == GroupsModel.IDRole:
                return row.id
            elif role == GroupsModel.NameRole:
                return row.name

    @Slot(int)
    def addItem(self, id_: int):
        group = self.__find_model_group(id_)
        if group is not None:
            count = self.rowCount()
            self.beginInsertRows(QModelIndex(), count, count)
            self.displayed.append(group)
            self.endInsertRows()
        self.onGroupAdded(id_)

    @Slot(int)
    def removeItem(self, id_):
        index = self.__find_displayed_group_index(id_)
        if index is not None:
            self.beginRemoveRows(QModelIndex(), index, index)
            del self.displayed[index]
            self.endRemoveRows()

    def __find_model_group(self, searched_id: int):
        for group in self.model:
            if group.id == searched_id:
                return group
        return None

    def __find_displayed_group_index(self, searched_id: int):
        for index, group in enumerate(self.displayed):
            if group.id == searched_id:
                return index
        return None


# noinspection PyPep8Naming
class GroupsModelSorter(QSortFilterProxyModel):
    def __init__(self):
        QSortFilterProxyModel.__init__(self)

    @Slot(int)
    def addItem(self, id_: int):
        self.sourceModel().addItem(id_)

    @Slot(int)
    def removeItem(self, id_: int):
        self.sourceModel().removeItem(id_)


def neutralFunction(id_):
    pass
