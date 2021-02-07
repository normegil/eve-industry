from dateutil.relativedelta import relativedelta

from model.dao import CharacterDAO, MarketDAO, UniverseDAO, AssetsDAO, WarehouseDAO
from model.dao.cache import CharacterCache, UniverseCache, IndustryCache, TimeoutCacheAdapter, MarketCache, DictAdapter
from model.dao.database import WarehouseDB, AssetsDB, BlueprintsDB
from model.dao.eveapi import CharacterAPI, MarketAPI, UniverseAPI, AssetsAPI, LocationAPI, IndustryAPI
from .api import Warehouse, Universe, Character, BlueprintModelAPI


class Model:
    def __init__(self, userdb, staticdb, cache, tokens):
        character_api = CharacterCache(TimeoutCacheAdapter(cache, relativedelta(minutes=5)), CharacterAPI(tokens))
        location_api = LocationAPI(tokens)
        industry_api = IndustryCache(DictAdapter({}), IndustryCache(TimeoutCacheAdapter(cache, relativedelta(days=1)),
                                                       IndustryAPI(tokens)))

        market_dao = MarketDAO(MarketCache(DictAdapter({}), MarketCache(TimeoutCacheAdapter(cache, relativedelta(hours=1)), MarketAPI(tokens))))
        universe_dao = UniverseDAO(
            UniverseCache(DictAdapter({}), UniverseCache(TimeoutCacheAdapter(cache, relativedelta(months=2)), UniverseAPI(tokens))),
            industry_api)
        assets_dao = AssetsDAO(AssetsDB(userdb), AssetsAPI(tokens), character_api, BlueprintsDB(staticdb), market_dao,
                               universe_dao)
        character_dao = CharacterDAO(character_api, location_api)
        warehouse_dao = WarehouseDAO(WarehouseDB(userdb))

        self.warehouse = Warehouse(warehouse_dao, character_dao, assets_dao)
        self.character = Character(character_dao, universe_dao)
        self.universe = Universe(universe_dao)
        self.blueprints = BlueprintModelAPI(self.warehouse)
