import json

import requests

from cfg import eve_api
from model.entities.assets import Asset, IndividualAsset, find_asset, AssetLocation, AssetLocationStation, \
    AssetLocationItem


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
                    found_asset = Asset(asset["type_id"], is_blueprint_copy=asset["is_blueprint_copy"])
                else:
                    found_asset = Asset(asset["type_id"])
                assets_grouped.append(found_asset)

            location_id = asset["location_id"]
            location_type = asset["location_type"]
            location = AssetLocation(location_type, location_id)
            if location_type == "station":
                location = AssetLocationStation(location_type, location_id)
            elif location_type == "item":
                location = AssetLocationItem(location_type, location_id)

            individual_asset = IndividualAsset(asset["item_id"], location, asset["quantity"])
            individual_asset.set_parent(found_asset)
            found_asset.by_locations.append(individual_asset)
        return assets_grouped
