import qrcode as qr
import random

n = ''
r = "1234567890"
for i in range(1,5):
    n += random.choice(r)

image = qr.make("Hello , Ritik Barman")
image.save(f"QR{n}")
print(f"QR{n}")
