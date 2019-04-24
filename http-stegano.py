from mitmproxy import ctx
import http.client
# from bitstring import BitArray
import random

ADDRESS = '127.0.0.1'
PORT = 8000
ITERATIONS = 86640 #dokładnie 20%
i = 0
antygona = ''

def reorder(headers, header_order=["Host","User-Agent","Accept"]):
    lines = []
    for name in header_order:  # add existing headers in the specified order
        if name in headers:
            lines.extend(headers.get_all(name))
            del headers[name]
    lines.extend(headers.fields)  # all other headers
    print(lines)
    return lines



class Counter:
    def __init__(self, antygona):
        self.i = 0
        self.antygona = antygona

    def request(self, flow):
        ctx.log.warn(str(self.i))
        print(flow.request.headers)
        header_order = ["Host", "Accept", "User-Agent"]
        lines = []
        fill = []
        for name in header_order:  # add existing headers in the specified order
            if name in flow.request.headers:
                lines.extend((name, flow.request.headers.get_all(name)[0]))
                del flow.request.headers[name]
        fill.extend(flow.request.headers.fields)  # all other headers

        for header in fill:
            del flow.request.headers[header[0]]

        j = 0

        while j<len(lines)-1:
            flow.request.headers[lines[j]] = lines[j+1]
            j=j+2

        for header in fill:
            flow.request.headers[header[0]] = header[1]

        print(flow.request.headers)
        # flow.request.headers.fields = reorder(flow.request.headers)
addons = [
    Counter(antygona)
]