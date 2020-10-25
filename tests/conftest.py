import json
import http.server
from threading import Thread
from collections import namedtuple

import pytest

from hostedpi.pi import Pi


class MockCloudHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/pi':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.wfile.write(json.dumps({
                'servers': {
                    name: {'model': pi.model}
                    for name, pi in self.server._instances.items()
                }
            }).encode('utf-8'))
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/loginl
        self.send_error(404)


@pytest.fixture()
def mock_cloud(request):
    cloud = HTTPServer(('127.0.0.1', 8000), MockCloudHandler)
    cloud._instances = {}
    thread = Thread(target=cloud.serve_forever())
    thread.start()
    yield cloud
    cloud.shutdown()
    thread.join()
