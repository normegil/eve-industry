from PySide2.QtCore import QObject

from controller.general import ContextProperties
from .group_model import GroupsModel, GroupsModelSorter


# noinspection PyPep8Naming
class SettingsController(QObject):
    def __init__(self, model, view):
        QObject.__init__(self)
        self.model = model
        self.view = view

        not_displayed_model = GroupsModel(self.model, False)
        self.not_displayed_group_model = GroupsModelSorter()
        self.not_displayed_group_model.setSourceModel(not_displayed_model)
        self.not_displayed_group_model.setSortRole(GroupsModel.NameRole)
        self.not_displayed_group_model.sort(0)

        displayed_model = GroupsModel(self.model, True)
        displayed_model.setOnGroupAdded(lambda id_: self.model.character.add_warehouse_displayed_asset(id_))
        displayed_model.setOnGroupRemoved(lambda id_: self.model.character.remove_warehouse_displayed_asset(id_))
        self.displayed_group_model = GroupsModelSorter()
        self.displayed_group_model.setSourceModel(displayed_model)
        self.displayed_group_model.setSortRole(GroupsModel.NameRole)
        self.displayed_group_model.sort(0)

        self.view.engine.rootContext().setContextProperty(
            ContextProperties.SETTINGS_WAREHOUSE_GROUPS_NOT_DISPLAYED.value,
            self.not_displayed_group_model)
        self.view.engine.rootContext().setContextProperty(
            ContextProperties.SETTINGS_WAREHOUSE_GROUPS_DISPLAYED.value,
            self.displayed_group_model)
