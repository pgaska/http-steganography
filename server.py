from http.server import BaseHTTPRequestHandler, HTTPServer
from http.client import HTTPMessage
from bitstring import BitArray

class myHandler(BaseHTTPRequestHandler):

    message =  ''

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        headers = str.split(str(self.headers))
        if headers.index("User-Agent:") < headers.index("Accept:"):
            myHandler.message += '0'
        else:
            myHandler.message += '1'
        if headers.index("Accept-Language:") < headers.index("Accept-Charset:"):
            myHandler.message += '0'
        else:
            myHandler.message += '1'
        if headers.index("Keep-Alive:") < headers.index("Connection:"):
            myHandler.message += '0'
        else:
            myHandler.message += '1'
        print(myHandler.message)

        if len(myHandler.message) >= 8:
            char_array = myHandler.message[:8]
            with open("out.txt", "ab") as f:
                bits = BitArray(bin=char_array)
                f.write(bits.bytes)
                myHandler.message = myHandler.message[8:]
                print(bits.bin)
                
            
    def do_POST(self):
        self.send_response(200)

with HTTPServer(("127.0.0.1", 8000), myHandler) as httpd:
    print("serving at port 8000")
    httpd.serve_forever()
