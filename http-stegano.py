from mitmproxy import ctx
import http.client
from bitstring import BitArray
import random


class Counter:
    def __init__(self):
        self.i = 0
        self.antygona = ''
        with open("Sofokles - Antygona.txt", "rb") as f:
            byte = True
            while byte != b"":
                byte = f.read(1)
                bits = BitArray(byte)
                self.antygona += bits.bin

    def request(self, flow):
        ctx.log.warn(str(self.i))

        header_order = ["Host"]
        # ustalanie kolejności nagłówków na podstawie bitów w pliku
        if self.antygona[self.i]=='0':
            header_order.append("User-Agent")
            header_order.append("Accept")
        else:
            header_order.append("Accept")
            header_order.append("User-Agent")

        if self.antygona[self.i+1]=='0':
            header_order.append("Accept-Language")
            header_order.append("Accept-Charset")
        else:
            header_order.append("Accept-Charset")
            header_order.append("Accept-Language")

        if self.antygona[self.i+2]=='0':
            header_order.append("Keep-Alive")
            header_order.append("Connection")
        else:
            header_order.append("Connection")
            header_order.append("Keep-Alive")

        lines = []
        fill = []
        # zapisanie w odpowiedniej kolejności nagłówków
        for name in header_order:
            if name in flow.request.headers:
                lines.extend((name, flow.request.headers.get_all(name)[0]))
                del flow.request.headers[name]
        # dodanie reszty nieużywanych do steganografii
        fill.extend(flow.request.headers.fields)

        # usunięcie starego requesta http
        for header in fill:
            del flow.request.headers[header[0]]

        j = 0
        # utworzenie nowego requesta z odpowiednią kolejnością
        while j<len(lines)-1:
            flow.request.headers[lines[j]] = lines[j+1]
            j+=2

        for header in fill:
            flow.request.headers[header[0]] = header[1]

        print(flow.request.headers)
        self.i += 3
addons = [
    Counter()
]
