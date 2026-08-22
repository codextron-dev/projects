import qrcode

text = input("Enter text or URL")

qr = qrcode.make(text)
qr.save("qrcode.png")

print("QR code saved as qrcode.png")