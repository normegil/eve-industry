# Warehouse manager
# Input
# Display all orders
# Output
# Results and Calculations
# Shopping List

from api import CharacterAPI, MarketAPI
from api.sso import EveAuth, Tokens

t = Tokens()

if not t.load():
    auth = EveAuth()
    t = auth.authenticate()

char = CharacterAPI(t).load()
MarketAPI(t).load_character_order_history(char.id)
