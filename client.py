import http.client
from bitstring import BitArray


antygona = ''
with open("Sofokles - Antygona.txt", "rb") as f:
    byte = f.read(1)
    while byte != b"":
        byte = f.read(1)
        bits = BitArray(byte)
        antygona += bits.bin

print(antygona)

i = 0

while i<9:
    conn = http.client.HTTPConnection("127.0.0.1", 8000)
    conn.putrequest("GET","/index.html")
    if antygona[i]=='0':
        conn.putheader('Accept', '*/*')
        conn.putheader('Connection', 'Keep-Alive')
    else:
        conn.putheader('Connection', 'Keep-Alive')
        conn.putheader('Accept', '/*/')
    if antygona[i+1]=='0':
        conn.putheader('Accept-Language', 'en-us,en;q=0.5')
        conn.putheader('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
    else:
        conn.putheader('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
        conn.putheader('Accept-Language', 'en-us,en;q=0.5')
    conn.endheaders()
    i+=2
    res = conn.getresponse()
    print (res.status, res.reason)