from model.dao import CharacterDAO, MarketDAO, UniverseDAO, AssetsDAO, WarehouseDAO
from model.dao.cache import CharacterCache, UniverseCache
from model.dao.database import WarehouseDB, AssetsDB
from model.dao.eveapi import CharacterAPI, MarketAPI, UniverseAPI, AssetsAPI
from .api import Warehouse, Universe


class Model:
    def __init__(self, db, cache, tokens):
        market_dao = MarketDAO(MarketAPI(tokens))
        universe_dao = UniverseDAO(UniverseCache(cache, UniverseAPI(tokens)))
        assets_dao = AssetsDAO(AssetsDB(db), AssetsAPI(tokens))
        character_dao = CharacterDAO(CharacterCache(cache, CharacterAPI(tokens)))
        warehouse_dao = WarehouseDAO(WarehouseDB(db), assets_dao, market_dao, universe_dao)

        self.warehouse = Warehouse(warehouse_dao, character_dao, assets_dao)
        self.universe = Universe(universe_dao)
