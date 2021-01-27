from PySide2.QtCore import QAbstractListModel, Qt, QModelIndex


class Group:
    def __init__(self, name, assets):
        self.name = name
        self.assets = assets


class ItemGroupsModel(QAbstractListModel):
    NameRole = Qt.UserRole + 1
    AssetsRole = Qt.UserRole + 2

    def __init__(self, groups=None, parent=None):
        QAbstractListModel.__init__(self, parent)
        if groups is None:
            groups = []
        self.setModel(groups)

    def setModel(self, groups):
        self.beginResetModel()
        self.groups = groups
        self.endResetModel()

    def roleNames(self):
        return {
            ItemGroupsModel.NameRole: b'groupName',
            ItemGroupsModel.AssetsRole: b'groupAssets',
        }

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.groups)

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            row = index.row()
            if role == ItemGroupsModel.NameRole:
                return self.groups[row].name
            elif role == ItemGroupsModel.AssetsRole:
                return ItemsModel(self.groups[row].assets)


class ItemsModel(QAbstractListModel):
    NameRole = Qt.UserRole + 1

    def __init__(self, items, parent=None):
        QAbstractListModel.__init__(self, parent)
        self.items = items

    def roleNames(self):
        return {
            ItemGroupsModel.NameRole: b'name',
        }

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.items)

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            row = index.row()
            if role == ItemGroupsModel.NameRole:
                return self.items[row].name
