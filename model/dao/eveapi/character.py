import json

import requests

from cfg import eve_api
from model.entities import Character


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
