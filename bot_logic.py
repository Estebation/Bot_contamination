import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

print( gen_pass(10))

def gen_emoji():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)


def moneda():
    moneda = random.randint(0, 2)
    if moneda == 0:
        return "CARA"
    else:
        return "CRUZ"
 