from PySide2.QtCore import Qt, QModelIndex, Slot, QSortFilterProxyModel, QAbstractListModel


# noinspection PyPep8Naming
class GroupsModel(QAbstractListModel):
    IDRole = Qt.UserRole + 1
    NameRole = Qt.UserRole + 2

    def __init__(self, model, showDisplayed: bool):
        QAbstractListModel.__init__(self)
        self.__model = model
        self.__showDisplayed = showDisplayed
        self.__internal = []
        self.refresh()

    def refresh(self):
        self.beginResetModel()
        if self.__showDisplayed:
            self.__internal = self.__model.warehouse.displayed_groups_ids()
        else:
            self.__internal = self.__model.warehouse.not_displayed_groups_ids()
        self.endResetModel()

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.__internal)

    def roleNames(self):
        return {
            GroupsModel.IDRole: b'identifier',
            GroupsModel.NameRole: b'name',
        }

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            id_ = self.__internal[index.row()]
            if role == GroupsModel.IDRole:
                return id_
            elif role == GroupsModel.NameRole:
                return self.__model.warehouse.group(id_).name

    @Slot(int)
    def addItem(self, id_: int):
        index = self.rowCount()
        if index is not None:
            self.beginInsertRows(QModelIndex(), index, index)
            self.__internal.append(id_)
            self.endInsertRows()
        if self.__showDisplayed:
            self.__model.warehouse.add_displayed_groups_ids(id_)

    @Slot(int)
    def removeItem(self, id_):
        index = find_id_index(self.__internal, id_)
        if index is not None:
            self.beginRemoveRows(QModelIndex(), index, index)
            del self.__internal[index]
            self.endResetModel()
        if self.__showDisplayed:
            self.__model.warehouse.remove_displayed_groups_ids(id_)


def find_id_index(ids, searched_id):
    for index, id_ in enumerate(ids):
        if id_ == searched_id:
            return index
    return None


# noinspection PyPep8Naming
class GroupsModelSorter(QSortFilterProxyModel):
    def __init__(self):
        QSortFilterProxyModel.__init__(self)

    def refresh(self):
        self.sourceModel().refresh()

    @Slot(int)
    def addItem(self, id_: int):
        self.sourceModel().addItem(id_)

    @Slot(int)
    def removeItem(self, id_: int):
        self.sourceModel().removeItem(id_)


def neutral_function(id_):
    pass
