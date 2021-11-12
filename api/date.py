import sys
from datetime import datetime
from http.server import BaseHTTPRequestHandler

import jinja2
from jinja2 import Template

print('Python version: ', sys.version_info)
print('Jinja version: ', jinja2.__version__)


class handler(BaseHTTPRequestHandler):

  template = Template('{ "date": "{{ date }}"}')

  def _render(self, context):

    return self.template.render(context)

  def do_GET(self):
    context = {
      'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }
    s = self._render(context)

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(s.encode())

    return
