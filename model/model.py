from model.dao import CharacterDAO, MarketDAO, UniverseDAO
from model.dao.eveapi import CharacterAPI, MarketAPI, UniverseAPI
from model.dao.redis import CharacterCache, UniverseCache
from .api import Characters


class Model:
    def __init__(self, redis, tokens):
        market_dao = MarketDAO(MarketAPI(tokens))
        universe_dao = UniverseDAO(UniverseCache(redis, UniverseAPI(tokens)))
        character_dao = CharacterDAO(CharacterCache(redis, CharacterAPI(tokens)), market_dao, universe_dao)

        self.characters = Characters(character_dao)

    @property
    def character(self):
        return self.characters
