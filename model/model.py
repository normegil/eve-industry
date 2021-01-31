from model.dao import CharacterDAO, MarketDAO, UniverseDAO
from model.dao.cache import CharacterCache, UniverseCache
from model.dao.database import CharacterDB
from model.dao.eveapi import CharacterAPI, MarketAPI, UniverseAPI
from .api import Characters, Universe


class Model:
    def __init__(self, db, cache, tokens):
        market_dao = MarketDAO(MarketAPI(tokens))
        universe_dao = UniverseDAO(UniverseCache(cache, UniverseAPI(tokens)))
        character_dao = CharacterDAO(CharacterCache(cache, CharacterAPI(tokens)), CharacterDB(db), market_dao,
                                     universe_dao)

        self.character = Characters(character_dao)
        self.universe = Universe(universe_dao, character_dao)
