from PySide2.QtCore import QAbstractListModel, Qt, QModelIndex


class BaseLocationModel(QAbstractListModel):
    def __init__(self, model=None):
        QAbstractListModel.__init__(self)
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


class AssetRegion(BaseLocationModel):
    NameRole = Qt.UserRole + 1
    ConstellationsRole = Qt.UserRole + 2

    def roleNames(self):
        return {
            AssetRegion.NameRole: b'name',
            AssetRegion.ConstellationsRole: b'constellations',
        }

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            row = index.row()
            if role == AssetRegion.NameRole:
                return self.model[row].name
            elif role == AssetRegion.ConstellationsRole:
                return AssetConstellation(self.model[row].constellations)


class AssetConstellation(BaseLocationModel):
    NameRole = Qt.UserRole + 1
    SystemsRole = Qt.UserRole + 2

    def roleNames(self):
        return {
            AssetConstellation.NameRole: b'name',
            AssetConstellation.SystemsRole: b'systems',
        }

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            row = index.row()
            if role == AssetConstellation.NameRole:
                return self.model[row].name
            elif role == AssetConstellation.SystemsRole:
                return AssetSystem(self.model[row].systems)


class AssetSystem(BaseLocationModel):
    NameRole = Qt.UserRole + 1
    StationsRole = Qt.UserRole + 2

    def roleNames(self):
        return {
            AssetSystem.NameRole: b'name',
            AssetSystem.StationsRole: b'stations',
        }

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            row = index.row()
            if role == AssetSystem.NameRole:
                return self.model[row].name
            elif role == AssetSystem.StationsRole:
                return AssetStations(self.model[row].stations)


class AssetStations(BaseLocationModel):
    NameRole = Qt.UserRole + 1
    AssetQuantityRole = Qt.UserRole + 2

    def roleNames(self):
        return {
            AssetStations.NameRole: b'name',
            AssetStations.AssetQuantityRole: b'assetQuantity',
        }

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            row = index.row()
            if role == AssetStations.NameRole:
                return self.model[row].name
            elif role == AssetStations.AssetQuantityRole:
                return self.model[row].asset.quantity
