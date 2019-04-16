import http.client
from bitstring import BitArray
import random

ADDRESS = '192.168.1.198'
PORT = 8000
ITERATIONS = 86640 #dokładnie 20%
FILES = ['index.html', 'about.html', 'contact.html', 'industries.html', 'services.html',
         'aos.css', 'bootstrap.min.css', 'bootstrap-datepicker.css', 'jquery-ui.css', 'magnific-popup.css',
         'mediaelementplayer.css', 'owl.carousel.min.css', 'owl.theme.default.min.css', 'style.css',
         'blog_1.jpg', 'blog_2.jpg', 'blog_3.jpg', 'hero_bg_1.jpg', 'hero_bg_2.jpg', 'hero_bg_3.jpg', 'hero_bg_4.jpg',
         'img_1.jpg', 'img_2.jpg', 'img_3.jpg', 'img_4.jpg', 'img_5.jpg', 'person_1.jpg', 'person_2.jpg',
         'main.js']

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
    request_file = FILES[random.randint(0, len(FILES)-1)]

    conn = http.client.HTTPConnection(ADDRESS, PORT)
    conn.putrequest("GET","/"+request_file)
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