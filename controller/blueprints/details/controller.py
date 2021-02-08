from PySide2.QtCore import Signal, QObject, Property, Slot


class BlueprintDetailController(QObject):
    nameChanged = Signal()

    def __init__(self):
        QObject.__init__(self)

    @Slot()
    def refresh(self):
        self.nameChanged.emit()

    @Property(str, notify=nameChanged)
    def name(self):
        return "Test"
        #return self.__blueprint.parent.name
