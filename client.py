import http.client
from bitstring import BitArray
import random

ADDRESS = '127.0.0.1'
PORT = 8000
ITERATIONS = 86640 #dokładnie 20%

antygona = ''
with open("Sofokles - Antygona.txt", "rb") as f:
    byte = True
    while byte != b"":
        byte = f.read(1)
        bits = BitArray(byte)
        antygona += bits.bin

print(antygona)

i = 0

while i<ITERATIONS:
    conn = http.client.HTTPConnection(ADDRESS, PORT)
    conn.putrequest("GET","/index.html")
    if antygona[i]=='0':
        conn.putheader('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
        conn.putheader('Accept', '*/*')
    else:
        conn.putheader('Accept', '*/*')
        conn.putheader('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
    if antygona[i+1]=='0':
        conn.putheader('Accept-Language', 'en-us,en;q=0.5')
        conn.putheader('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
    else:
        conn.putheader('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
        conn.putheader('Accept-Language', 'en-us,en;q=0.5')
    if antygona[i+2]=='0':
        conn.putheader('Keep-Alive', '115')
        conn.putheader('Connection', 'Keep-Alive')
    else:
        conn.putheader('Connection', 'Keep-Alive')
        conn.putheader('Keep-Alive', '115')
    conn.putheader('Referer', 'https://developer.mozilla.org/en-US/docs/Web/JavaScript')
    conn.endheaders()
    i+=3
    res = conn.getresponse()
    print (res.status, res.reason)