import random

# 1. Kirjoitan parametriton funktio, joka palauttaa silmäluvun väliltä 1-6
def heitä_noppaa():
    # random.randint(1, 6)
    return random.randint(1, 6)

# Pääohjelma
def pääohjelma():
    heitto = 0
    
    # Heitetään noppaa niin kauan, kunnes saadaan kutonen
    while heitto != 6:
        heitto = heitä_noppaa()  # Kutsutaan funktiota
        print(f"Heitit: {heitto}")  # Tulostetaan kunkin heiton tulos

# Suoritetaan pääohjelma
pääohjelma()
