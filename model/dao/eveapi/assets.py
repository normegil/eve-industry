import json

import requests

from cfg import eve_api
from model.entities.assets import Assets, AssetLocation


class AssetsAPI:
    def __init__(self, tokens):
        self.tokens = tokens

    def owned(self, character_id):
        resp = requests.get(eve_api.esi_base_address + f"/characters/{character_id}/assets",
                            headers={'Authorization': F"Bearer {self.tokens.access_token}"})
        if resp.status_code >= 300:
            raise RuntimeError("Wrong response code: " + str(resp.status_code))

        content = json.loads(resp.content)

        assets_grouped = []
        for asset in content:
            found_asset = find_asset(assets_grouped, asset["type_id"])
            if found_asset is None:
                if "is_blueprint_copy" in asset:
                    found_asset = Assets(asset["type_id"], is_blueprint_copy=asset["is_blueprint_copy"])
                else:
                    found_asset = Assets(asset["type_id"])
                assets_grouped.append(found_asset)

            found_asset.by_locations.append(
                AssetLocation(asset["item_id"], asset["location_id"], asset["location_type"], asset["quantity"]))
        return assets_grouped


def find_asset(assets, searched_id):
    for asset in assets:
        if asset.id == searched_id:
            return asset
    return None
