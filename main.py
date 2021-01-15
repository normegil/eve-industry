# Warehouse manager
# Input
# Display all orders
# Output
# Results and Calculations
# Shopping List

import logging
import os.path

from redislite import Redis

from dao import CharacterDAO, UniverseDAO, MarketDAO
from dao.api import CharacterAPI, UniverseAPI, MarketAPI
from dao.api.sso import EveAuth, Tokens
from dao.redis import CharacterCache, UniverseCache
from reports import report_assets

logging.basicConfig(level=logging.INFO)

if not os.path.exists("data"):
    os.mkdir("data")

conn = Redis("data/redis.db", decode_responses=True)

print(conn.keys())

t = Tokens()
if not t.load():
    auth = EveAuth()
    t = auth.authenticate()

character_dao = CharacterDAO(CharacterCache(conn, CharacterAPI(t)), MarketDAO(MarketAPI(t)))
char = character_dao.load()

universe_dao = UniverseDAO(UniverseCache(conn, UniverseAPI(t)))
report_assets(char, universe_dao, group_name="Mineral")