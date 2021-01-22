import os

from PySide2.QtGui import QGuiApplication, QFontDatabase
from PySide2.QtQml import QQmlApplicationEngine


class QtView:
    def __init__(self, argv, backend):
        self.argv = argv
        self.backend = backend

    def __add_roboto_font(self):
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto-Black.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto-BlackItalic.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto-Bold.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto-BoldItalic.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto-Italic.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto-Light.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto-LightItalic.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto-Medium.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto-MediumItalic.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto-Regular.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto-Thin.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto-ThinItalic.ttf")

    def exec_(self):
        app = QGuiApplication(self.argv)
        self.__add_roboto_font()

        engine = QQmlApplicationEngine()
        engine.rootContext().setContextProperty("backend", self.backend)

        engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

        if not engine.rootObjects():
            raise RuntimeError("Could not start QtView")
        return app.exec_()
