# Warehouse manager
# Input
# Display all orders
# Output
# Results and Calculations
# Shopping List

import logging
import os
import sys

from redislite import Redis

from controller import Controller
from model import Model
from model.dao.api.sso import EveAuth, Tokens
from ui.qt import QtView

# character_dao = CharacterDAO(CharacterCache(conn, CharacterAPI(t)), MarketDAO(MarketAPI(t)))
# char = character_dao.load()
#
# universe_dao = UniverseDAO(UniverseCache(conn, UniverseAPI(t)))
# report_assets(char, universe_dao, group_name="Mineral")

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
        controller = Controller(model)
        view = QtView(sys.argv, controller)
        sys.exit(view.exec_())
