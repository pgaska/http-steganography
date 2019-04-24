import http.client
import random

ADDRESS = '127.0.0.1'
PORT = 8000
ITERATIONS = 86640 #dokładnie 20%
FILES = ['index.html', 'about.html', 'contact.html', 'industries.html', 'services.html',
         'aos.css', 'bootstrap.min.css', 'bootstrap-datepicker.css', 'jquery-ui.css', 'magnific-popup.css',
         'mediaelementplayer.css', 'owl.carousel.min.css', 'owl.theme.default.min.css', 'style.css',
         'blog_1.jpg', 'blog_2.jpg', 'blog_3.jpg', 'hero_bg_1.jpg', 'hero_bg_2.jpg', 'hero_bg_3.jpg', 'hero_bg_4.jpg',
         'img_1.jpg', 'img_2.jpg', 'img_3.jpg', 'img_4.jpg', 'img_5.jpg', 'person_1.jpg', 'person_2.jpg',
         'main.js', 'aos.js', 'bootstrap.min.js', 'bootstrap-datepicker.min.js', 'mediaelement-and-player.min.js',
         'owl.carousel.min.js', 'slick.min.js']

i = 0

while i<ITERATIONS:
    request_file = FILES[random.randint(0, len(FILES)-1)]

    conn = http.client.HTTPConnection(ADDRESS, PORT)
    conn.putrequest("GET","/"+request_file)
    conn.putheader('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
    if request_file.endswith(".html"):
        conn.putheader('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    elif request_file.endswith(".jpg"):
        conn.putheader('Accept', 'image/*')
    else:
        conn.putheader('Accept', '*/*')

    conn.putheader('Accept-Language', 'en-us,en;q=0.5')
    conn.putheader('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')

    conn.putheader('Keep-Alive', '115')
    conn.putheader('Connection', 'Keep-Alive')

    conn.putheader('Referer', 'https://developer.mozilla.org/en-US/docs/Web/JavaScript')
    conn.endheaders()
    res = conn.getresponse()
    print (res.status, res.reason)