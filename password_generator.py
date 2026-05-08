import random
import string

length = int(input("Şifre uzunluğu: "))

chars = string.ascii_letters + string.digits + "!@#$%"

password = "".join(random.choice(chars) for _ in range(length))

print("Şifre:", password)
