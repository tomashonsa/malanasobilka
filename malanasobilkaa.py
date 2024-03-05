import random
for vysledek in range (10):
    print (vysledek)

def nasobeni (x, y):
    vysledek = x * y
    return vysledek

def kontrola(vysledek, volba):
    if vysledek == volba:
        print("Jsi šikulka máš to správně")
    else:
        print ("Jejda mas to spatne")


x = random.randint(1,10)
y = random.randint(1,10)
vysledek = nasobeni(x,y)


volba = input(f"{x} * {y} = ")

