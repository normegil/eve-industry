from PySide2.QtCore import QObject

from controller.warehouse import WarehouseController


class Controller(QObject):
    def __init__(self, model, view):
        QObject.__init__(self)
        self.model = model
        self.view = view

        self.warehouse_controller = WarehouseController(self.model, self.view)
