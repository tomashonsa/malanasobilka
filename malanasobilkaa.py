import random


def nasobeni (x, y):
    vysledek = x * y
    return vysledek

def kontrola(vysledek, vysledek_zak):
    if vysledek == vysledek_zak:
        print("Jsi šikulka máš to správně")
    else:
        print ("Jejda mas to spatne")

x = random.randint(1,10)
y = random.randint(1,10)
vysledek = nasobeni(x,y)

vysledek_zak = input(f"{x} * {y} = ")
vysledek_zak = int(vysledek_zak)
kontrola(vysledek, vysledek_zak)


