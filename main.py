import logging
import os
import sys

from redislite import Redis

from controller import Controller
from model import Model
from model.dao.eveapi.sso import EveAuth, Tokens
from ui.qt import QtView

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    if not os.path.exists("data"):
        os.mkdir("data")

    with Redis("data/redis.db", decode_responses=True) as conn:
        t = Tokens()
        if not t.load():
            auth = EveAuth()
            t = auth.authenticate()
        model = Model(conn, t)
        view = QtView(sys.argv)
        controller = Controller(model, view)
        sys.exit(view.exec_())
