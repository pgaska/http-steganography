from http.server import BaseHTTPRequestHandler, HTTPServer
from http.client import HTTPMessage

class myHandler(BaseHTTPRequestHandler):

    message =  ''

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        headers = str.split(str(self.headers))
        if headers.index("Accept:") < headers.index("Connection:"):
            myHandler.message += '0'
        else:
            myHandler.message += '1'
        if headers.index("Accept-Language:") < headers.index("Accept-Charset:"):
            myHandler.message += '0'
        else:
            myHandler.message += '1'
        print(myHandler.message)

    def do_POST(self):
        self.send_response(200)

with HTTPServer(("127.0.0.1", 8000), myHandler) as httpd:
    print("serving at port 8000")
    httpd.serve_forever()