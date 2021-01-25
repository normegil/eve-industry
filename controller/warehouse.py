import logging

from PySide2.QtCore import QAbstractListModel, Qt, QModelIndex


class Group:
    def __init__(self, name, assets):
        self.name = name
        self.assets = assets


class Item:
    def __init__(self, name):
        self.name = name


class ItemGroupsModel(QAbstractListModel):
    NameRole = Qt.UserRole + 1
    AssetsRole = Qt.UserRole + 2

    def __init__(self, parent=None):
        QAbstractListModel.__init__(self, parent)
        self.groups = [
            Group("Tech 1", ItemsModel([Item("A"), Item("B"), Item("C")])),
            Group("Tech 2", ItemsModel([Item("D")])),
            Group("Tech 3", ItemsModel([Item("E"), Item("F"), Item("G"), Item("H"), Item("I")]))
        ]

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
                logging.info("Group: Name")
                return self.groups[row].name
            elif role == ItemGroupsModel.AssetsRole:
                logging.info("Group: Assets")
                return self.groups[row].assets


class ItemsModel(QAbstractListModel):
    NameRole = Qt.UserRole + 1

    def __init__(self, items, parent=None):
        QAbstractListModel.__init__(self, parent)
        self.items = items

    def roleNames(self):
        return {
            ItemGroupsModel.NameRole: b'itemName',
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
