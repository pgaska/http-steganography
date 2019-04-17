from http.server import BaseHTTPRequestHandler, HTTPServer
from http.client import HTTPMessage
from bitstring import BitArray
from os import sep, curdir, path

class myHandler(BaseHTTPRequestHandler):

    message =  ''

    def do_GET(self):
        try:
            sendReply = False
            if self.path.endswith(".html"):
                mimetype = 'text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype = 'image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype = 'image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True
            if sendReply == True:
                f = open(curdir + sep + self.path, "rb")
                self.send_response(200)
                self.send_header('Accept-Ranges', 'bytes')
                self.send_header('Content-type', mimetype)
                self.send_header('Content-Length', path.getsize(curdir + sep + self.path))
                self.end_headers()
                self.wfile.write(f.read())
                f.close()

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

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)
                
            
    def do_POST(self):
        self.send_response(200)

with HTTPServer(("192.168.1.198", 8000), myHandler) as httpd:
    print("serving at port 8000")
    httpd.serve_forever()
