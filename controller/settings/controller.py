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
        ids = self.model.character.load_warehouse_displayed_asset()

        displayed = []
        not_displayed = []
        for group in groups:
            if group.id in ids:
                displayed.append(group.id)
            else:
                not_displayed.append(group.id)

        groups_model = GroupsModel(groups, not_displayed)
        self.notDisplayedGroupModel = GroupsModelSorter()
        self.notDisplayedGroupModel.setSourceModel(groups_model)
        self.notDisplayedGroupModel.setSortRole(GroupsModel.NameRole)
        self.notDisplayedGroupModel.sort(0)

        self.displayedGroupModel = GroupsModelSorter()
        displayedModel = GroupsModel(groups, displayed)
        displayedModel.setOnGroupAdded(lambda id_: self.model.character.add_warehouse_displayed_asset(id_))
        displayedModel.setOnGroupRemoved(lambda id_: self.model.character.remove_warehouse_displayed_asset(id_))
        self.displayedGroupModel.setSourceModel(displayedModel)
        self.displayedGroupModel.setSortRole(GroupsModel.NameRole)
        self.displayedGroupModel.sort(0)

        self.view.engine.rootContext().setContextProperty(
            ContextProperties.SETTINGS_WAREHOUSE_GROUPS_NOT_DISPLAYED.value,
            self.notDisplayedGroupModel)
        self.view.engine.rootContext().setContextProperty(
            ContextProperties.SETTINGS_WAREHOUSE_GROUPS_DISPLAYED.value,
            self.displayedGroupModel)
