from PySide2.QtCore import QObject

from .warehouse import ItemGroupsModel


class Controller(QObject):
    def __init__(self, model, view):
        QObject.__init__(self)
        self.model = model
        self.view_model = ItemGroupsModel()

        self.refresh_warehouse()
        view.engine.rootContext().setContextProperty("itemGroupsModel", self.view_model)

    def refresh_warehouse(self):
        asset_categories = self.model.characters.assets()
        qt_group_format = self.to_qt_group_format(asset_categories)
        self.view_model.setModel(qt_group_format)

    def to_qt_group_format(self, asset_categories):
        groups = []
        for category in asset_categories:
            for group in category.groups:
                if group.name == "Mineral":
                    groups.append(group)
        return groups
