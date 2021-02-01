from PySide2.QtCore import QObject

from controller.general import ContextProperties
from .group_model import GroupsModel, GroupsModelSorter


# noinspection PyPep8Naming
class SettingsController(QObject):
    def __init__(self, model, view):
        QObject.__init__(self)
        self.model = model
        self.view = view

        groups = self.model.universe.all_character_groups()

        groups_model = GroupsModel(groups)
        self.notDisplayedGroupModel = GroupsModelSorter()
        self.notDisplayedGroupModel.setSourceModel(groups_model)
        self.notDisplayedGroupModel.setSortRole(GroupsModel.NameRole)
        self.notDisplayedGroupModel.sort(0)

        self.displayedGroupModel = GroupsModelSorter()
        self.displayedGroupModel.setSourceModel(GroupsModel(groups, []))
        self.displayedGroupModel.setSortRole(GroupsModel.NameRole)
        self.displayedGroupModel.sort(0)

        self.view.engine.rootContext().setContextProperty(
            ContextProperties.SETTINGS_WAREHOUSE_GROUPS_NOT_DISPLAYED.value,
            self.notDisplayedGroupModel)
        self.view.engine.rootContext().setContextProperty(
            ContextProperties.SETTINGS_WAREHOUSE_GROUPS_DISPLAYED.value,
            self.displayedGroupModel)
