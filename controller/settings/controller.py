from PySide2.QtCore import QObject

from controller.general import ContextProperties
from .group_model import GroupsModel


# noinspection PyPep8Naming
class SettingsController(QObject):
    def __init__(self, model, view):
        QObject.__init__(self)
        self.model = model
        self.view = view

        groups = self.model.universe.all_character_groups()
        self.groupModel = GroupsModel(groups)
        self.view.engine.rootContext().setContextProperty(
            ContextProperties.SETTINGS_WAREHOUSE_GROUPS_NOT_FOLLOWED.value,
            self.groupModel)
