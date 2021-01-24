import os

from PySide2.QtGui import QGuiApplication, QFontDatabase
from PySide2.QtQml import QQmlApplicationEngine


class QtView:
    def __init__(self, argv):
        self.app = QGuiApplication(argv)
        self.__add_roboto_font()
        self.engine = QQmlApplicationEngine()

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
        self.engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

        if not self.engine.rootObjects():
            raise RuntimeError("Could not start QtView")
        return self.app.exec_()
