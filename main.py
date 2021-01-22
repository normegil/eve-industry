# Warehouse manager
# Input
# Display all orders
# Output
# Results and Calculations
# Shopping List

import logging
import os
import sys

from PySide2.QtGui import QGuiApplication, QFontDatabase
from PySide2.QtQml import QQmlApplicationEngine
from redislite import Redis

logging.basicConfig(level=logging.INFO)

if not os.path.exists("data"):
    os.mkdir("data")

# conn = Redis("data/redis.db", decode_responses=True)
# t = Tokens()
# if not t.load():
#     auth = EveAuth()
#     t = auth.authenticate()
#
# character_dao = CharacterDAO(CharacterCache(conn, CharacterAPI(t)), MarketDAO(MarketAPI(t)))
# char = character_dao.load()
#
# universe_dao = UniverseDAO(UniverseCache(conn, UniverseAPI(t)))
# report_assets(char, universe_dao, group_name="Mineral")

def addRobotoFont():
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

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    addRobotoFont()

    engine = QQmlApplicationEngine()
    engine.load(os.path.join(os.path.dirname(__file__), "ui/qt/main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
