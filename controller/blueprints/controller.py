import logging

from PySide2.QtCore import QObject, Slot, Signal, Property

from controller.general import ContextProperties
from .blueprint_list import BlueprintList
from .blueprint_region_list import BlueprintRegionList
from .blueprint_system_list import BlueprintSystemsList, BlueprintSystemsSorter
from .details import BlueprintDetailController


class BlueprintsController(QObject):
    initialRegionIndexChanged = Signal()
    initialSystemIndexChanged = Signal()

    def __init__(self, model, view):
        QObject.__init__(self)
        self.__model = model
        self.__view = view

        current_system = self.__model.character.current_system()
        initial_region_id = current_system.constellation.region.id

        self.blueprint_list = BlueprintList(model, current_system.id)

        self.blueprint_region_list = BlueprintRegionList(model, initial_region_id)
        self.blueprint_system_list = BlueprintSystemsSorter(BlueprintSystemsList(model, initial_region_id))

        self.blueprint_detail = BlueprintDetailController()

        self.__view.engine.rootContext().setContextProperty(ContextProperties.BLUEPRINT_CONTROLLER.value, self)
        self.__view.engine.rootContext().setContextProperty(ContextProperties.BLUEPRINT_LIST.value, self.blueprint_list)
        self.__view.engine.rootContext().setContextProperty(ContextProperties.BLUEPRINT_REGION_LIST.value,
                                                            self.blueprint_region_list)
        self.__view.engine.rootContext().setContextProperty(ContextProperties.BLUEPRINT_SYSTEM_LIST.value,
                                                            self.blueprint_system_list)
        self.__view.engine.rootContext().setContextProperty(ContextProperties.BLUEPRINT_DETAIL_CONTROLLER.value,
                                                           self.blueprint_detail)

    @Slot(int)
    def setCurrentRegion(self, id_: int):
        logging.info(f"Selected: {id_}")

    @Property(int, notify=initialRegionIndexChanged)
    def initialRegionIndex(self):
        return self.blueprint_region_list.initialIndex()

    @Property(int, notify=initialSystemIndexChanged)
    def initialSystemIndex(self):
        return self.blueprint_system_list.initialIndex()
