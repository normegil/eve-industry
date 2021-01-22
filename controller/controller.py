from PySide2.QtCore import QObject


class Controller(QObject):
    def __init__(self, model):
        QObject.__init__(self)
        self.model = model
