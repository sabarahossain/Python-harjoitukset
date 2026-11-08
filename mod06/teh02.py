import random

# 2. Muokatun funktion parametri
def heitä_noppaa(tahkot):
    # Arvotaan silmäluku väliltä 1 - tahkojen määrä
    return random.randint(1, tahkot)

# Pääohjelma
def pääohjelma():
    # Kysytään nopan tahkojen määrä käyttäjältä ja (int)
    tahkojen_määrä = int(input("Syötä nopan tahkojen yhteismäärä: "))
    
    heitto = 0
    
    while heitto != tahkojen_määrä:
        heitto = heitä_noppaa(tahkojen_määrä)  # Välitetään tahkojen määrä parametrina
        print(f"Heitit: {heitto}")

# Suoritetaan pääohjelma
pääohjelma()