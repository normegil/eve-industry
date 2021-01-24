from PySide2.QtCore import QObject

from .warehouse import ItemGroupsModel


class Controller(QObject):
    def __init__(self, model, view):
        QObject.__init__(self)
        self.model = model
        self.register_warehouse(view)

    def register_warehouse(self, view):
        self.model = ItemGroupsModel()
        view.engine.rootContext().setContextProperty("itemGroupsModel", self.model)
