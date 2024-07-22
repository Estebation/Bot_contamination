import random
characters = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
ch_input = int(input("Introduce la longitud de la contraseña"))
password = ("")

for i in range(ch_input):
    password = password + random.choice(characters)

print(password)