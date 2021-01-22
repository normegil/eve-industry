import os
import time
import requests
from cfg import eve_api
from cfg import application as application_cfg
import json
import threading
import logging

data_folder = "data"
filename = data_folder + "/refresh_token"
expires_safe_zone = 20
refresh_token_file_lock = threading.Lock()


class Tokens:
    def __init__(self, access_token=None, refresh_token=None, expires=None):
        if access_token is not None:
            self.__access_token = access_token
        if expires is not None:
            self.access_token_validity = self.__compute_token_validity(expires)
        if refresh_token is not None:
            self.refresh_token = refresh_token

    def __compute_token_validity(self, expires):
        return time.time() + expires - expires_safe_zone

    def __store(self):
        with refresh_token_file_lock:
            if not os.path.exists(data_folder):
                os.mkdir(data_folder)
            with open(filename, "w") as token_file:
                token_file.write(self.__refresh_token)

    def load(self):
        with refresh_token_file_lock:
            if not os.path.exists(filename) or not os.path.isfile(filename):
                return False

            with open(filename, "r") as token_file:
                token = token_file.read()
                if not token:
                    return False
                else:
                    self.__refresh_token = token
            return True

    @property
    def access_token(self):
        if not hasattr(self, "_Tokens__access_token") \
                or self.__access_token is None \
                or time.time() > self.access_token_validity:
            self.__refresh_tokens()
        return self.__access_token

    @access_token.setter
    def access_token(self, access_token):
        self.__access_token = access_token

    @property
    def refresh_token(self):
        return self.__refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        self.__refresh_token = refresh_token
        self.__store()

    def __refresh_tokens(self):
        logging.info("Refreshing token")
        resp = requests.post(eve_api.oauth_base_url_v2 + "/token",
                             auth=(application_cfg.client_id, application_cfg.secret_key),
                             headers={'Content-Type': 'application/x-www-form-urlencoded',
                                      'Host': eve_api.sso_base_address},
                             data={'grant_type': 'refresh_token', 'refresh_token': self.refresh_token})
        if resp.status_code >= 300:
            raise RuntimeError("Wrong response code: " + str(resp.status_code))

        tokens = json.loads(resp.content)
        self.access_token = tokens["access_token"]
        self.refresh_token = tokens["refresh_token"]
        self.access_token_validity = self.__compute_token_validity(tokens["expires_in"])
