import threading
from http.server import HTTPServer

from cfg import application as application_cfg
from .handler import Handler


class Server:
    def __init__(self, queue, state):
        self.http_server = HTTPServer(('', application_cfg.oauth_http_callback_server_port), Handler)
        self.http_server.queue = queue
        self.http_server.state = state

    def listen(self):
        thread = threading.Thread(target=self.__start_server, daemon=True)
        thread.start()

    def __start_server(self):
        self.http_server.serve_forever()

    def close(self):
        self.http_server.shutdown()
