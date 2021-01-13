import uuid
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs


class Handler(BaseHTTPRequestHandler):
    # noinspection PyPep8Naming
    def do_GET(self):
        query_params = parse_qs(self.path[2:])
        code = query_params['code'][0]
        state = uuid.UUID(query_params['state'][0])
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"Code received: {code}\n\nYou can close this page.".encode())
        if self.server.state == state:
            self.server.queue.put(code)
        else:
            print("Error: wrong state returned")
        self.server.queue.put("end")
