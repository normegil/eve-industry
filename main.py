# Warehouse manager
# Input
# Display all orders
# Output
# Results and Calculations
# Shopping List
from db import connect

import logging
from api import CharacterAPI, MarketAPI
from api.sso import EveAuth, Tokens

logging.basicConfig(level=logging.INFO)

t = Tokens()

if not t.load():
    auth = EveAuth()
    t = auth.authenticate()

char = CharacterAPI(t).load()
MarketAPI(t).load_character_order_history(char.id)

with connect("data/eve-industry.db") as db:
    pass