import os

from PySide2.QtGui import QGuiApplication, QFontDatabase
from PySide2.QtQml import QQmlApplicationEngine


class QtView:
    def __init__(self, argv):
        self.app = QGuiApplication(argv)
        self.__add_roboto_font()
        self.__add_line_awesome_font()
        self.engine = QQmlApplicationEngine()

    def __add_roboto_font(self):
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto/Roboto-Black.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto/Roboto-BlackItalic.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto/Roboto-Bold.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto/Roboto-BoldItalic.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto/Roboto-Italic.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto/Roboto-Light.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto/Roboto-LightItalic.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto/Roboto-Medium.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto/Roboto-MediumItalic.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto/Roboto-Regular.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto/Roboto-Thin.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/Roboto/Roboto-ThinItalic.ttf")

    def __add_line_awesome_font(self):
        QFontDatabase.addApplicationFont("ui/resources/fonts/line-awesome/la-brands-400.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/line-awesome/la-regular-400.ttf")
        QFontDatabase.addApplicationFont("ui/resources/fonts/line-awesome/la-solid-900.ttf")

    def exec_(self):
        self.engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

        if not self.engine.rootObjects():
            raise RuntimeError("Could not start QtView")
        return self.app.exec_()
