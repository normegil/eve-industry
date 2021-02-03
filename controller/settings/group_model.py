from PySide2.QtCore import Qt, QModelIndex, Slot, QSortFilterProxyModel, QAbstractListModel


# noinspection PyPep8Naming
class GroupsModel(QAbstractListModel):
    IDRole = Qt.UserRole + 1
    NameRole = Qt.UserRole + 2

    def __init__(self, model, showDisplayed: bool):
        QAbstractListModel.__init__(self, model)
        self.__model = model
        self.__onGroupAdded = neutral_function
        self.__onGroupRemoved = neutral_function
        self.__showDisplayed = showDisplayed
        self.__internal = []
        self.refresh()

    def refresh(self):
        if self.__showDisplayed:
            self.__internal = self.__model.character.all_displayed_groups()
        else:
            self.__internal = self.__model.character.all_not_displayed_groups()

    def setOnGroupAdded(self, onGroupAdded):
        self.__onGroupAdded = onGroupAdded

    def setOnGroupRemoved(self, onGroupRemoved):
        self.__onGroupRemoved = onGroupRemoved

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
            group = self.__internal[index.row()]
            if role == GroupsModel.IDRole:
                return group.id
            elif role == GroupsModel.NameRole:
                return group.name

    @Slot(int)
    def addItem(self, id_: int):
        self.onGroupAdded(id_)
        self.refresh()

    @Slot(int)
    def removeItem(self, id_):
        self.onGroupRemoved(id_)
        self.refresh()


# noinspection PyPep8Naming
class GroupsModelSorter(QSortFilterProxyModel):
    def __init__(self):
        QSortFilterProxyModel.__init__(self)

    def refresh(self):
        self.sourceModel().refresh()

    @Slot(int)
    def addItem(self, id_: int):
        self.sourceModel().addItem(id_)
        self.refresh()

    @Slot(int)
    def removeItem(self, id_: int):
        self.sourceModel().removeItem(id_)
        self.refresh()


def neutral_function(id_):
    pass
