import logging

from PySide2.QtCore import QObject, Slot, QSortFilterProxyModel

from controller.general import ContextProperties
from .blueprint_list import BlueprintList
from .blueprint_region_list import BlueprintRegionList


class BlueprintsController(QObject):
    def __init__(self, model, view):
        QObject.__init__(self)
        self.__model = model
        self.__view = view
        self.blueprint_list = BlueprintList(model)

        current_system = self.__model.character.current_system()

        self.region_list = QSortFilterProxyModel()
        self.region_list.setSourceModel(BlueprintRegionList(model, current_system.constellation.region.id))
        self.region_list.setSortRole(BlueprintRegionList.NameRole)
        self.region_list.sort(0)

        self.__view.engine.rootContext().setContextProperty(ContextProperties.BLUEPRINT_CONTROLLER.value, self)
        self.__view.engine.rootContext().setContextProperty(ContextProperties.BLUEPRINT_LIST.value, self.blueprint_list)
        self.__view.engine.rootContext().setContextProperty(ContextProperties.BLUEPRINT_REGION_LIST.value,
                                                            self.region_list)

    @Slot(int)
    def setCurrentRegion(self, id_: int):
        logging.info(f"Selected: {id_}")
