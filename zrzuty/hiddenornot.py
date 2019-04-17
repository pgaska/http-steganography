import sys
import hashlib

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

UKRYTE=['17c13deb20eb6a820a5157fa181bebb1', '1ccff2f23d5a6a7a7ba4b0604ce8b04b', 'fa8977efdb712c83edca57dae41d6756',
        '13e5633f7d231a4cc253c3cc01e0297f', 'f13661e4e92434acd48d8925090da16f', 'dd73d26793eaf6e2bac1c69c954fb8eb',
        '0418885c1303a6d594a6ee7a844a4f64']

NIEUKRYTE=['607e2c8c25d234e44aa37bdf86eecdc6', '8c35099d19c8c263b0026c4f17aa0f73', 'a7bd3175176344ff01f5c1d983c8a76c',
           'e959b625048feca1c65fac7375a2921b', '1fe120afff00fa1f8d44320cdf8c3410', 'fd7580562e1bce7c19952fef1a80a7ef',
           'c76d7e403c480a40ec4105e3fdeffa74']

md5 = hashlib.md5()
sha1 = hashlib.sha1()

with open(sys.argv[1], 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        md5.update(data)
        sha1.update(data)

if md5.hexdigest() in UKRYTE:
    print('Ruch ukryty')
elif md5.hexdigest() in NIEUKRYTE:
    print('Ruch nieukryty')
else:
    print('Niepoprawny plik')