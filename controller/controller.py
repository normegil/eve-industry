import logging

from PySide2.QtCore import QObject, Signal, Slot, Property

from controller.general import ContextProperties
from controller.settings import SettingsController
from controller.warehouse import WarehouseController

pageSources = {
    "warehouse": "pages/warehouse/Warehouse.qml",
    "settings": "pages/settings/Settings.qml"
}


# noinspection PyPep8Naming
class Controller(QObject):
    pageSourceChanged = Signal()

    def __init__(self, model, view):
        QObject.__init__(self)
        self.model = model
        self.view = view

        self._pageSource = pageSources["warehouse"]
        self.warehouse_controller = WarehouseController(self.model, self.view)
        self.settings_controller = SettingsController(self.model, self.view)
        self.view.engine.rootContext().setContextProperty(ContextProperties.MAIN_CONTROLLER.value, self)

    @Property(str, notify=pageSourceChanged)
    def pageSource(self):
        return self._pageSource

    @Slot(str)
    def changePage(self, page):
        logging.info(f"Changing page: {page}")
        source = pageSources[page]
        if source is not None:
            self._pageSource = source
            self.pageSourceChanged.emit()
