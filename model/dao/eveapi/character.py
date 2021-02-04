import json

import requests

from cfg import eve_api
from model.entities import Character
from model.entities.assets import Blueprint, BlueprintLocation, find_asset


class CharacterAPI:
    def __init__(self, tokens):
        self.tokens = tokens

    def load(self):
        resp = requests.get(eve_api.oauth_base_url_v1 + "/verify",
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError("Wrong response code: " + str(resp.status_code))

        content = json.loads(resp.content)

        character = Character(content["CharacterID"], content["CharacterName"])

        return character

    def blueprints(self, character_id):
        resp = requests.get(eve_api.esi_base_address + f"/characters/{character_id}/blueprints",
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError("Wrong response code: " + str(resp.status_code))

        content = json.loads(resp.content)

        blueprints = []
        for blueprint in content:
            found_blueprint = find_asset(blueprints, blueprint["type_id"])
            if found_blueprint is None:
                found_blueprint = Blueprint(blueprint["type_id"])
                blueprints.append(found_blueprint)

            found_blueprint.by_locations.append(
                BlueprintLocation(blueprint["item_id"], blueprint["location_id"], blueprint["location_type"],
                                  blueprint["quantity"], blueprint["runs"], blueprint["material_efficiency"],
                                  blueprint["time_efficiency"]))
        return blueprints
