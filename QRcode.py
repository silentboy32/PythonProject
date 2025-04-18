import qrcode as qr

image = qr.make("Enter Your Massage Here ")
image.save("Maked QR")
