from PySide2.QtCore import QObject, Signal, Property

from model.entities.assets import Assets


# noinspection PyPep8Naming
class AssetDetail(QObject):
    nameChanged = Signal()

    def __init__(self, asset: Assets):
        QObject.__init__(self)
        self._asset = asset

    @Property(str, notify=nameChanged)
    def name(self):
        return self._asset.name
