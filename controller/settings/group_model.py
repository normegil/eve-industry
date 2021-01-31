from PySide2.QtCore import Qt, QModelIndex

from controller.general import ResetableModelList


class GroupsModel(ResetableModelList):
    IDRole = Qt.UserRole + 1
    NameRole = Qt.UserRole + 2

    def __init__(self, model=None):
        ResetableModelList.__init__(self, model)

    def roleNames(self):
        return {
            GroupsModel.IDRole: b'identifier',
            GroupsModel.NameRole: b'name',
        }

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            row = self.model[index.row()]
            if role == GroupsModel.IDRole:
                return row.id
            elif role == GroupsModel.NameRole:
                return row.name

    def addGroup(self, group):
        count = self.rowCount()
        self.beginInsertRows(parent=QModelIndex(), first=count, last=count)
        self.model.append(group)
        self.endInsertRows()

    def removeGroup(self):
        pass
        #self.__find_group_index()
        #self.beginRemoveRows(parent=QModelIndex(), first=)
        #self.endRemoveRows()

    def __find_group_index(self, searched_name: str):
        for index, group in enumerate(self.model):
            if group.name == searched_name:
                return index
        return None
