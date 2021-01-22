import json

import requests
import logging

from cfg import eve_api
from model import Race
from model.entities.locations import Region, Constellation, Station, System
from model.entities.types import Type, Group, Category


class UniverseAPI:
    base_url = eve_api.esi_base_address + "/universe/"

    def __init__(self, tokens):
        self.tokens = tokens

    def load_region(self, region_id):
        logging.info(f"Requesting region: {region_id}")
        resp = requests.get(self.base_url + "regions/" + str(region_id),
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError(f"Wrong response code: {str(resp.status_code)} - {region_id}")

        region = json.loads(resp.content)
        return Region(region["region_id"], region["name"], region["description"])

    def load_constellation(self, constellation_id):
        logging.info(f"Requesting constellation: {constellation_id}")
        resp = requests.get(self.base_url + "constellations/" + str(constellation_id),
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError(f"Wrong response code: {str(resp.status_code)} - {constellation_id}")

        constellation = json.loads(resp.content)
        c = Constellation(constellation["constellation_id"], constellation["name"])
        c.region_id = constellation["region_id"]
        return c

    def load_system(self, system_id):
        logging.info(f"Requesting system: {system_id}")
        resp = requests.get(self.base_url + "systems/" + str(system_id),
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError(f"Wrong response code: {str(resp.status_code)} - {system_id}")

        system = json.loads(resp.content)
        s = System(system["system_id"], system["name"])
        s.constellation_id = system["constellation_id"]
        return s

    def load_races(self):
        logging.info(f"Requesting races")
        resp = requests.get(self.base_url + "races",
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError(f"Wrong response code: {str(resp.status_code)}")

        races = []
        content = json.loads(resp.content)
        for r in content:
            races.append(Race(r["race_id"], r["name"], r["description"]))

        return races

    def load_race(self, race_id):
        logging.info(f"Requesting race: {race_id}")
        races = self.load_races()
        for r in races:
            if r.id == race_id:
                return r
        return None

    def load_stations(self, station_id):
        logging.info(f"Requesting station: {station_id}")
        resp = requests.get(self.base_url + "stations/" + str(station_id),
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError(f"Wrong response code: {str(resp.status_code)} - {station_id}")

        station = json.loads(resp.content)
        s = Station(station["station_id"], station["name"], station["services"])
        s.system_id = station["system_id"]
        s.type_id = station["type_id"]
        s.race_id = station["race_id"]
        return s

    def load_type(self, type_id):
        logging.info(f"Requesting type: {type_id}")
        resp = requests.get(self.base_url + "types/" + str(type_id),
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError(f"Wrong response code: {str(resp.status_code)} - {type_id}")

        type_ = json.loads(resp.content)
        t = Type(type_["type_id"], type_["name"], type_["description"], type_["volume"], type_["packaged_volume"])
        t.group_id = type_["group_id"]
        return t

    def load_group(self, group_id):
        logging.info(f"Requesting group: {group_id}")
        resp = requests.get(self.base_url + "groups/" + str(group_id),
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError(f"Wrong response code: {str(resp.status_code)} - {group_id}")

        group = json.loads(resp.content)

        g = Group(group["group_id"], group["name"])
        g.category_id = group["category_id"]
        return g

    def load_category(self, category_id):
        logging.info(f"Requesting category: {category_id}")
        resp = requests.get(self.base_url + "categories/" + str(category_id),
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError(f"Wrong response code: {str(resp.status_code)} - {category_id}")

        category = json.loads(resp.content)

        return Category(category["category_id"], category["name"])
