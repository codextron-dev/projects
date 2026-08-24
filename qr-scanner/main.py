import cv2

# provide your image file here
file = "image.png"

img = cv2.imread(file)
detector = cv2.QRCodeDetector()
data, points, _ = detector.detectAndDecode(img)

print("QR Code Data: ", data)