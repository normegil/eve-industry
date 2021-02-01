from PySide2.QtCore import Qt, QModelIndex, Slot, QSortFilterProxyModel

from controller.general import ResetableModelList


# noinspection PyPep8Naming
class GroupsModel(ResetableModelList):
    IDRole = Qt.UserRole + 1
    NameRole = Qt.UserRole + 2

    def __init__(self, model=None, displayed_ids=None):
        ResetableModelList.__init__(self, model)
        self.onGroupAdded = neutralFunction
        self.onGroupRemoved = neutralFunction
        if displayed_ids is None:
            self.displayed_ids = []
        else:
            self.displayed_ids = displayed_ids

    def setOnGroupAdded(self, onGroupAdded):
        self.onGroupAdded = onGroupAdded

    def setOnGroupRemoved(self, onGroupRemoved):
        self.onGroupRemoved = onGroupRemoved

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.displayed_ids)

    def roleNames(self):
        return {
            GroupsModel.IDRole: b'identifier',
            GroupsModel.NameRole: b'name',
        }

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            row = self.displayed_ids[index.row()]
            if role == GroupsModel.IDRole:
                return row
            elif role == GroupsModel.NameRole:
                return self.__find_model_group(row).name

    @Slot(int)
    def addItem(self, id_: int):
        count = self.rowCount()
        self.beginInsertRows(QModelIndex(), count, count)
        self.displayed_ids.append(id_)
        self.endInsertRows()
        self.onGroupAdded(id_)

    @Slot(int)
    def removeItem(self, id_):
        index = self.__find_displayed_group_index(id_)
        if index is not None:
            self.beginRemoveRows(QModelIndex(), index, index)
            del self.displayed_ids[index]
            self.endRemoveRows()
        self.onGroupRemoved(id_)

    def __find_model_group(self, searched_id: int):
        for group in self.model:
            if group.id == searched_id:
                return group
        return None

    def __find_displayed_group_index(self, searched_id: int):
        for index, id_ in enumerate(self.displayed_ids):
            if id_ == searched_id:
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
