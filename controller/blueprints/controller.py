import logging

from PySide2.QtCore import QObject, Slot, QSortFilterProxyModel, Signal, Property

from controller.general import ContextProperties
from .blueprint_list import BlueprintList
from .blueprint_region_list import BlueprintRegionList


class BlueprintsController(QObject):
    initialRegionIndexChanged = Signal()

    def __init__(self, model, view):
        QObject.__init__(self)
        self.__model = model
        self.__view = view
        self.blueprint_list = BlueprintList(model)

        current_system = self.__model.character.current_system()

        self.__blueprint_region_list = BlueprintRegionList(model, current_system.constellation.region.id)

        self.__view.engine.rootContext().setContextProperty(ContextProperties.BLUEPRINT_CONTROLLER.value, self)
        self.__view.engine.rootContext().setContextProperty(ContextProperties.BLUEPRINT_LIST.value, self.blueprint_list)
        self.__view.engine.rootContext().setContextProperty(ContextProperties.BLUEPRINT_REGION_LIST.value,
                                                            self.__blueprint_region_list)

    @Slot(int)
    def setCurrentRegion(self, id_: int):
        logging.info(f"Selected: {id_}")

    @Property(int, notify=initialRegionIndexChanged)
    def initialRegionIndex(self):
        return self.__blueprint_region_list.initialIndex()
