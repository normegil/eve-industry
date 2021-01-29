from PySide2.QtCore import QAbstractListModel, QModelIndex


# noinspection PyPep8Naming
class ResetableModelList(QAbstractListModel):
    def __init__(self, model: [] = None):
        QAbstractListModel.__init__(self)
        self.model = []
        if model is None:
            model = []
        self.setModel(model)

    def setModel(self, model):
        self.beginResetModel()
        self.model = model
        self.endResetModel()

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.model)
