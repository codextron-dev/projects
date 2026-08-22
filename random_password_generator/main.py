import random
import string

length = int(input("Password length: "))

alphabet = string.ascii_letters

digits = string.digits

symbols = string.punctuation

chars = alphabet + digits + symbols

password = ""

for i in range(length):
    password += random.choice(chars)

print("Password: ",password)