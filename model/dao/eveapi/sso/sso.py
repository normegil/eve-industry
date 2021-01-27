import json
import logging
import queue
import urllib.parse
import uuid
import webbrowser

import requests

from model.dao.eveapi.sso.httpserver import Server
from cfg import application as application_cfg
from cfg import eve_api
from .tokens import Tokens


class EveAuth:
    def authenticate(self):

        logging.info("Requesting new authentication informations")
        code = self.__resquest_authorization_code()
        return self.__request_new_tokens(code)

    def __resquest_authorization_code(self):
        q = queue.Queue()
        state = uuid.uuid4()

        srv = Server(q, state)
        srv.listen()

        payload = urllib.parse.urlencode({
            'response_type': 'code',
            'client_id': application_cfg.client_id,
            'scope': 'publicData esi-calendar.read_calendar_events.v1 esi-location.read_location.v1 '
                     'esi-wallet.read_character_wallet.v1 esi-characters.read_contacts.v1 '
                     'esi-universe.read_structures.v1 esi-assets.read_assets.v1 esi-planets.manage_planets.v1 '
                     'esi-ui.open_window.v1 esi-markets.structure_markets.v1 esi-characters.read_loyalty.v1 '
                     'esi-characters.read_opportunities.v1 esi-characters.read_standings.v1 '
                     'esi-characters.read_agents_research.v1 esi-industry.read_character_jobs.v1 '
                     'esi-markets.read_character_orders.v1 esi-characters.read_blueprints.v1 '
                     'esi-characters.read_corporation_roles.v1 esi-contracts.read_character_contracts.v1 '
                     'esi-clones.read_implants.v1 esi-wallet.read_corporation_wallets.v1 '
                     'esi-corporations.read_contacts.v1 esi-assets.read_corporation_assets.v1 '
                     'esi-contracts.read_corporation_contracts.v1 esi-corporations.read_standings.v1 '
                     'esi-corporations.read_starbases.v1 esi-industry.read_corporation_jobs.v1 '
                     'esi-markets.read_corporation_orders.v1 esi-industry.read_character_mining.v1 '
                     'esi-industry.read_corporation_mining.v1 esi-planets.read_customs_offices.v1 '
                     'esi-corporations.read_facilities.v1 esi-alliances.read_contacts.v1 esi-characterstats.read.v1 ',
            'state': state,
            'redirect_uri': 'http://localhost:' + str(eve_api.oauth_http_callback_server_port) + "/"
        })
        webbrowser.open(eve_api.oauth_base_url_v2 + "/authorize?" + payload, new=2)

        code = ""
        msg = ""
        while "end" != msg:
            msg = q.get()
            if "end" != msg:
                code = msg
        srv.close()
        return code

    def __request_new_tokens(self, code):
        resp = requests.post(eve_api.oauth_base_url_v2 + "/token",
                             auth=(application_cfg.client_id, application_cfg.secret_key),
                             headers={'Content-Type': 'application/x-www-form-urlencoded',
                                      'Host': eve_api.sso_base_address},
                             data={'grant_type': 'authorization_code', 'code': code})

        if resp.status_code >= 300:
            raise RuntimeError("Wrong response code: " + str(resp.status_code))

        tokens = json.loads(resp.content)
        return Tokens(tokens["access_token"], tokens["refresh_token"], tokens["expires_in"])
