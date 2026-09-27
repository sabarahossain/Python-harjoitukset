import random

# Tietokone arpoo salaisen luvun väliltä 1-10
salainen_luku = random.randint(1, 10)

print("Tietokone on arvonut luvun väliltä 1–10. Arvaa se!")

while True:
    arvaus = int(input("Anna arvauksesi: "))
    
    if arvaus > salainen_luku:
        print("Liian suuri arvaus")
    elif arvaus < salainen_luku:
        print("Liian pieni arvaus")
    else:
        print("Oikein")
        break 
