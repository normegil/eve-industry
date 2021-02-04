from PySide2.QtCore import QObject

from controller.general import ContextProperties
from .blueprint_list import BlueprintList


class BlueprintsController(QObject):
    def __init__(self, model, view):
        QObject.__init__(self)
        self.__model = model
        self.__view = view
        self.blueprint_list = BlueprintList(model)
        self.view.engine.rootContext().setContextProperty(ContextProperties.BLUEPRINT_CONTROLLER.value, self)
        self.view.engine.rootContext().setContextProperty(ContextProperties.BLUEPRINT_LIST.value, self.blueprint_list)
