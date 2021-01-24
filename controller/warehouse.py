import logging

from PySide2.QtCore import QAbstractListModel, Qt, QModelIndex


class ItemGroupsModel(QAbstractListModel):
    NameRole = Qt.UserRole + 1

    def __init__(self, parent=None):
        QAbstractListModel.__init__(self, parent)
        self.groups = [
            Group("Tech 1"),
            Group("Tech 2")
        ]
        logging.info(f"ItemGroupsModel: Init")

    def roleNames(self):
        logging.info(f"ItemGroupsModel: role names")
        return {
            ItemGroupsModel.NameRole: b'groupName',
        }

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        logging.info(f"ItemGroupsModel: Row Count {len(self.groups)}")
        return len(self.groups)

    def data(self, index, role=Qt.DisplayRole):
        logging.info(f"ItemGroupsModel[]: ")
        if index.isValid():
            row = index.row()
            logging.info(f"ItemGroupsModel[{row}]: ")
            if role == ItemGroupsModel.NameRole:
                logging.info(f"ItemGroupsModel[{row}]: {self.groups[row].name}")
                return self.groups[row].name


class Group:
    def __init__(self, name):
        self.name = name
