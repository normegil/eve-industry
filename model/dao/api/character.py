import json

import requests

from cfg import eve_api
from model import Character, Assets, AssetLocation


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

    def load_assets(self, character_id):
        resp = requests.get(eve_api.esi_base_address + f"/characters/{character_id}/assets",
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError("Wrong response code: " + str(resp.status_code))

        content = json.loads(resp.content)

        assets_grouped = {}
        for asset in content:
            if asset["type_id"] not in assets_grouped:
                if "is_blueprint_copy" in asset:
                    assets_grouped[asset["type_id"]] = Assets(asset["type_id"], asset["is_blueprint_copy"])
                else:
                    assets_grouped[asset["type_id"]] = Assets(asset["type_id"])

            assets_grouped[asset["type_id"]].by_locations.append(
                AssetLocation(asset["item_id"], asset["location_id"], asset["location_type"], asset["quantity"]))

        return assets_grouped
