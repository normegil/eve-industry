import logging
import os
import sqlite3
import sys

from sqlitedict import SqliteDict

from controller import Controller
from model import Model
from model.dao.cache import SQLLiteDictAdapter
from model.dao.database import Versioner
from model.dao.database.versioning.user import upgrades as userdb_versions
from model.dao.eveapi.sso import EveAuth, Tokens
from ui.qt import QtView

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    if not os.path.exists("data"):
        os.mkdir("data")
    with sqlite3.connect("data/user_store.db") as dbconn:
        Versioner(dbconn, userdb_versions).upgrade()
        with SqliteDict("data/cache.db", autocommit=True) as cache_conn:
            t = Tokens()
            if not t.load():
                auth = EveAuth()
                t = auth.authenticate()
            model = Model(dbconn, SQLLiteDictAdapter(cache_conn), t)
            view = QtView(sys.argv)
            controller = Controller(model, view)
            sys.exit(view.exec_())
